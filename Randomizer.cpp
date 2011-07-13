// Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#include <ctime>

#include <irrlicht.h>

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;
 
#ifdef _IRR_WINDOWS_
#pragma comment(lib, "Irrlicht.lib")
#pragma comment(linker, "/subsystem:windows /ENTRY:mainCRTStartup")
#endif

class UserIEventReceiver : public IEventReceiver
{
public:
	virtual bool OnEvent(const SEvent& event)
	{
		if (event.EventType == irr::EET_KEY_INPUT_EVENT)
			KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown;

		if (!event.KeyInput.PressedDown && (event.KeyInput.Key >= KEY_KEY_0 || event.KeyInput.Key <= KEY_KEY_9 || event.KeyInput.Key >= KEY_NUMPAD0 || event.KeyInput.Key <= KEY_NUMPAD9))
		{
			key_value = 0;
			switch (event.KeyInput.Key)
			{
				case KEY_KEY_0:
					key_value = 0;
					break;
				case KEY_KEY_1:
					key_value = 1;
					break;
				case KEY_KEY_2:
					key_value = 2;
					break;
				case KEY_KEY_3:
					key_value = 3;
					break;
				case KEY_KEY_4:
					key_value = 4;
					break;
				case KEY_KEY_5:
					key_value = 5;
					break;
				case KEY_KEY_6:
					key_value = 6;
					break;
				case KEY_KEY_7:
					key_value = 7;
					break;
				case KEY_KEY_8:
					key_value = 8;
					break;
				case KEY_KEY_9:
					key_value = 9;
					break;
				case KEY_NUMPAD0:
					key_value = 0;
					break;
				case KEY_NUMPAD1:
					key_value = 1;
					break;
				case KEY_NUMPAD2:
					key_value = 2;
					break;
				case KEY_NUMPAD3:
					key_value = 3;
					break;
				case KEY_NUMPAD4:
					key_value = 4;
					break;
				case KEY_NUMPAD5:
					key_value = 5;
					break;
				case KEY_NUMPAD6:
					key_value = 6;
					break;
				case KEY_NUMPAD7:
					key_value = 7;
					break;
				case KEY_NUMPAD8:
					key_value = 8;
					break;
				case KEY_NUMPAD9:
					key_value = 9;
					break;
			}
			if (first)
			{
				answer_buffer[1] = key_value;
				first = false;
			}
			else
			{
				answer_buffer[0] = key_value;
				first = true;
			}
			answer = answer_buffer[1] + answer_buffer[0] *10;
		}

		return false;
	}

	virtual bool IsKeyDown(EKEY_CODE keyCode) const
	{
		return KeyIsDown[keyCode];
	}
	
	UserIEventReceiver()
	{
		for (u32 i=0; i<KEY_KEY_CODES_COUNT; ++i)
			KeyIsDown[i] = false;
		answer = -1;
		answer_buffer[0] = answer;
		answer_buffer[1] = answer;
		first = true;
	}

	int answer;

private:
	bool KeyIsDown[KEY_KEY_CODES_COUNT], first;
	int key_value, answer_buffer[2];
};

int randrange(int rnd_min = 0, int rnd_max = RAND_MAX)
{
	return rand () % (rnd_max - rnd_min + 1) + rnd_min;
}

ITexture* texture_generator(IVideoDriver* driver, video::ECOLOR_FORMAT image_format = ECF_R8G8B8, const dimension2d<u32>& image_size = dimension2d<u32>(2, 2), char* texture_name = "texture_01", u32 alpha_value = 128, u32 red1 = 0, u32 red2 = 255, u32 green1 = 0, u32 green2 = 255, u32 blue1 = 0, u32 blue2 = 255)
{
	int row, column;
	IImage* image = driver->createImage(image_format, image_size);
	int alpha = 0;
	bool blend = false;
	video::ECOLOR_FORMAT color_format = image->getColorFormat();
	if (color_format == ECF_A1R5G5B5 || color_format == ECF_A8R8G8B8 || color_format == ECF_A16B16G16R16F || color_format == ECF_A32B32G32R32F)
	{
		alpha = alpha_value;
		blend = true;
	}
	for (row = 0; row < image_size.Height; row++)
	{
		for (column = 0; column < image_size.Width; column++)
			image->setPixel(row, column, SColor(alpha, randrange(red1, red2), randrange(green1, green2), randrange(blue1, blue2)), blend);
	}
	return driver->addTexture(texture_name, image);
}

ITriangleSelector* create_wall_plane_selector(ISceneManager* scene_manager, const IGeometryCreator* i_geometry_creator, const dimension2df& tileSize, const dimension2du& tileCount, SMaterial* material, const dimension2df& textureRepeatCount, const vector3df& pos, const vector3df& rotation)
{
	IMesh* i_mesh = i_geometry_creator->createPlaneMesh(tileSize, tileCount, material, textureRepeatCount);
	IMeshSceneNode* i_mesh_scene_node = scene_manager->addMeshSceneNode(i_mesh);
	i_mesh_scene_node->setPosition(pos);
	i_mesh_scene_node->setRotation(rotation);
	ITriangleSelector* selector = scene_manager->createTriangleSelector(i_mesh_scene_node->getMesh(), i_mesh_scene_node);
	i_mesh_scene_node->setTriangleSelector(selector);
	return selector;
}

int main()
{
	int tile_count = randrange(10, 100);
	int height = 200;
	int tile_len = 100;
	bool texture_from_file = false;//true;
	f32 p = (f32)(tile_count * tile_len / 2);
	int a = 0;
	int b = 0;
	wchar_t msg[100], check_answer[100];
	ITexture* texture;
	ISceneNode* sky_node;
	IGUIWindow* dlg = 0;

	const dimension2d<u32>& windowSize = dimension2d<u32>(640, 480);
	IrrlichtDevice* device = createDevice(video::EDT_OPENGL, windowSize, 16, false, false, false, 0);
	if (!device)
		return 1;

	device->setWindowCaption(L"Hello World! - Irrlicht Engine Demo");
	device->setResizable(true);
	IVideoDriver* driver = device->getVideoDriver();
	ISceneManager* scene_manager = device->getSceneManager();
	IGUIEnvironment* guienv = device->getGUIEnvironment();

	IGUIFont* from_file_font = guienv->getFont(L"lang//multi_Arial_36.xml");
	IGUISkin* skin = guienv->getSkin();
	skin->setFont(from_file_font);
	IGUIStaticText* i_gui_static_text = guienv->addStaticText(L"", recti(0, 0, windowSize.Width, windowSize.Height));

	const IGeometryCreator* i_geometry_creator = scene_manager->getGeometryCreator();

	if (texture_from_file)
		sky_node = scene_manager->addSkyDomeSceneNode(driver->getTexture(L"media//skydome.jpg"));
	else
	{
		srand((unsigned)time(NULL));
		texture = texture_generator(driver, ECF_R8G8B8, dimension2d<u32>(32, 32), "skydome");
		sky_node = scene_manager->addSkyDomeSceneNode(texture);
	}

	const dimension2d<f32>& tileSize = dimension2d<f32>((f32)tile_len, (f32)tile_len);
	dimension2d<u32>& tileCount = dimension2d<u32>(tile_count, tile_count);
	dimension2d<f32>& textureRepeatCount = dimension2d<f32>((f32)tile_count, (f32)tile_count);
	SMaterial* material = new SMaterial();
	material->EmissiveColor = SColor(0,255,255,255);
	if (texture_from_file)
		texture = driver->getTexture(L"media//stones.jpg");
	else
		texture = texture_generator(driver, ECF_R8G8B8, dimension2d<u32>(32, 32), "bottom");
	material->setTexture(0, texture);

	IMesh* i_mesh_top = i_geometry_creator->createPlaneMesh(tileSize, tileCount, material, textureRepeatCount);
	material->MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL;
	if (texture_from_file)
		texture = driver->getTexture(L"media//opengllogo.png");
	else
		texture = texture_generator(driver, ECF_A8R8G8B8, dimension2d<u32>(8, 8), "top");
	material->setTexture(0, texture);

	IMesh* i_mesh_bottom = i_geometry_creator->createPlaneMesh(tileSize, tileCount, material, textureRepeatCount);
	IMeshSceneNode* i_mesh_scene_node_top = scene_manager->addOctreeSceneNode(i_mesh_top);
	IMeshSceneNode* i_mesh_scene_node_bottom = scene_manager->addOctreeSceneNode(i_mesh_bottom, i_mesh_scene_node_top);
	i_mesh_scene_node_bottom->setPosition(vector3df(0,(f32)height,0));
	i_mesh_scene_node_bottom->setRotation(vector3df(180,0,0));
	ITriangleSelector* selector_top = scene_manager->createOctreeTriangleSelector(i_mesh_scene_node_top->getMesh(), i_mesh_scene_node_top);
	ITriangleSelector* selector_bottom = scene_manager->createOctreeTriangleSelector(i_mesh_scene_node_bottom->getMesh(), i_mesh_scene_node_bottom);
	i_mesh_scene_node_top->setTriangleSelector(selector_top);
	i_mesh_scene_node_bottom->setTriangleSelector(selector_bottom);

	// left, right, front and back plane
	tileCount.Height = height / tile_len;
	textureRepeatCount.Height = (f32)(height / tile_len);
	if (texture_from_file)
	{
		material->MaterialType = EMT_LIGHTMAP;
		texture = driver->getTexture(L"media//wall.jpg");
	}
	else
		texture = texture_generator(driver, ECF_A8R8G8B8, dimension2d<u32>(64, 64), "front");
	material->setTexture(0, texture);
	ITriangleSelector* selector_front = create_wall_plane_selector(
		scene_manager,
		i_geometry_creator, 
		tileSize, 
		tileCount, 
		material, 
		textureRepeatCount, 
		vector3df(0, (f32)height / 2, p), 
		vector3df(-90,0,0));
	if (!texture_from_file)
	{
		material->MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL;
		texture = texture_generator(driver, ECF_A8R8G8B8, dimension2d<u32>(64, 64), "back");
	}
	material->setTexture(0, texture);
	ITriangleSelector* selector_back = create_wall_plane_selector(
		scene_manager,
		i_geometry_creator, 
		tileSize, 
		tileCount, 
		material, 
		textureRepeatCount, 
		vector3df(0, (f32)height / 2, -p), 
		vector3df(90,0,0));
	if (!texture_from_file)
	{
		material->MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL;
		texture = texture_generator(driver, ECF_A8R8G8B8, dimension2d<u32>(64, 64), "left");
	}
	material->setTexture(0, texture);
	ITriangleSelector* selector_left = create_wall_plane_selector(
		scene_manager,
		i_geometry_creator, 
		tileSize, 
		tileCount, 
		material, 
		textureRepeatCount, 
		vector3df(-p, (f32)height / 2, 0),
		vector3df(90,90,0));
	if (!texture_from_file)
	{
		material->MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL;
		texture = texture_generator(driver, ECF_A8R8G8B8, dimension2d<u32>(64, 64), "right");
	}
	material->setTexture(0, texture);
	ITriangleSelector* selector_right = create_wall_plane_selector(
		scene_manager,
		i_geometry_creator, 
		tileSize, 
		tileCount, 
		material, 
		textureRepeatCount, 
		vector3df(p, (f32)height / 2, 0),
		vector3df(90,-90,0));

	// ADD MAGIC VOLUME
	IMeshSceneNode* i_scene_node = scene_manager->addSphereSceneNode(40.0f, 16, 0, 1, vector3df(0,60,0));
	if (i_scene_node)
	{
		i_scene_node->getMaterial(0).MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL;
		texture = texture_generator(driver, ECF_A8R8G8B8, dimension2d<u32>(4, 4), "magic", 50, 50, 100, 50, 100, 50, 100);
		i_scene_node->setMaterialTexture(0, texture);
	}
	ITriangleSelector* selector_magic = scene_manager->createTriangleSelector(i_scene_node->getMesh(), i_scene_node);
	i_scene_node->setTriangleSelector(selector_magic);
	i_scene_node->setName("magic_scene_node");

	// addCameraSceneNodeFPS(self, parent = ISceneNode(0), rotateSpeed = 100->0, moveSpeed = 0->5, id = -1, keyMapArray = SKeyMap(0), keyMapSize = 0, noVerticalMovement = False, jumpSpeed = 0->0, invertMouse = False):
	ICameraSceneNode* camera = scene_manager->addCameraSceneNodeFPS(i_mesh_scene_node_top);
	camera->setPosition(vector3df(100,60,0));

	IMetaTriangleSelector* i_meta_triangle_selector = scene_manager->createMetaTriangleSelector();
	i_meta_triangle_selector->addTriangleSelector(selector_top);
	i_meta_triangle_selector->addTriangleSelector(selector_bottom);
	i_meta_triangle_selector->addTriangleSelector(selector_front);
	i_meta_triangle_selector->addTriangleSelector(selector_back);
	i_meta_triangle_selector->addTriangleSelector(selector_left);
	i_meta_triangle_selector->addTriangleSelector(selector_right);
	i_meta_triangle_selector->addTriangleSelector(selector_magic);

	// createCollisionResponseAnimator(self, world, sceneNode, ellipsoidRadius = vector3df(30,60,30), gravityPerSecond = vector3df(0,-10->0,0), ellipsoidTranslation = vector3df(0,0,0), slidingValue = 0->0005):
	ISceneNodeAnimatorCollisionResponse* anim = scene_manager->createCollisionResponseAnimator(i_meta_triangle_selector, camera);
	camera->addAnimator(anim);
	anim->drop();

	ICursorControl* cursor_control = device->getCursorControl();
	cursor_control->setVisible(false);

	const SColor& scolor = SColor(255,120,102,136);

	ISceneCollisionManager* collision_manager = scene_manager->getSceneCollisionManager();

	UserIEventReceiver* i_event_receiver = new UserIEventReceiver();
	device->setEventReceiver(i_event_receiver);

	while (device->run())
	{
		if (device->isWindowActive())
		{
			if (i_event_receiver->IsKeyDown(KEY_ESCAPE))
				break;
			driver->beginScene(true, true, scolor);
			scene_manager->drawAll();

			if (!dlg)
			{
				ISceneNode* selectedSceneNode = collision_manager->getSceneNodeFromCameraBB(camera);
				if (selectedSceneNode)
				{
					if (selectedSceneNode->getType() == ESNT_SPHERE)
					{
						a = randrange(0, 9);
						b = randrange(0, 9);
						swprintf(msg, L"Please enter answer and press 'Enter'\n%d x %d =", a, b);
						dlg = guienv->addMessageBox(L"Warning", msg);
					}
				}
			}
			else
			{
				if (i_event_receiver->IsKeyDown(KEY_RETURN))
				{
					if ((a * b) == i_event_receiver->answer)
					{
						swprintf(check_answer, L"%d\nCorrectly", i_event_receiver->answer);
						i_gui_static_text->setDrawBackground(false);
					}
					else
					{
						swprintf(check_answer, L"%d\nNot correctly\nCorrectly answer is %d", i_event_receiver->answer, (a * b));
						i_gui_static_text->setDrawBackground(true);
						i_gui_static_text->setBackgroundColor(SColor(128,255,0,0));
					}
					i_gui_static_text->setText(check_answer);
					IGUIButton* btn_close = dlg->getCloseButton();
					btn_close->setPressed();
					dlg->remove();
					dlg = 0;
				}
			}
			printf("dialog pointer = %d\n", dlg);
			if (dlg)
				cursor_control->setVisible(true);
			else
				cursor_control->setVisible(false);

			guienv->drawAll();
			driver->endScene();
			device->sleep(10);
		}
		else
			device->yield();
	}
	return device->drop();
}