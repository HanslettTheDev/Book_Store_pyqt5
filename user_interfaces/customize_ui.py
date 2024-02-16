import os
from PySide2 import (QtCore, QtGui)
from PySide2.QtCore import QSize
from PySide2.QtGui import QColor,QIcon
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QPushButton

from user_interfaces.home_window import BaseGuiWindow
from user_interfaces import TempPath

# WINDOW GLOBALS
WINDOW_STATE = 0
WINDOW_TITLE_BAR = True


class UIFunctions(BaseGuiWindow):
	# GLOBAL VARIABLES 
	WINDOW_STATE = 0

	def maximize_window(self):
		global WINDOW_STATE
		status = WINDOW_STATE
		if status == 0:
			self.showFullScreen()
			WINDOW_STATE = 1
			self.ui.centralwidget.setContentsMargins(0,0,0,0)
			self.ui.maximize_button.setToolTip("Restore")
			icon = QIcon()
			icon.addFile(u":/tab_icons/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
			self.ui.maximize_button.setIcon(icon)
		else:
			WINDOW_STATE = 0
			self.showNormal()
			self.ui.centralwidget.setContentsMargins(10,10,10,10)
			self.ui.maximize_button.setToolTip("Maximize")
			icon = QIcon()
			icon.addFile(u":/tab_icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
			self.ui.maximize_button.setIcon(icon)

	def return_status():
		return WINDOW_STATE

	def load_ui_tweaks(self):
		def double_click_maximize_restore(event):
			if event.type() == QtCore.QEvent.MouseButtonDblClick:
				QtCore.QTimer.singleShot(250, lambda: self.functions.maximize_window(self))
		
		if WINDOW_TITLE_BAR:
			self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
			self.ui.window_bar.mouseDoubleClickEvent = double_click_maximize_restore
		
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(17)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 150))
		self.ui.frame_main.setGraphicsEffect(self.shadow)

		self.ui.close_button.clicked.connect(lambda: self.functions.clear_temp_files_before_close(self))
		self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
		self.ui.maximize_button.clicked.connect(lambda: self.functions.maximize_window(self))
		QSizeGrip(self.ui.size_grip)#resize option
	
	def clear_temp_files_before_close(self):
		self.webview.close()
		for file in os.listdir(TempPath):
			if file.startswith("tmp"):
				os.remove(os.path.join(TempPath, file))
		self.logger.info("Temp Files Deleted successfully:")
		self.close()
	
	def sub_content(self, main_content, label):
		self.tab_display.ui.close_button.clicked.connect(lambda: self.close_tab_window())

		self.tab_display.show()
		# set the minimum height for the window
		if self.minimumHeight() < 615:
			self.setMinimumHeight(625)

		self.ui.frame_main.layout().insertWidget(2, self.tab_display)
		# Button active state
		self.functions.check_ischecked
		# Set rootpath per button clicked and rootIndex
		self.tab_display.model.setRootPath(os.path.join(self.dir_path, f"Prog/index/Lib/{main_content}"))
		# set model filter to filter only files to the second list view
		self.tab_display.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
		self.tab_display.ui.dropdown_tree.setRootIndex(
			self.tab_display.model.index(
				os.path.join(self.dir_path, f"Prog/index/Lib/{main_content}")
			)
		)
		
		# Set the label to the button clicked
		if main_content == "Immobilizer\EEPROM Location":
			self.tab_display.ui.groupBox_3.setTitle("IMMO Data") 
			self.tab_display.ui.groupBox_2.setTitle(f"{label}")
		elif main_content == "ECU Datasheet":
			self.tab_display.ui.groupBox_3.setTitle("Manufacturer") 
			self.tab_display.ui.groupBox_2.setTitle(f"{label}")
		elif main_content == "Electronics":
			self.tab_display.ui.groupBox_3.setTitle("Electrical/Electronic Manuals")
			self.tab_display.ui.groupBox_2.setTitle(f"{label}")
		else:
			self.tab_display.ui.groupBox_3.setTitle("Car Model")
			self.tab_display.ui.groupBox_2.setTitle(f"{label}")
	
	def set_window_icons(self, url, button):
		icon = QIcon()
		icon.addFile(url)
		button.setIcon(icon)
	
	def set_button_icons(self, button, icon_name, width=500, height=55):
		icon_path = ":/tab_icons/{name}.png".format(name=icon_name)
		button.setIconSize(QtCore.QSize(width,height))
		button.setIcon(QtGui.QIcon(icon_path))
	
	def load_fonts(self):
		QtCore.QDir("Montserrat_Alternates")
		QtCore.QDir("Montserrat")
		QtCore.QDir("Roboto")
		QtGui.QFontDatabase().addApplicationFont(":/fonts/Roboto-bold.ttf")
		QtGui.QFontDatabase().addApplicationFont(":/fonts/Montserrat-Bold.ttf")
		QtGui.QFontDatabase().addApplicationFont(":/fonts/MontserratAlternates-Regular.ttf")


	def change_fonts(self, font_type, button_object, is_bold=False):
		font = QtGui.QFont(font_type)
		font.setBold(is_bold)
		button_object.setFont(font)
		# change some fonts
	
	def check_ischecked(self):
		for button in self.ui.frame_top.findChildren(QPushButton):
			print(button)
			if button.isChecked():
				button.setStyleSheet("background-color: rgb(98, 88, 153);")
				button.setCheckable(False)
				button.setEnabled(False)
			else:
				button.setStyleSheet("background-color: white;")
				button.setCheckable(True)
				button.setEnabled(True)
