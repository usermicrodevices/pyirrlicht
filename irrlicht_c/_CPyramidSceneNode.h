// Copyright(c) Max Kolosov 2023 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

class CPyramidSceneNode : public scene::ISceneNode
{
	f32 _height_;
	f32 _hpos_;
	f32 _base_size_;
	video::SColor _color_;
	core::aabbox3d<f32> Box;
	video::S3DVertex Vertices[5];
	video::SMaterial Material;

public:
	CPyramidSceneNode(scene::ISceneNode* parent, ISceneManager* smgr, s32 id = -1, f32 height = 10.0, f32 hpos = 0.0, f32 base_size = 10.0, const video::SColor& color = video::SColor(255,128,128,128)) : scene::ISceneNode(parent, smgr, id), _height_(height), _hpos_(hpos), _base_size_(base_size), _color_(color)
	{
		Material.Wireframe = false;
		Material.Lighting = false;
		Vertices[0] = video::S3DVertex(core::vector3df(_base_size_,_hpos_,_base_size_), core::vector3df(1.0,0.0,1.0), _color_, core::vector2df(0.0, 1.0));
		Vertices[1] = video::S3DVertex(core::vector3df(_base_size_,_hpos_,-_base_size_), core::vector3df(1.0,0.0,-1.0), _color_, core::vector2df(1.0, 1.0));
		Vertices[2] = video::S3DVertex(core::vector3df(-_base_size_,_hpos_,-_base_size_), core::vector3df(-1.0,0.0,-1.0), _color_, core::vector2df(0.0, 0.0));
		Vertices[3] = video::S3DVertex(core::vector3df(-_base_size_,_hpos_,_base_size_), core::vector3df(-1.0,0.0,1.0), _color_, core::vector2df(0.0, 0.0));
		Vertices[4] = video::S3DVertex(core::vector3df(0.0,_hpos_+_height_,0.0), core::vector3df(0.0,1.0,0.0), _color_, core::vector2df(1.0, 0.0));
		Box.reset(Vertices[0].Pos);
		for (s32 i=1; i<5; ++i)
			Box.addInternalPoint(Vertices[i].Pos);
	}

	virtual void OnRegisterSceneNode()
	{
		if (IsVisible)
			SceneManager->registerNodeForRendering(this);
		scene::ISceneNode::OnRegisterSceneNode();
	}

	virtual void render()
	{
		u16 indices[] = {0,4,1, 1,4,2, 2,4,3, 3,4,0, 0,1,2, 1,2,3};
		video::IVideoDriver* driver = SceneManager->getVideoDriver();
		driver->setMaterial(Material);
		driver->setTransform(video::ETS_WORLD, AbsoluteTransformation);
		driver->drawVertexPrimitiveList(&Vertices[0], 6, &indices[0], 6, video::EVT_STANDARD, scene::EPT_TRIANGLES, video::EIT_16BIT);
	}

	virtual const core::aabbox3d<f32>& getBoundingBox() const
	{
		return Box;
	}

	virtual u32 getMaterialCount() const
	{
		return 1;
	}

	virtual video::SMaterial& getMaterial(u32 i)
	{
		return Material;
	}	
};

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API CPyramidSceneNode* CPyramidSceneNode_ctor(scene::ISceneNode* parent, scene::ISceneManager* mgr, s32 id, f32 height, f32 hpos, f32 base_size, const video::SColor& color)
{return new CPyramidSceneNode(parent, mgr, id, height, hpos, base_size, color);}

#ifdef __cplusplus
}
#endif
