'Setup video settings with venster GUI'

has_venster = True
try:
	from venster.wtl import *
	from venster.dialog import *
except:
	has_venster = False
	print('VENSTER MODULE IS NOT ACCESSIBLE')

if has_venster:
	class ChoiseDialog(Dialog):
		driver_type = 0
		full_screen = False
		stencil_buffer = False
		vsync = False
		anti_alias = False
		with_alpha_channel = False
		double_buffer = False
		IDC_EDT_NULL = 1000
		IDC_EDT_SOFTWARE = 1001
		IDC_EDT_BURNINGSVIDEO = 1002
		IDC_EDT_DIRECT3D8 = 1003
		IDC_EDT_DIRECT3D9 = 1004
		IDC_EDT_OPENGL = 1005
		IDC_FULL_SCREEN = 1010
		IDC_STENCIL_BUFFER = 1011
		IDC_VSYNC = 1012
		IDC_ANTI_ALIAS = 1013
		IDC_WITH_ALPHA_CHANNEL = 1014
		IDC_DOUBLE_BUFFER = 1015

		items = [
			#~ ComboBox(orStyle=CBS_DROPDOWNLIST, rcPos=RECT(10, 0, 220, 12), id=IDC_EDIT_EVAL),
			GroupBox(title = 'Video drivers:', rcPos = RECT(5, 0, 100, 90)),
			RadioButton(id = IDC_EDT_NULL, title = 'NULL', rcPos = RECT(10, 10, 90, 10)),
			RadioButton(id = IDC_EDT_SOFTWARE, title = 'SOFTWARE', rcPos = RECT(10, 23, 90, 10)),
			RadioButton(id = IDC_EDT_BURNINGSVIDEO, title = 'BURNINGSVIDEO', rcPos = RECT(10, 36, 90, 10)),
			RadioButton(id = IDC_EDT_DIRECT3D8, title = 'DIRECT3D8', rcPos = RECT(10, 49, 90, 10)),
			RadioButton(id = IDC_EDT_DIRECT3D9, title = 'DIRECT3D9', rcPos = RECT(10, 62, 90, 10)),
			RadioButton(id = IDC_EDT_OPENGL, title = 'OPENGL', rcPos = RECT(10, 75, 90, 10)),
			CheckBox(id = IDC_FULL_SCREEN, title = 'Full Screen', rcPos = RECT(110, 5, 100, 10)),
			CheckBox(id = IDC_STENCIL_BUFFER, title = 'Stencil Buffer', rcPos = RECT(110, 20, 100, 10)),
			CheckBox(id = IDC_VSYNC, title = 'Vsync', rcPos = RECT(110, 35, 100, 10)),
			CheckBox(id = IDC_ANTI_ALIAS, title = 'Anti Alias', rcPos = RECT(110, 50, 100, 10)),
			CheckBox(id = IDC_WITH_ALPHA_CHANNEL, title = 'With Alpha Channel', rcPos = RECT(110, 65, 100, 10)),
			CheckBox(id = IDC_DOUBLE_BUFFER, title = 'Double Buffer', rcPos = RECT(110, 80, 100, 10)),
			DefPushButton(title = 'OK', id = IDOK, rcPos = RECT(left = 30, top = 100, right = 50, bottom = 15)),
			PushButton(title = 'Cancel', id = IDCANCEL, rcPos = RECT(left = 130, top = 100, right = 50, bottom = 15)),
			]

		_dialog_template_ = DialogTemplate(
			title = 'Select video settings',
			style = DS_MODALFRAME|WS_POPUP|WS_CAPTION|WS_SYSMENU|DS_SETFONT,
			rcPos = RECT(left = 0, top = 0, right = 210, bottom = 120),
			items = items
			)

		def set_driver_type(self, ctrl_id):
			self.driver_type = ctrl_id - 1000
			for cid, ctrl in self.ctrl_edt.iteritems():
				if cid == ctrl_id:
					ctrl.SetCheck(BST_CHECKED)
				else:
					ctrl.SetCheck(BST_UNCHECKED)

		def event_edt_null(self, event):
			self.set_driver_type(self.IDC_EDT_NULL)
		event_edt_null = cmd_handler(IDC_EDT_NULL)(event_edt_null)
		def event_edt_software(self, event):
			self.set_driver_type(self.IDC_EDT_SOFTWARE)
		event_edt_software = cmd_handler(IDC_EDT_SOFTWARE)(event_edt_software)
		def event_edt_burningsvideo(self, event):
			self.set_driver_type(self.IDC_EDT_BURNINGSVIDEO)
		event_edt_burningsvideo = cmd_handler(IDC_EDT_BURNINGSVIDEO)(event_edt_burningsvideo)
		def event_edt_direct3d8(self, event):
			self.set_driver_type(self.IDC_EDT_DIRECT3D8)
		event_edt_direct3d8 = cmd_handler(IDC_EDT_DIRECT3D8)(event_edt_direct3d8)
		def event_edt_direct3d9(self, event):
			self.set_driver_type(self.IDC_EDT_DIRECT3D9)
		event_edt_direct3d9 = cmd_handler(IDC_EDT_DIRECT3D9)(event_edt_direct3d9)
		def event_edt_opengl(self, event):
			self.set_driver_type(self.IDC_EDT_OPENGL)
		event_edt_opengl = cmd_handler(IDC_EDT_OPENGL)(event_edt_opengl)

		def event_full_screen(self, event):
			self.full_screen = not self.ctrl_FULL_SCREEN.GetCheck()
			self.ctrl_FULL_SCREEN.SetCheck(int(self.full_screen))
		event_full_screen = cmd_handler(IDC_FULL_SCREEN)(event_full_screen)

		def event_stencil_buffer(self, event):
			self.stencil_buffer = not self.ctrl_STENCIL_BUFFER.GetCheck()
			self.ctrl_STENCIL_BUFFER.SetCheck(int(self.stencil_buffer))
		event_stencil_buffer = cmd_handler(IDC_STENCIL_BUFFER)(event_stencil_buffer)

		def event_vsync(self, event):
			self.vsync = not self.ctrl_VSYNC.GetCheck()
			self.ctrl_VSYNC.SetCheck(int(self.vsync))
		event_vsync = cmd_handler(IDC_VSYNC)(event_vsync)

		def event_anti_alias(self, event):
			self.anti_alias = not self.ctrl_ANTI_ALIAS.GetCheck()
			self.ctrl_ANTI_ALIAS.SetCheck(int(self.anti_alias))
		event_anti_alias = cmd_handler(IDC_ANTI_ALIAS)(event_anti_alias)

		def event_with_alpha_channel(self, event):
			self.with_alpha_channel = not self.ctrl_WITH_ALPHA_CHANNEL.GetCheck()
			self.ctrl_WITH_ALPHA_CHANNEL.SetCheck(int(self.with_alpha_channel))
		event_with_alpha_channel = cmd_handler(IDC_WITH_ALPHA_CHANNEL)(event_with_alpha_channel)

		def event_double_buffer(self, event):
			self.double_buffer = not self.ctrl_DOUBLE_BUFFER.GetCheck()
			self.ctrl_DOUBLE_BUFFER.SetCheck(int(self.double_buffer))
		event_double_buffer = cmd_handler(IDC_DOUBLE_BUFFER)(event_double_buffer)

		def OnInitDialog(self, event):
			Dialog.OnInitDialog(self, event)
			self.ctrl_edt = {
				self.IDC_EDT_NULL:self.GetDlgItem(self.IDC_EDT_NULL, comctl.RadioButton),
				self.IDC_EDT_SOFTWARE:self.GetDlgItem(self.IDC_EDT_SOFTWARE, comctl.RadioButton),
				self.IDC_EDT_BURNINGSVIDEO:self.GetDlgItem(self.IDC_EDT_BURNINGSVIDEO, comctl.RadioButton),
				self.IDC_EDT_DIRECT3D8:self.GetDlgItem(self.IDC_EDT_DIRECT3D8, comctl.RadioButton),
				self.IDC_EDT_DIRECT3D9:self.GetDlgItem(self.IDC_EDT_DIRECT3D9, comctl.RadioButton),
				self.IDC_EDT_OPENGL:self.GetDlgItem(self.IDC_EDT_OPENGL, comctl.RadioButton),
			}
			default_id_driver_type = self.driver_type + 1000
			self.set_driver_type(default_id_driver_type)
			self.ctrl_edt[default_id_driver_type].SetFocus()

			self.ctrl_FULL_SCREEN = self.GetDlgItem(self.IDC_FULL_SCREEN, comctl.CheckBox)
			self.ctrl_FULL_SCREEN.SetCheck(int(self.full_screen))

			self.ctrl_STENCIL_BUFFER = self.GetDlgItem(self.IDC_STENCIL_BUFFER, comctl.CheckBox)
			self.ctrl_STENCIL_BUFFER.SetCheck(int(self.stencil_buffer))

			self.ctrl_VSYNC = self.GetDlgItem(self.IDC_VSYNC, comctl.CheckBox)
			self.ctrl_VSYNC.SetCheck(int(self.vsync))

			self.ctrl_ANTI_ALIAS = self.GetDlgItem(self.IDC_ANTI_ALIAS, comctl.CheckBox)
			self.ctrl_ANTI_ALIAS.SetCheck(int(self.anti_alias))

			self.ctrl_WITH_ALPHA_CHANNEL = self.GetDlgItem(self.IDC_WITH_ALPHA_CHANNEL, comctl.CheckBox)
			self.ctrl_WITH_ALPHA_CHANNEL.SetCheck(int(self.with_alpha_channel))

			self.ctrl_DOUBLE_BUFFER = self.GetDlgItem(self.IDC_DOUBLE_BUFFER, comctl.CheckBox)
			self.ctrl_DOUBLE_BUFFER.SetCheck(int(self.double_buffer))

if __name__ == '__main__':
	if has_venster:
		dialog = ChoiseDialog()
		dialogResult = dialog.DoModal()
		if dialogResult == IDOK:
			print('Pressed OK')
		elif dialogResult == IDCANCEL:
			print('Pressed Cancel')
		else:
			print('Unknown dialog return value %d' % dialogResult)
