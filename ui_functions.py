import os

from main import BaseGuiWindow
from PySide6 import (QtCore, QtGui)
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor,QIcon
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QPushButton

import os

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
		for tf in self.temp_files:
			try:	
				os.remove(tf)
			except Exception as e:
				self.logger.debug("There was an issue Deleting the temp files:", exc_info=True)
				continue
		self.webview.close()
		self.logger.info("Temp Files Deleted successfully:")
		self.close()

	def sub_content(self, main_content, label):
		# Button active state
		self.functions.check_ischecked(self)
		# Set rootpath per button clicked and rootIndex
		self.model.setRootPath(os.path.join(self.dir_path, f"Lib/{main_content}"))
		# set model filter to filter only files to the second list view
		self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
		self.ui.dropdown_tree.setModel(self.model)
		self.ui.dropdown_tree.setRootIndex(self.model.index(os.path.join(self.dir_path, f"Lib/{main_content}")))
		self.ui.dropdown_tree.setColumnWidth(0,250)
		self.ui.dropdown_tree.setAlternatingRowColors(True)
		# Hide the file type, folder size and date created columns
		self.ui.dropdown_tree.hideColumn(1)
		self.ui.dropdown_tree.hideColumn(2)
		self.ui.dropdown_tree.hideColumn(3)
		# Set the label to the button clicked
		if main_content == "Immobilizer\EEPROM Location":
			self.ui.groupBox_3.setTitle("IMMO Data") 
			self.ui.groupBox_2.setTitle(f"{label}")
		elif main_content == "ECU Datasheet":
			self.ui.groupBox_3.setTitle("Manufacturer") 
			self.ui.groupBox_2.setTitle(f"{label}")
		elif main_content == "Electronics":
			self.ui.groupBox_3.setTitle("Electrical/Electronic Manuals")
			self.ui.groupBox_2.setTitle(f"{label}")
		else:
			self.ui.groupBox_3.setTitle("Car Model")
			self.ui.groupBox_2.setTitle(f"{label}")  				
	
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
		all_buttons = self.ui.frame_top.findChildren(QPushButton)
		for button in all_buttons:
			if button.isChecked():
				button.setStyleSheet("background-color: rgb(98, 88, 153);")
				button.setCheckable(False)
			else:
				button.setStyleSheet("background-color: white;")
				button.setCheckable(True)