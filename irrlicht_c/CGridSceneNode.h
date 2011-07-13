#ifndef __C_GRID_SCENE_NODE_H__
#define __C_GRID_SCENE_NODE_H__

#include "ISceneNode.h"
#include "SMeshBuffer.h"

//! Grid scene node
/*! If you need a grid on the XY or ZY axis, simply rotate this node by 90 
degrees in the appropiate axis.
This node creates an XZ grid by default, which should be fine for normal use.
Axis Lines are a default Red and Blue for the X and Z axis respectively.

Please note that the internal meshbuffer used for the grid has a max size of 65535 indecies.

Thanks goes to MasterGod for helping to clean up the code and for a few bug fixes.

Additional thanks to:
JP for optimising the rendering.
Vins for fixing a nasty crash bug and optimising memory usage.
*/

namespace irr
{
namespace scene
{

class CGridSceneNode : public ISceneNode
{
public:
	//! Constructor
	CGridSceneNode(ISceneNode* parent, ISceneManager* smgr, s32 id = -1, 
		u32 spacing = 8, u32 size = 1024, video::SColor gridcolor = video::SColor(255,128,128,128),
		u32 accentlineoffset = 8, video::SColor accentgridcolor = video::SColor(255,192,192,192),
		bool axislinestate = false);

	//! Will create a copy of this scenenode and it's settings
	virtual CGridSceneNode* clone(ISceneNode* newParent = 0, ISceneManager* newSceneManager = 0);

	//! Pre-Register stuff
	virtual void OnRegisterSceneNode();

	//! Render our grid using 3D lines stored inside the internal meshbuffer
	virtual void render();

	//! Returns our bounding box
	virtual const core::aabbox3d<f32>& getBoundingBox() const;

	//! Returns the total number of materials, in this case, only 1
	virtual u32 getMaterialCount();

	//! Returns the only material
	virtual video::SMaterial& getMaterial(u32 i);

	//! Will cause the grid scene node to rebuild it's grid
	void RegenerateGrid();

	//! Returns the Spacing of the grid
	u32 GetSpacing();

	//! Returns the total size of the grid
	u32 GetSize();

	//! Returns the Grid Color
	video::SColor GetGridColor();

	//! Returns the offset of the accent lines
	u32 GetAccentlineOffset();

	//! Returns the Accent Line Color
	video::SColor GetAccentlineColor();

	//! Returns the Active State of the Axis Lines
	bool AreAxisLineActive();

	//! Returns the Color of the "X" axis lines
	video::SColor GetAxisLineXColor();

	//! Returns the Color of the "Z" axis lines
	video::SColor GetAxisLineZColor();

	//! Sets Spacing
	void SetSpacing(u32 newspacing);

	//! Sets Size
	void SetSize(u32 newsize);

	//! Sets the general grid color
	void SetGridColor(video::SColor newcolor);

	//! Sets the offset for the accent lines
	//! If > 0, accent lines will be active, otherwise not
	void SetAccentlineOffset(u32 newoffset);

	//! Sets the color of the accent lines
	void SetAccentlineColor(video::SColor newcolor);

	//! Sets whether the lines denoting the center of the grid are active
	void SetAxisLineActive(bool active);

	//! Sets the Color of the "X" axis lines
	void SetAxisLineXColor(video::SColor XLine);
	
	//! Sets the Color of the "Z" axis lines
	void SetAxisLineZColor(video::SColor ZLine);

	//! Allows for setting a complete new material
	void SetMaterial(video::SMaterial newMaterial);

private:
	u32 m_spacing;
	u32 m_size;
	video::SColor m_gridcolor;
	video::SColor m_accentgridcolor;
	u32 m_accentlineoffset;
	bool m_AxisLineState;
	video::SColor m_XLineColor;
	video::SColor m_ZLineColor;

	SMeshBuffer Buffer;
};

//==================START from CGridSceneNode.cpp==================
CGridSceneNode::CGridSceneNode(ISceneNode* parent, ISceneManager* smgr, s32 id, 
		u32 spacing, u32 size, video::SColor gridcolor, u32 accentlineoffset, 
		video::SColor accentgridcolor, bool axislinestate)	: ISceneNode(parent, smgr, id), 
		m_spacing(spacing), m_size(size), 
		m_gridcolor(gridcolor), m_accentgridcolor(accentgridcolor),
        m_accentlineoffset(accentlineoffset), m_AxisLineState(axislinestate),
		m_XLineColor(video::SColor(255,255,0,0)), m_ZLineColor(video::SColor(255,0,0,255))
{
	// Set the material
	Buffer.Material.Wireframe = false;
	Buffer.Material.Lighting = false;
	Buffer.Material.Thickness = 1;
	Buffer.Material.FogEnable = false;
	Buffer.Material.ZWriteEnable = false;

	// Set the default culling state to Frustum Box
	AutomaticCullingState = EAC_FRUSTUM_BOX;

	RegenerateGrid();
}

CGridSceneNode* CGridSceneNode::clone(ISceneNode *newParent, ISceneManager *newSceneManager)
{
	if (!newParent) newParent = Parent;
	if (!newSceneManager) newSceneManager = SceneManager;

	CGridSceneNode* clone = new CGridSceneNode(
		Parent,
		SceneManager,
		ID,
		m_spacing,
		m_size*2,
		m_gridcolor,
		m_accentlineoffset,
		m_accentgridcolor,
		m_AxisLineState);

	if(!clone)
		return 0x0;

	clone->SetAxisLineXColor(m_XLineColor);
	clone->SetAxisLineZColor(m_ZLineColor);
	clone->SetMaterial(Buffer.Material);

	clone->drop();
	return clone;
}

void CGridSceneNode::OnRegisterSceneNode()
{
	if (IsVisible)
		SceneManager->registerNodeForRendering(this);

	ISceneNode::OnRegisterSceneNode();
}

void CGridSceneNode::RegenerateGrid()
{
	//Clean up memory
	Buffer.Indices.clear();
	Buffer.Vertices.clear();

	u32 m_numVertices = ((m_size / m_spacing) + 1) * 2 * 2;
	if (m_accentlineoffset) m_numVertices += ((m_size / (m_spacing * m_accentlineoffset)) + 1) * 2 * 2;

	if ( m_numVertices > 65535)
	{
		//Too many vertices on 16 bit for for 16bit indices of SMeshBuffer
		//Returning with a blank buffer to avoid segfaulting the entire application
		return;
	}

	//Set our left corner
	core::vector3df leftMost = core::vector3df(0,0,0);
	leftMost.X -= m_size/2;
	leftMost.Z -= m_size/2;

	//Set our right corner
	core::vector3df rightMost = core::vector3df(0,0,0);
	rightMost.X += m_size/2;
	rightMost.Z += m_size/2;

	u32 indexIndex = 0;

	//X-axis lines
	for(u32 x = 0; x <= m_size; x+= m_spacing)
	{
		core::vector3df start = leftMost;
		start.X += x ;

		core::vector3df end = rightMost;
		end.X = start.X;

		Buffer.Vertices.push_back(video::S3DVertex(start, core::vector3df(0,1,0), m_gridcolor, core::vector2df(0.0f, 0.0f)));
		Buffer.Vertices.push_back(video::S3DVertex(end, core::vector3df(0,1,0), m_gridcolor, core::vector2df(0.0f, 0.0f)));

		Buffer.Indices.push_back(indexIndex++);
		Buffer.Indices.push_back(indexIndex++);
	}

	//Z-axis lines
	for(u32 z = 0; z <= m_size; z+= m_spacing)
	{
		core::vector3df start = leftMost;
		start.Z += z ;

		core::vector3df end = rightMost;
		end.Z = start.Z;

		Buffer.Vertices.push_back(video::S3DVertex(start, core::vector3df(0,1,0), m_gridcolor, core::vector2df(0.0f, 0.0f)));
		Buffer.Vertices.push_back(video::S3DVertex(end, core::vector3df(0,1,0), m_gridcolor, core::vector2df(0.0f, 0.0f)));

		Buffer.Indices.push_back(indexIndex++);
		Buffer.Indices.push_back(indexIndex++);
	}

	//Accent lines are only drawn if the offset is greater than 0
	if(m_accentlineoffset > 0)
	{
		//X-axis
		for(u32 x = 0; x <= m_size; x+= m_spacing*m_accentlineoffset)
		{
			core::vector3df start = leftMost;
			start.X += x ;

			core::vector3df end = rightMost;
			end.X = start.X;

			Buffer.Vertices.push_back(video::S3DVertex(start, core::vector3df(0,1,0), m_accentgridcolor, core::vector2df(0.0f, 0.0f)));
			Buffer.Vertices.push_back(video::S3DVertex(end, core::vector3df(0,1,0), m_accentgridcolor, core::vector2df(0.0f, 0.0f)));

			Buffer.Indices.push_back(indexIndex++);
			Buffer.Indices.push_back(indexIndex++);
		}

		//Z-axis
		for(u32 z = 0; z <= m_size; z+= m_spacing*m_accentlineoffset)
		{
			core::vector3df start = leftMost;
			start.Z += z ;

			core::vector3df end = rightMost;
			end.Z = start.Z;

			Buffer.Vertices.push_back(video::S3DVertex(start, core::vector3df(0,1,0), m_accentgridcolor, core::vector2df(0.0f, 0.0f)));
			Buffer.Vertices.push_back(video::S3DVertex(end, core::vector3df(0,1,0), m_accentgridcolor, core::vector2df(0.0f, 0.0f)));

			Buffer.Indices.push_back(indexIndex++);
			Buffer.Indices.push_back(indexIndex++);
		}
	}


	// Create our box, it is the size of the grid exactly, plus 1 in the Y axis
	Buffer.BoundingBox = core::aabbox3df(-(f32)m_size/2,-0.5f,-(f32)m_size/2,(f32)m_size/2,0.5f,(f32)m_size/2);
}

void CGridSceneNode::render()
{
	video::IVideoDriver* driver = SceneManager->getVideoDriver();

	//Prep to render
	if(driver)
	{
		driver->setMaterial(Buffer.Material);
		driver->setTransform(video::ETS_WORLD, AbsoluteTransformation);

		driver->drawVertexPrimitiveList(Buffer.getVertices(), Buffer.getVertexCount(), Buffer.getIndices(), Buffer.getVertexCount()/2, video::EVT_STANDARD, scene::EPT_LINES);

		// Axis Lines are only drawn if the State is true
		if(m_AxisLineState)
		{
			driver->draw3DLine(core::vector3df((f32)m_size,0,0),core::vector3df(-(f32)m_size,0,0),m_XLineColor);
			driver->draw3DLine(core::vector3df(0,0,(f32)m_size),core::vector3df(0,0,-(f32)m_size),m_ZLineColor);
		}
	}
}

const core::aabbox3d<f32>& CGridSceneNode::getBoundingBox() const
{
	return Buffer.BoundingBox;
}

u32 CGridSceneNode::getMaterialCount()
{
	return 1;
}

video::SMaterial& CGridSceneNode::getMaterial(u32 i)
{
	return Buffer.Material;
}

u32 CGridSceneNode::GetSpacing()
{
	return m_spacing;
}

u32 CGridSceneNode::GetSize()
{
	return m_size;
}

u32 CGridSceneNode::GetAccentlineOffset()
{
	return m_accentlineoffset;
}

video::SColor CGridSceneNode::GetAccentlineColor()
{
	return m_accentgridcolor;
}

video::SColor CGridSceneNode::GetGridColor()
{
	return m_gridcolor;
}

bool CGridSceneNode::AreAxisLineActive()
{
	return m_AxisLineState;
}

video::SColor CGridSceneNode::GetAxisLineXColor()
{
	return m_XLineColor;
}

video::SColor CGridSceneNode::GetAxisLineZColor()
{
	return m_ZLineColor;
}

void CGridSceneNode::SetSpacing(u32 newspacing)
{
	m_spacing = newspacing;
	RegenerateGrid();
}

void CGridSceneNode::SetSize(u32 newsize)
{
	m_size = newsize;
	RegenerateGrid();
}

void CGridSceneNode::SetAccentlineColor(video::SColor newcolor)
{
	m_accentgridcolor = newcolor;
	RegenerateGrid();
}

void CGridSceneNode::SetAccentlineOffset(u32 newoffset)
{
	m_accentlineoffset = newoffset;
	RegenerateGrid();
}

void CGridSceneNode::SetGridColor(video::SColor newcolor)
{
	m_gridcolor = newcolor;
	RegenerateGrid();
}

void CGridSceneNode::SetAxisLineActive(bool active)
{
	m_AxisLineState = active;
}

void CGridSceneNode::SetAxisLineXColor(video::SColor XLine)
{
	m_XLineColor = XLine;
}

void CGridSceneNode::SetAxisLineZColor(video::SColor ZLine)
{
	m_ZLineColor = ZLine;
}

void CGridSceneNode::SetMaterial(video::SMaterial newMaterial)
{
	Buffer.Material = newMaterial;
}
//==================END from CGridSceneNode.cpp==================

};// end namespace scene
};// end namespace irr

#endif // __C_GRID_SCENE_NODE_H__

