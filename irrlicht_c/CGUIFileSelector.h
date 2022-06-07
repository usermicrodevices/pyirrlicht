// http://irrlicht.sourceforge.net/forum/viewtopic.php?f=9&t=30241
// author JP (http://irrlicht.sourceforge.net/forum/memberlist.php?mode=viewprofile&u=2783)
// some changes from Maxim Kolosov in April 2012

#ifndef INC_CGUIFILESELECTOR_H
#define INC_CGUIFILESELECTOR_H

#include <irrlicht.h>
#ifdef _IRR_WINDOWS_
   #include <windows.h>
   #include <iostream>
#endif

using namespace irr;
using namespace gui;

/** Enum to specify the usage of the instance of the class */   
enum E_FILESELECTOR_TYPE {
  EFST_OPEN_DIALOG, //<! For opening files
  EFST_SAVE_DIALOG, //<! For saving files
  EFST_NUM_TYPES    //<! Not used, just specifies how many possible types there are
};

/** Class for opening/saving files. */
class CGUIFileSelector : public IGUIFileOpenDialog
{
public:
	/**
	\brief Constructor
	\param title - The title of the dialog
	\pararm environment - The GUI environment to be used
	\param parent - The parent of the dialog
	\param id - The ID of the dialog
	\param type - The type of dialog
	*/
	CGUIFileSelector(const wchar_t* title, IGUIEnvironment* environment, IGUIElement* parent, s32 id, E_FILESELECTOR_TYPE type);
	CGUIFileSelector(const wchar_t* title, IGUIEnvironment* environment, IGUIElement* parent, s32 id, rect<s32>* rectangle = 0, E_FILESELECTOR_TYPE type = EFST_OPEN_DIALOG);
	void init(const wchar_t* title);

	/**
	\brief Destructor
	*/
	virtual ~CGUIFileSelector();
	/**
	\brief Returns the filename of the selected file. Returns NULL, if no file was selected.
	\return a const wchar_t*
	*/
	virtual const wchar_t* getFileName() const;
	//! Returns the directory of the selected file. Returns NULL, if no directory was selected.
	virtual const io::path& getDirectoryName();
	/**
	\brief called if an event happened.
	\param even - the event that happened
	\return a bool
	*/
	virtual bool OnEvent(const SEvent& event);
	/**
	\brief Render function
	*/
	virtual void draw();
	/**
	\brief Returns the current file filter selected or "All Files" if no filter is applied
	\return a stringw
	*/
	inline core::stringw getFileFilter() const
	{
	if (FilterComboBox->getSelected() >= (s32)FileFilters.size()) return core::stringw("All Files");
	else return FileFilters[FilterComboBox->getSelected()].FileExtension;
	}

	/**
	\brief Returns the type of the dialog
	\return a E_FILESELECTOR_TYPE
	*/
	inline E_FILESELECTOR_TYPE getDialogType() { return DialogType; }

	/**
	\brief Add a file filter
	\param name - The description of the file type
	\param ext - The file's extension
	\param texture - The icon texture
	*/
	void addFileFilter(wchar_t* name, wchar_t* ext, video::ITexture* texture);

	/**
	\brief Set an icon to use to display unknown files
	\param texture - the 16x16 icon to use
	*/
	inline void setCustomFileIcon(video::ITexture* texture) {
	if (texture) FileIconIdx = addIcon(texture);
	else FileIconIdx = -1;
	fillListBox();
	}
	/**
	\brief Set an icon to use to display directories
	\param texture - the 16x16 icon to use
	*/
	inline void setCustomDirectoryIcon(video::ITexture* texture) {
	if (texture) DirectoryIconIdx = addIcon(texture);
	else DirectoryIconIdx = -1;
	fillListBox();
	}

	/**
	\brief Sets whether directories can be chosen as the 'file' to open
	\param choosable - Whether the directory can be chosen
	*/
	inline void setDirectoryChoosable(bool choosable) { IsDirectoryChoosable = choosable; }

protected:

	/**
	\brief Returns true if the file extension is one of the registered filters
	\param s - the string to be checked
	\return a bool
	*/
	bool matchesFileFilter(core::stringw s);
	/**
	\brief Returns true if the file extension matches the specified filter
	\param s - the string to be checked
	\param f - the filter to check for
	\return a bool
	*/
	bool matchesFileFilter(core::stringw s, core::stringw f);

	/**
	\brief Fills the listbox with files.
	*/
	void fillListBox();

	/**
	\brief Sends the event that the file has been selected.
	*/
	void sendSelectedEvent();

	/**
	\brief Sends the event that the file choose process has been canceld
	*/
	void sendCancelEvent();

	u32 addIcon(video::ITexture* texture);

	/** Struct to describe file filters to use when displaying files in directories */
	struct SFileFilter
	{
		/*
		\brief Constructor
		\param name - The name/description of the filter
		\param filter - The file extension required
		\param texture - The texture to use as an icon for the file type
		*/
		SFileFilter(wchar_t* name, wchar_t* filter, video::ITexture* texture)
		{
			FilterName = name;
			FileExtension = filter;
			FileIcon = texture;
			FileIconIdx = 0;
		}
		void operator=(const SFileFilter& other)
		{
			FilterName = other.FilterName;
			FileExtension = other.FileExtension;
			FileIcon = other.FileIcon;
			FileIconIdx = other.FileIconIdx;
		}
		core::stringw FilterName;
		core::stringw FileExtension;     
		video::ITexture* FileIcon;
		u32 FileIconIdx;
	};

	core::position2d<s32> DragStart;
	bool Dragging;
	bool IsDirectoryChoosable;
	s32 FileIconIdx;
	s32 DirectoryIconIdx;
	IGUIButton* CloseButton;
	IGUIButton* OKButton;
	IGUIButton* CancelButton;
	IGUIEditBox* FileNameText;
	IGUIListBox* FileBox;
	IGUIComboBox* DriveBox;
	IGUIComboBox* FilterComboBox;
	IGUIElement* EventParent;
	IGUISpriteBank* SpriteBank;
	io::IFileSystem* FileSystem;
	io::IFileList* FileList;
	core::array<SFileFilter> FileFilters;
	E_FILESELECTOR_TYPE DialogType;
	core::stringc prev_working_dir;
	io::path FileDirectory;
	static s32 numFileSelectors;
};

//================================

const s32 FOD_WIDTH = 350;
const s32 FOD_HEIGHT = 265;

s32 CGUIFileSelector::numFileSelectors = 0;

const wchar_t* returnMultiByte_FromString(const char* src_buf)
{
	wchar_t* dst_buf = 0;
	size_t src_size = strlen(src_buf) + 1;
	if (src_size > 1)
	{
		dst_buf = new wchar_t[src_size * sizeof(wchar_t)];
#ifdef _MSC_VER
		size_t NumOfCharConverted;
		errno_t res = mbstowcs_s(&NumOfCharConverted, dst_buf, src_size, src_buf, _TRUNCATE);
#else
		//size_t res = mbstowcs(dst_buf, src_buf, MB_CUR_MAX);
		mbstowcs(dst_buf, src_buf, MB_CUR_MAX);
#endif
	}
	return dst_buf;
}

//! constructor
CGUIFileSelector::CGUIFileSelector(const wchar_t* title, IGUIEnvironment* environment, IGUIElement* parent, s32 id, E_FILESELECTOR_TYPE type)
: IGUIFileOpenDialog(environment, parent, id,
core::rect<s32>((parent->getAbsolutePosition().getWidth()-FOD_WIDTH)/2,
(parent->getAbsolutePosition().getHeight()-FOD_HEIGHT)/2,
(parent->getAbsolutePosition().getWidth()-FOD_WIDTH)/2+FOD_WIDTH,
(parent->getAbsolutePosition().getHeight()-FOD_HEIGHT)/2+FOD_HEIGHT)),
Dragging(false), FileNameText(0), FileList(0), DialogType(type)
{init(title);}

CGUIFileSelector::CGUIFileSelector(const wchar_t* title, IGUIEnvironment* environment, IGUIElement* parent, s32 id, rect<s32>* rectangle, E_FILESELECTOR_TYPE type)
: IGUIFileOpenDialog(environment, parent, id, *rectangle),
Dragging(false), FileNameText(0), FileList(0), DialogType(type)
{init(title);};

void CGUIFileSelector::init(const wchar_t* title)
{
#ifdef _DEBUG
	IGUIElement::setDebugName("CGUIFileSelector");
#endif

	Text = core::stringw(title);
	IsDirectoryChoosable = false;

	IGUISkin* skin = Environment->getSkin();
	IGUISpriteBank* sprites = 0;
	video::SColor color(255,255,255,255);
	if (skin)
	{
		sprites = skin->getSpriteBank();
		color = skin->getColor(EGDC_WINDOW_SYMBOL);
	}

	s32 buttonw = Environment->getSkin()->getSize(EGDS_WINDOW_BUTTON_WIDTH);
	s32 posx = RelativeRect.getWidth() - buttonw - 4;

	CloseButton = Environment->addButton(core::rect<s32>(posx, 3, posx + buttonw, 3 + buttonw), this, -1, L"", L"Close");
	CloseButton->setSubElement(true);
	if (sprites)
	{
		CloseButton->setSpriteBank(sprites);
		CloseButton->setSprite(EGBS_BUTTON_UP, skin->getIcon(EGDI_WINDOW_CLOSE), color);
		CloseButton->setSprite(EGBS_BUTTON_DOWN, skin->getIcon(EGDI_WINDOW_CLOSE), color);
	}
	CloseButton->setAlignment(EGUIA_LOWERRIGHT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	CloseButton->grab();

	OKButton = Environment->addButton(core::rect<s32>(RelativeRect.getWidth()-80, 30, RelativeRect.getWidth()-10, 50), this, -1, (DialogType==EFST_OPEN_DIALOG?L"Open":L"Save"));
	OKButton->setSubElement(true);
	OKButton->setAlignment(EGUIA_LOWERRIGHT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	OKButton->grab();

	CancelButton = Environment->addButton(core::rect<s32>(RelativeRect.getWidth()-80, 55, RelativeRect.getWidth()-10, 75), this, -1, skin ? skin->getDefaultText(EGDT_MSG_BOX_CANCEL) : L"Cancel");
	CancelButton->setSubElement(true);
	CancelButton->setAlignment(EGUIA_LOWERRIGHT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	CancelButton->grab();

	FileBox = Environment->addListBox(core::rect<s32>(10, 80, RelativeRect.getWidth()-90, RelativeRect.getHeight()-60), this, -1, true);
	FileBox->setSubElement(true);
	FileBox->setAlignment(EGUIA_UPPERLEFT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_LOWERRIGHT);
	FileBox->grab();

	DriveBox = Environment->addComboBox(core::rect<s32>(10, 55, RelativeRect.getWidth()-90, 75), this, -1);
	DriveBox->setSubElement(true);
	DriveBox->setAlignment(EGUIA_UPPERLEFT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	DriveBox->grab();   

	FileNameText = Environment->addEditBox(0, core::rect<s32>(10, 30, RelativeRect.getWidth()-90, 50), true, this, -1);
	FileNameText->setSubElement(true);
	FileNameText->setAlignment(EGUIA_UPPERLEFT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	FileNameText->setTextAlignment(EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	FileNameText->grab();

	FilterComboBox = Environment->addComboBox(core::rect<s32>(10, RelativeRect.getHeight()-30, RelativeRect.getWidth()-90, RelativeRect.getHeight()-10), this, -1);
	FilterComboBox->setSubElement(true);
	FilterComboBox->setAlignment(EGUIA_UPPERLEFT, EGUIA_LOWERRIGHT, EGUIA_UPPERLEFT, EGUIA_UPPERLEFT);
	FilterComboBox->grab();
	FilterComboBox->addItem(L"All Files");
   
	core::stringc str = "FileSelectorIcons";
	str += numFileSelectors++;
	SpriteBank = Environment->addEmptySpriteBank(str.c_str());
	if (SpriteBank)
	{
		SpriteBank->grab();
		FileBox->setSpriteBank(SpriteBank);
	}
	DirectoryIconIdx = -1;
	FileIconIdx = -1;

	FileSystem = Environment->getFileSystem();
   
	if (FileSystem)
	{
		FileSystem->grab();
		prev_working_dir = FileSystem->getWorkingDirectory();
		//printf("working directory saved: %s\n", prev_working_dir.c_str());
	}

	fillListBox();


#ifdef _IRR_WINDOWS_
	enum { SZ = 1024, GB = 1024*1024*1024 } ;
	char drives[SZ] ;

	if (GetLogicalDriveStrings( SZ, drives ) < SZ)
	{
		char* p = drives;
		while(*p)// two null chars; end of list
		{
			DriveBox->addItem(returnMultiByte_FromString(p));
			while(*p)
				++p ; // get to next null char
			++p ; // and then skip over it
		}
	}
#endif
}

//! destructor
CGUIFileSelector::~CGUIFileSelector() {
   if (CloseButton)
	  CloseButton->drop();

   if (OKButton)
	  OKButton->drop();

   if (CancelButton)
	  CancelButton->drop();

   if (FileBox)
	  FileBox->drop();

   if (FileNameText)
	  FileNameText->drop();

   if (FileSystem)
	  FileSystem->drop();

   if (FileList)
	  FileList->drop();
	  
   if (FilterComboBox)
	   FilterComboBox->drop();
	  
	if (SpriteBank)
		SpriteBank->drop();
	  
}

//! returns the filename of the selected file. Returns NULL, if no file was selected.
const wchar_t* CGUIFileSelector::getFileName() const {
   return FileNameText->getText();
}

const io::path& CGUIFileSelector::getDirectoryName() {
   FileSystem->flattenFilename ( FileDirectory );
   return FileDirectory;
}

//! called if an event happened.
bool CGUIFileSelector::OnEvent(const SEvent& event)
{
	s32 selected = 0;
	switch((int)event.EventType) {
		case EET_KEY_INPUT_EVENT:
			switch (event.KeyInput.Key) {
				case KEY_RETURN:
					if (FileSystem) {
						FileSystem->changeWorkingDirectoryTo(core::stringc(FileNameText->getText()).c_str());
						fillListBox();
						FileNameText->setText(core::stringw(FileSystem->getWorkingDirectory()).c_str());
					}
					return true;
				default: return false;
			}
			break;
		case EET_GUI_EVENT:
			switch(event.GUIEvent.EventType) {
				case EGET_COMBO_BOX_CHANGED:
					if (event.GUIEvent.Caller == FilterComboBox) {
						fillListBox();
					} else {  // change drive
						if (FileSystem) {      
							FileSystem->changeWorkingDirectoryTo(core::stringc(DriveBox->getText()).c_str());
							fillListBox();
						}
					}
					break;
				default: break;
			}
			break;
		//case EGET_ELEMENT_FOCUS_LOST:
			//Dragging = false;
			//break;
		case EGET_BUTTON_CLICKED:
			if (event.GUIEvent.Caller == CloseButton ||
				event.GUIEvent.Caller == CancelButton) {
					if (FileSystem) {
				FileSystem->changeWorkingDirectoryTo(prev_working_dir.c_str());
				//printf("working directory reset to: %s\n", prev_working_dir.c_str());
				}
				sendCancelEvent();
				remove();
				return true;
			}
			else
			if (event.GUIEvent.Caller == OKButton && (IsDirectoryChoosable || matchesFileFilter(FileNameText->getText()))) {
				if (FileSystem) {
				  FileSystem->changeWorkingDirectoryTo(prev_working_dir.c_str());
				  //printf("working directory reset to: %s\n", prev_working_dir.c_str());
				}
				sendSelectedEvent();
				remove();
				return true;
			}
			break;
		case EGET_LISTBOX_CHANGED:
			selected = FileBox->getSelected();
			if (FileList && FileSystem)
			{
				core::stringw strw;
				strw = FileSystem->getWorkingDirectory();
				if (strw[strw.size()-1] != '\\')
					strw += "\\";
				strw += FileBox->getListItem(selected);
				FileNameText->setText(strw.c_str());
			}
			break;
		case EGET_LISTBOX_SELECTED_AGAIN:
			selected = FileBox->getSelected();
			if (FileList && FileSystem) {
				if (FileList->isDirectory(selected)) {
					FileSystem->changeWorkingDirectoryTo(FileList->getFileName(selected));
					fillListBox();
					FileNameText->setText(core::stringw(FileSystem->getWorkingDirectory()).c_str());
				}
				else
				{
					core::stringw strw;
					strw = FileSystem->getWorkingDirectory();
					if (strw[strw.size()-1] != '\\')
						strw += "\\";
					strw += FileBox->getListItem(selected);
					FileNameText->setText(strw.c_str());
					return true;
				}
			}
			break;
		case EET_MOUSE_INPUT_EVENT:
			switch(event.MouseInput.Event) {
				case EMIE_LMOUSE_PRESSED_DOWN:
					DragStart.X = event.MouseInput.X;
					DragStart.Y = event.MouseInput.Y;
					Dragging = true;
					Environment->setFocus(this);
					return true;
				case EMIE_LMOUSE_LEFT_UP:
					Dragging = false;
					Environment->removeFocus(this);
					return true;
				case EMIE_MOUSE_MOVED:
					if (Dragging) {
						// gui window should not be dragged outside its parent
						if (Parent){
							if (event.MouseInput.X < Parent->getAbsolutePosition().UpperLeftCorner.X +1 ||
								event.MouseInput.Y < Parent->getAbsolutePosition().UpperLeftCorner.Y +1 ||
								event.MouseInput.X > Parent->getAbsolutePosition().LowerRightCorner.X -1 ||
								event.MouseInput.Y > Parent->getAbsolutePosition().LowerRightCorner.Y -1)
								return true;
						}
						move(core::position2d<s32>(event.MouseInput.X - DragStart.X, event.MouseInput.Y - DragStart.Y));
						DragStart.X = event.MouseInput.X;
						DragStart.Y = event.MouseInput.Y;
						return true;
					}
					break;
				default:
					break;
			}
			break;
		default:
			break;
	}
	return Parent ? Parent->OnEvent(event) : false;
}


//! draws the element and its children
void CGUIFileSelector::draw() {
   if (!IsVisible)
	  return;

   IGUISkin* skin = Environment->getSkin();

   core::rect<s32> rect = AbsoluteRect;

   rect = skin->draw3DWindowBackground(this, true, skin->getColor(EGDC_ACTIVE_BORDER),
	  rect, &AbsoluteClippingRect);

   if (Text.size()) {
	  rect.UpperLeftCorner.X += 2;
	  rect.LowerRightCorner.X -= skin->getSize(EGDS_WINDOW_BUTTON_WIDTH) + 5;

	  IGUIFont* font = skin->getFont(EGDF_WINDOW);
	  if (font)
		 font->draw(Text.c_str(), rect, skin->getColor(EGDC_ACTIVE_CAPTION), false, true,
		 &AbsoluteClippingRect);
   }

   IGUIElement::draw();
}

bool CGUIFileSelector::matchesFileFilter(core::stringw s) {
   if (FileFilters.size() > 1) {
	  s32 selected = FilterComboBox->getSelected();
	  if (selected == 0) {
		 for (u32 i = 0; i < FileFilters.size(); i++) {
			s32 pos = s.findLast('.'); // Find the last '.' so we can check the file extension
			if (FileFilters[i].FileExtension.equals_ignore_case(core::stringw(&s.c_str()[pos+1])))
			   return true;
		 }
		 return false;
	  }
	  selected--;
	  if (selected >= (s32)FileFilters.size()) return true; // 'All Files' selectable
	  else {
		 s32 pos = s.findLast('.'); // Find the last '.' so we can check the file extension
		 return FileFilters[selected].FileExtension.equals_ignore_case(core::stringw(&s.c_str()[pos+1]));
	  }
   }
   if (FilterComboBox->getSelected() >= (s32)FileFilters.size()) return true; // 'All Files' selectable
   else {
	  s32 pos = s.findLast('.'); // Find the last '.' so we can check the file extension
	  return FileFilters[FilterComboBox->getSelected()].FileExtension.equals_ignore_case(core::stringw(&s.c_str()[pos+1]));
   }
}

bool CGUIFileSelector::matchesFileFilter(core::stringw s, core::stringw f) {
  s32 pos = s.findLast('.'); // Find the last '.' so we can check the file extension
  return f.equals_ignore_case(core::stringw(&s.c_str()[pos+1]));
}

//! fills the listbox with files.
void CGUIFileSelector::fillListBox() {
   IGUISkin *skin = Environment->getSkin();

   if (!FileSystem || !FileBox || !skin)
	  return;

   if (FileList)
	  FileList->drop();

   FileBox->clear();

   FileList = FileSystem->createFileList();
   core::stringw s;

   for (u32 i=0; i<FileList->getFileCount(); ++i) {
	  s = FileList->getFileName(i);
	  // We just want a list of directories and those matching the file filter
	  if (FileList->isDirectory(i))
		  if (DirectoryIconIdx != -1) FileBox->addItem(s.c_str(), DirectoryIconIdx);
		  else FileBox->addItem(s.c_str());
	  else if (matchesFileFilter(s))
	  {
		if (FilterComboBox->getSelected() >= (s32)FileFilters.size())
			if (FileIconIdx != -1) {
			  s32 iconIdx = FileIconIdx;
			  for (u32 i = 0 ; i < FileFilters.size() ; i++)
				if (matchesFileFilter(s, FileFilters[i].FileExtension))
				  iconIdx = FileFilters[i].FileIconIdx;
			  FileBox->addItem(s.c_str(), iconIdx);
			} else  FileBox->addItem(s.c_str());
		else FileBox->addItem(s.c_str(), FileFilters[FilterComboBox->getSelected()].FileIconIdx);
	  }

   }

   if (FileNameText) {
	  s = FileSystem->getWorkingDirectory();
	  FileNameText->setText(s.c_str());
   }
}


//! sends the event that the file has been selected.
void CGUIFileSelector::sendSelectedEvent() {
   SEvent event;
   event.EventType = EET_GUI_EVENT;
   event.GUIEvent.Caller = this;
   event.GUIEvent.EventType = EGET_FILE_SELECTED;
   Parent->OnEvent(event);
}

//! sends the event that the file choose process has been canceld
void CGUIFileSelector::sendCancelEvent() {
   SEvent event;
   event.EventType = EET_GUI_EVENT;
   event.GUIEvent.Caller = this;
   event.GUIEvent.EventType = EGET_FILE_CHOOSE_DIALOG_CANCELLED;
   Parent->OnEvent(event);
}

void CGUIFileSelector::addFileFilter(wchar_t* name, wchar_t* ext, video::ITexture* texture) {
  SFileFilter filter(name, ext, texture);

  filter.FileIconIdx = addIcon(texture);

  FileFilters.push_back(filter);

  FilterComboBox->clear();
  core::stringw strw;

  if (FileFilters.size() > 1) {
	 strw = "Supported ";
	 for (u32 i = 0 ; i < FileFilters.size() ; i++) {
	  strw += ".";
	  strw += FileFilters[i].FileExtension;
	  strw += " ";
	 }
	 FilterComboBox->addItem(strw.c_str());
  }

  for (u32 i = 0 ; i < FileFilters.size() ; i++) {
	strw = FileFilters[i].FilterName;
	strw += " (*.";
	strw += FileFilters[i].FileExtension;
	strw += ")";
	FilterComboBox->addItem(strw.c_str());
  }
  FilterComboBox->addItem(L"All Files");

  fillListBox();
}

u32 CGUIFileSelector::addIcon(video::ITexture* texture) {
   if (!SpriteBank || !texture) return 0;
   
   // load and add the texture to the bank     
   SpriteBank->addTexture(texture);
   u32 textureIndex = SpriteBank->getTextureCount() - 1;
   // now lets get the sprite bank's rectangles and add some for our animation
   core::array<core::rect<s32> >& rectangles = SpriteBank->getPositions();
   u32 firstRect = rectangles.size();
   // remember that rectangles are not in pixels, they enclose pixels!
   // to draw a rectangle around the pixel at 0,0, it would rect<s32>(0,0, 1,1)
   rectangles.push_back(core::rect<s32>(0,0, 16,16));


   // now we make a sprite..
   SGUISprite sprite;
   sprite.frameTime = 30;
   // add some frames of animation.
   SGUISpriteFrame frame;
   frame.rectNumber = firstRect;
   frame.textureNumber = textureIndex;

   // add this frame
   sprite.Frames.push_back(frame);
   // add the sprite
   //u32 spriteIndex = SpriteBank->getSprites().size();
   SpriteBank->getSprites().push_back(sprite); 

   return textureIndex;
}
//================================

#endif /* INC_CGUIFILESELECTOR_H */
