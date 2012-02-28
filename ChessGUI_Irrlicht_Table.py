'Irrlicht GUI for "Python Chess" project (Copyright (C) 2009 Steve Osborne http://yakinikuman.wordpress.com)'

import os, sys
from pyirrlicht import *
from locale import getdefaultlocale

has_chess_modules = False
try:
	import ChessAI
	from ChessRules import ChessRules
	from ChessBoard import ChessBoard
	from ChessPlayer import ChessPlayer
except:
	print('ERROR load ChessAI module')
else:
	has_chess_modules = True

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

app_name = os.path.basename(sys.argv[0].split('.')[0])

# simple language translator
default_locale = getdefaultlocale()[0]
translation_catalog = 'lang'
if not os.path.isdir(translation_catalog):
	os.mkdir(translation_catalog)
translation_catalog += '//'# only for python 2.4.4 version and isdir function
translation_file_name = translation_catalog + app_name + '_' + default_locale + '.lng'
if not os.path.exists(translation_file_name):
	default_locale = 'en_US'
	translation_file_name = translation_catalog + app_name + '_' + default_locale + '.lng'
if not os.path.exists(translation_file_name):
	f = open(translation_file_name, 'w')
	f.close()
translation_file = open(translation_file_name, 'r+')
translations = {}
for line in translation_file.readlines():
	if len(line.strip()) > 2 and line.find('='):
		key, value = line.split('=', 1)
		translations[key.strip()] = value.strip()
def _(source = ''):
	if not source in translations:
		translation_file.write('\n' + source + ' = ' + source + '\n')
		translation_file.flush()
		translations[source] = source
	try:
		return unicode(translations[source], 'cp1251')
	except:
		return translations[source]

class UserIEventReceiver(IEventReceiver):
	game = None
	current_command = -1
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	def OnEvent(self, evt):
		event = SEvent(evt)
		if self.game.help_dialog:
			try:
				self.game.help_dialog.getID()
			except:
				self.game.help_dialog = None
		if event.EventType is EET_KEY_INPUT_EVENT:
			pressed_down = event.KeyInput.PressedDown
			self.KeyIsDown[event.KeyInput.Key] = pressed_down
			current_character = str(event.KeyInput.Char)
			if '12345678abcdefghABCDEFGH'.find(current_character) > -1 and pressed_down:
				self.game.command += current_character
				if not self.game.commands.getItemCount():
					self.current_command = self.game.commands.addItem(self.game.command)
				if self.current_command > -1:
					self.game.commands.setItem(self.current_command, self.game.command, 0)
			elif event.KeyInput.Key == KEY_RETURN and not pressed_down and not self.game.help_dialog:
				if self.game.command.lower() == 'exit':
					self.KeyIsDown[KEY_ESCAPE] = True
				else:
					self.game.make_step()
					self.current_command = self.game.commands.addItem('')
					self.game.commands.setSelected(self.current_command)
				self.game.command = ''
			elif event.KeyInput.Key == KEY_F1:
				self.help()
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode]
	def help(self):
		if not self.game.help_dialog:
			self.game.help_dialog = self.game.gui_environment.addMessageBox(_('Help'), _('Copyright (C) 2009 Steve Osborne') + '\n' + _('F1 - help; ESC - exit') + '\n' + _('Please enter movie and press "Enter"'))

class game:
	def __init__(self, *args, **kwargs):
		self.checkmate = False
		self.command = ''
		self.current_player = 0
		self.figures = {'wP':chr(14), 'wR':chr(15), 'wT':chr(16), 'wB':chr(17), 'wQ':chr(18), 'wK':chr(19), 'bP':chr(20), 'bR':chr(21), 'bT':chr(22), 'bB':chr(23), 'bQ':chr(24), 'bK':chr(25)}
		self.board = None
		self.rules = None
		self.players = [0,0]
		self.AIvsAI = False
		self.AIpause = False
		self.AIpauseSeconds = 1
		if has_chess_modules:
			self.rules = ChessRules()
			self.board = ChessBoard(0)
			player1Name = 'Kasparov'
			player1Type = 'human'
			player1Color = 'white'
			player2Name = 'Light Blue'
			player2Type = 'randomAI'
			player2Color = 'black'		
			if player1Type == 'human':
				self.players[0] = ChessPlayer(player1Name,player1Color)
			elif player1Type == 'randomAI':
				self.players[0] = ChessAI.ChessAI_random(player1Name,player1Color)
			elif player1Type == 'defenseAI':
				self.players[0] = ChessAI.ChessAI_defense(player1Name,player1Color)
			elif player1Type == 'offenseAI':
				self.players[0] = ChessAI.ChessAI_offense(player1Name,player1Color)
			if player2Type == 'human':
				self.players[1] = ChessPlayer(player2Name,player2Color)
			elif player2Type == 'randomAI':
				self.players[1] = ChessAI.ChessAI_random(player2Name,player2Color)
			elif player2Type == 'defenseAI':
				self.players[1] = ChessAI.ChessAI_defense(player2Name,player2Color)
			elif player2Type == 'offenseAI':
				self.players[1] = ChessAI.ChessAI_offense(player2Name,player2Color)
			if 'AI' in self.players[0].GetType() and 'AI' in self.players[1].GetType():
				self.AIvsAI = True
		self.font_size_text = 20
		self.font_file_text = os.environ['SYSTEMROOT']+'/Fonts/arial.ttf'
		self.font_size_chess = 40
		self.font_file_chess = 'chess.ttf'
		#~ self.font_file_chess = 'cheq_tt.ttf'
		self.black = SColor(255, 0, 0, 0)
		self.white = SColor(255, 255, 255, 255)
		self.back_color = SColor(255,150,150,150)
		self.board_color = SColor(255, 255, 255, 0)
		self.help_dialog = None
		self.video_driver = None
		self.scene_manager = None
		self.gui_environment = None
		self.font_text = None
		self.font_chess = None
		self.skin = None
		p = SIrrlichtCreationParameters()
		p.DriverType = driverType
		p.WindowSize = dimension2du(640, 480)
		p.AntiAlias = True
		p.WithAlphaChannel = True
		self.device = createDeviceEx(p)
		if self.device:
			self.device.setWindowCaption('Python Chess written by Steve Osborne, Irrlicht GUI by Maxim Kolosov')
			self.device.setResizable(True)
			self.video_driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.gui_environment = self.device.getGUIEnvironment()
			# icon
			if is_frozen():
				self.video_driver.SetIcon(101)
			else:
				self.video_driver.SetIcon()
			# skin
			self.skin = self.gui_environment.getSkin()
			self.skin.setColor(EGDC_HIGH_LIGHT_TEXT, SColor(255, 0, 0, 0))
			self.skin.setColor(EGDC_GRAY_TEXT, SColor(255, 0, 255, 0))
			# chess font
			self.font_chess = CGUITTFont(self.gui_environment, self.font_file_chess, self.font_size_chess)
			if self.font_chess:
				self.skin.setFont(self.font_chess)
			else:
				self.font_chess = self.gui_environment.getBuiltInFont()
				print('++++ ERROR chess font not created !!!')
			# text font
			self.font_text = CGUITTFont(self.gui_environment, self.font_file_text, self.font_size_text)
			if self.font_text:
				self.skin.setFont(self.font_text, EGDF_BUTTON)
				self.skin.setFont(self.font_text, EGDF_WINDOW)
				self.skin.setFont(self.font_text, EGDF_MENU)
				self.skin.setFont(self.font_text, EGDF_TOOLTIP)
			# create board
			#~ self.dlg_tbl = self.gui_environment.addWindow(recti(0,0,800,600), True, _('board'))
			self.back_table = self.gui_environment.addTable(recti(0,0,800,600))#, self.dlg_tbl, drawBackground = True)
			#~ self.back_table.setDrawFlags(EGTDF_ROWS | EGTDF_COLUMNS)
			self.table = self.gui_environment.addTable(recti(0,0,800,600))#, self.dlg_tbl)
			self.table.setResizableColumns(False)
			self.table.setDrawFlags(EGUI_TABLE_DRAW_FLAGS)
			#~ self.black_table = self.gui_environment.addTable(recti(0,0,800,600), self.dlg_tbl)
			#~ self.black_table.setResizableColumns(False)
			#~ self.black_table.setDrawFlags(EGUI_TABLE_DRAW_FLAGS)
			self.fill_table()
			# create dialog list commands
			self.dlg_cmd = self.gui_environment.addWindow(recti(0,0,150,400))#, True, _('Steps history'))
			self.commands = self.gui_environment.addListBox(recti(0,20,150,300), self.dlg_cmd)
			self.commands.setAutoScrollEnabled(True)
			self.dlg_cmd.setRelativePosition(position2di(500,0))
		else:
			print('ERROR createDevice')

	def fill_table(self):
		blue = SColor(255, 0, 0, 255)
		green = SColor(255, 0, 255, 0)
		index = 0
		columns = '*abcdefgh*'
		for column in columns:
			self.table.addColumn('', index)
			self.table.setColumnWidth(index, 50)
			self.back_table.addColumn(column, index)
			self.back_table.setColumnWidth(index, 50)
			index = index + 1
		index = 0
		rows = '87654321'
		for row in rows:
			self.table.addRow(index)
			self.back_table.addRow(index)
			self.back_table.setCellText(index, 0, row, green)
			self.back_table.setCellText(index, 9, row, green)
			#~ for column in range(self.table.getColumnCount()):
				#~ self.table.setCellColor(index, column, self.white)
			index = index + 1
		self.back_table.addRow(index)#this is bottom row for captions
		first = True
		w, b = chr(1), chr(3)
		for row in range(self.back_table.getRowCount()):
			for column in range(1,self.back_table.getColumnCount()-1):
				if first:
					self.back_table.setCellText(row, column, '')
				else:
					self.back_table.setCellText(row, column, b)
				self.back_table.setCellColor(row, column, blue)
				first = not first
			first = not first
		index = 0
		for column in columns:
			self.back_table.setCellText(8, index, column, green)
			index = index + 1
		if not has_chess_modules:
			for i in range(1,9):
				self.table.setCellText(1, i, self.figures['bP'])
				self.table.setCellText(6, i, self.figures['wP'], self.white)
			self.table.setCellText(0, 1, self.figures['bR'])
			self.table.setCellText(0, 2, self.figures['bT'])
			self.table.setCellText(0, 3, self.figures['bB'])
			self.table.setCellText(0, 4, self.figures['bQ'])
			self.table.setCellText(0, 5, self.figures['bK'])
			self.table.setCellText(0, 6, self.figures['bB'])
			self.table.setCellText(0, 7, self.figures['bT'])
			self.table.setCellText(0, 8, self.figures['bR'])
			self.table.setCellText(7, 1, self.figures['wR'], self.white)
			self.table.setCellText(7, 2, self.figures['wT'], self.white)
			self.table.setCellText(7, 3, self.figures['wB'], self.white)
			self.table.setCellText(7, 4, self.figures['wQ'], self.white)
			self.table.setCellText(7, 5, self.figures['wK'], self.white)
			self.table.setCellText(7, 6, self.figures['wB'], self.white)
			self.table.setCellText(7, 7, self.figures['wT'], self.white)
			self.table.setCellText(7, 8, self.figures['wR'], self.white)
		else:
			self.redraw_board()

	def redraw_board(self):
		board_state = self.board.GetState()
		for row in range(self.table.getRowCount()):
			for column in range(1,self.table.getColumnCount()-1):
				figure = str(board_state[row][column-1])
				#~ print('=== figure', figure)
				if figure[0] in ('b', 'w'):
					if figure[0] == 'w':
						self.table.setCellText(row, column, self.figures[figure], self.white)
					else:
						self.table.setCellText(row, column, self.figures[figure])
				else:
					self.table.setCellText(row, column, '')
		#~ self.gui_environment.setFocus(self.dlg_cmd)
		#~ print "      a      b      c      d      e      f      g      h"
		#~ print "  ----------------------------------------"
		#~ for r in range(8):
			#~ print "r"+str(r)+"|",
			#~ for c in range(8):
				#~ if board_state[r][c] != 'e':
					#~ print  str(board_state[r][c]), "|",
				#~ else:
					#~ print "   |",
				#~ if c == 7:
					#~ print #to get a new line
			#~ print "  ----------------------------------------"

	def translate_step(self, step):
		s = step.replace('8', '0').replace('7', '1').replace('6', '2').replace('5', '3').replace('3', '5').replace('2', '6').replace('1', '7').lower().replace('a', '0').replace('b', '1').replace('c', '2').replace('d', '3').replace('e', '4').replace('f', '5').replace('g', '6').replace('h', '7')
		return (int(s[1]), int(s[0])), (int(s[3]), int(s[2]))

	def make_step(self):
		if len(self.command) < 4 and self.players[self.current_player].GetType() != 'AI':
			print('=== WRONG command %s' % self.command)
			return
		board_state = self.board.GetState()
		if self.rules.IsCheckmate(board_state, self.players[self.current_player].color):
			self.checkmate = True
			print('=== MATE')
			return
		if self.rules.IsInCheck(board_state, self.players[self.current_player].color):
			print('=== Warning... %s is in check!' % self.players[self.current_player].color)
		step = ((1,0), (2,0))
		if self.players[self.current_player].GetType() == 'AI':
			step = self.players[self.current_player].GetMove(self.board.GetState(), self.players[self.current_player].color) 
		else:
			step = self.translate_step(self.command)
		#~ if self.rules.IsClearPath(self.board.GetState(), *step):
		print('=== %s' % self.board.MovePiece(step))
		self.current_player = int(not self.current_player)
		if self.AIvsAI and self.AIpause:
			self.device.sleep(self.AIpauseSeconds)
		self.redraw_board()
		#~ else:
			#~ print('STEP %s is wrong' % self.command)
		if self.players[self.current_player].GetType() == 'AI':
			self.make_step()

	def run(self):
		i_event_receiver = UserIEventReceiver()
		i_event_receiver.game = self
		self.device.setEventReceiver(i_event_receiver)
		while self.device.run():
			if self.device.isWindowActive():
				if i_event_receiver.IsKeyDown(KEY_ESCAPE) and not self.help_dialog:
					break
				if self.video_driver.beginScene(True, True, self.back_color):
					#~ self.screen_size = self.video_driver.getScreenSize()
					#~ if not self.checkmate:
						#~ self.redraw_board()
					#~ self.font.draw(self.command, recti(0, 0, 100, self.font_size_text), self.board_color)
					self.gui_environment.drawAll()
					self.video_driver.endScene()
				self.device.sleep(10)
			else:
				self.device._yield()
		self.device.closeDevice()
		self.device.drop()

def main():
	g = game()
	if g.device:
		g.run()

if __name__ == "__main__":
	main()