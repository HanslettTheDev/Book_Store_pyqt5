# access command line arguments
import os 
import webbrowser
import logging

from PySide2 import QtGui
from PySide2.QtGui import QIcon, QColor
from PySide2.QtWidgets import (QMainWindow, QFileSystemModel, QAbstractItemView, 
	QFrame, QGraphicsDropShadowEffect, QPushButton, QHBoxLayout)
from PySide2.QtCore import Qt, QSize, QTimer

# GUI FILE
from generated_gui.gui import Ui_MainWindow
from utility_scripts.decrypt_pdf import DECRYPT_FILES

# STYLESHEET FILE
from stylesheet import STYLES

from user_interfaces import TempPath
# from user_interfaces.utils import FileIconProvider
from user_interfaces.pdf_viewer import PDFWindow
from user_interfaces.tab_display_window import TabDisplay

class BaseGuiWindow(QMainWindow):
	# IMPORT fUNCTIONS
	def __init__(self, *args, obj=None, **kwargs):
		super(BaseGuiWindow, self).__init__(*args, **kwargs)
		from user_interfaces.customize_ui import UIFunctions
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Main Window running...")
		self.setMinimumSize(QSize(1100, 500))
		# Instances of objects
		self.styles = STYLES()
		self.ui = Ui_MainWindow()
		self.tab_display = TabDisplay()
		# UI Modifications and PDFViewer
		self.functions = UIFunctions
		self.webview = PDFWindow()

		# SETUP UI
		self.ui.setupUi(self)   
		self.setWindowIcon(QIcon(os.path.join(":/tab_icons/logo.jpg")))  

		# DEFAULT PATH and temp variable
		self.dir_path = os.path.join(os.environ['WINDIR'].split(':\\')[0] + ":\\", "ProgramData", "Software") #get the directory 
		
		# Set SizeGrip Image
		self.ui.size_grip.setStyleSheet("QSizeGrip {\n"
		"background-image: url(\':/tab_icons/cil-size-grip.png\');\n"
		"}")
		for frame in self.ui.frame_top.children():
			if type(frame) == QFrame:
				frame.setStyleSheet("background-color: #40A2E3; border-radius: 15px; padding: 2px; color: white;")
				for button in frame.children():
					if type(button) == QPushButton:
						button.setStyleSheet("background-color: white; font-size: 15px; border-radius: 15px; color: black")
		
		self.ui.frame_top.setStyleSheet("#frame_top {background-image: url(\':/tab_icons/home-image.png\');}")
		

		# Overide default styles
		self.ui.label_title_bar_top.setStyleSheet("font-size: 15px")

		# Add window icons
		self.functions.set_window_icons(self, ":/tab_icons/cil-window-minimize.png", self.ui.minimize_button)
		self.functions.set_window_icons(self, ":/tab_icons/cil-window-maximize.png", self.ui.maximize_button)
		self.functions.set_window_icons(self, ":/tab_icons/cil-x.png", self.ui.close_button)
		self.functions.set_window_icons(self, ":/tab_icons/cil-x.png", self.tab_display.ui.close_button)

		# ==> BUTTON CONNECTIONS AND FUNCTIONS
		self.setStyleSheet(self.styles.default_styles)
			
		self.setWindowTitle('Cartronic PROG V2022.1')
		# set the title bar mouse move event
		self.ui.navbar.mouseMoveEvent = self.mouseMoveEvent
		# reset the default MouseMoveEvent
		self.mouseMoveEvent = self.disableMouseEvent
		self.mouseReleaseEvent = self.disableMouseEvent
		self.mouseMoveEvent = self.disableMouseEvent
		# Load UI tweaks
		self.functions.load_ui_tweaks(self)

		# Add button icons
		self.functions.set_button_icons(self, self.ui.button_9, 'electronics')
		self.functions.set_button_icons(self, self.ui.button_10, 'location')
		self.functions.set_button_icons(self, self.ui.button_11, 'dashboard')
		self.functions.set_button_icons(self, self.ui.button_14, 'ecu-pinout')
		self.functions.set_button_icons(self, self.ui.button_16, 'troubleshooting')
		self.functions.set_button_icons(self, self.ui.button_17, 'datasheet')
		# self.functions.set_button_icons(self, self.ui.whatsapp_button, 'whatsapp', width=20, height=20)
		# self.functions.set_button_icons(self, self.ui.gmail_button, 'gmail', width=20, height=20)

		# LOGO BUTTON ICON
		self.ui.logo_button.setIcon(QIcon(":/tab_icons/logo.jpg"))

		# change some fonts
		self.functions.load_fonts(self)
		self.functions.change_fonts(self, "Roboto", self.ui.label_title_bar_top, True)
		self.functions.change_fonts(self, "Montserrat_Alternates", self.tab_display.ui.groupBox_2, True)
		self.functions.change_fonts(self, "Montserrat_Alternates", self.tab_display.ui.groupBox_3, True)
		self.functions.change_fonts(self, "Montserrat", self.tab_display.ui.dropdown_menu, True)
		self.functions.change_fonts(self, "Roboto", self.tab_display.ui.dropdown_tree, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_3, True)

		# QLabel 
		self.functions.change_fonts(self, "Montserrat", self.ui.label_5, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_6, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_7, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_8, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_9, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_12, True)
		self.show()

		# Button tab events to launch the tab display window
		# self.ui.whatsapp_button.clicked.connect(lambda: self.open_whatsapp_or_email('Whatsapp'))
		# self.ui.gmail_button.clicked.connect(lambda: self.open_whatsapp_or_email('Gmail'))
		self.ui.button_17.clicked.connect(lambda: self.functions.sub_content(self, "ECU Datasheet", self.ui.label_9.text()))
		self.ui.button_16.clicked.connect(lambda: self.functions.sub_content(self, "ECU TROUBLESHOOTING", self.ui.label_7.text()))
		self.ui.button_14.clicked.connect(lambda: self.functions.sub_content(self, "ECU Repair and Pinout", self.ui.label_5.text()))
		self.ui.button_11.clicked.connect(lambda: self.functions.sub_content(self, "Dashboard repair and reset", self.ui.label_6.text()))
		self.ui.button_10.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\EEPROM Location", self.ui.label_12.text()))
		self.ui.button_9.clicked.connect(lambda: self.functions.sub_content(self, "Electronics", self.ui.label_8.text()))


		self.ui.button_17.clicked.connect(lambda: self.is_active)
		self.ui.button_16.clicked.connect(lambda: self.is_active)
		self.ui.button_14.clicked.connect(lambda: self.is_active)
		self.ui.button_11.clicked.connect(lambda: self.is_active)
		self.ui.button_10.clicked.connect(lambda: self.is_active)
		self.ui.button_9.clicked.connect(lambda: self.is_active)


		# populate the QListview by their respective indexes
		# On the other hand the second QListView must have a model where items are added or 
		# removed as they are selected or deselected, 
		# for this you must use the selectionChanged signal of selectionModel() of the first QListView, 
		# that signal transports the information of the selected and deselected items.(
		# Source StackOverflow(https://stackoverflow.com/questions/53270404/two-qlistview-box-one-showing-files-in-a-folder-and-one-shows-selected-files-fro))
		self.tab_display.ui.dropdown_menu.clicked.connect(self.book_instance)
		self.tab_display.ui.dropdown_tree.clicked.connect(self.check_indexes)

		self.dragging = False
		self.old_pos = None


	# @QtCore.Slot(QtCore.QModelIndex)
	def check_indexes(self, index):
		self.tab_display.car_model.removeRows(0, self.tab_display.car_model.rowCount())
		self.tab_display.car_model.layoutChanged.emit()
		for filename in os.listdir(index.data(QFileSystemModel.FilePathRole)):
			if os.path.isfile(os.path.join(index.data(QFileSystemModel.FilePathRole), filename)):
				for ext in [".pdf.aes", ".chm", ".xlsx", ".xls"]:
					if filename.endswith(ext):
						item = QtGui.QStandardItem(filename.split(ext)[0])
						item.setEditable(False)
						self.tab_display.car_model.appendRow(item)
						break
				global return_path 
				return_path = os.path.join(index.data(QFileSystemModel.FilePathRole))
		# print('selected item index found at %s with data: %s' %(index.row(), index.data(QFileSystemModel.FilePathRole)))
	
	def check_webview_states(self, path, index):
		if self.webview.windowState() == Qt.WindowMinimized:
			self.webview.close()
			# self.progress_bar(index)
			self.webview.load_pdf(path)
			self.webview.showNormal()
		elif self.webview.windowState() != Qt.WindowActive:
			self.webview.close()
			# self.progress_bar(index)
			self.webview.load_pdf(path)
			self.webview.showNormal()
		if self.webview.windowState() == Qt.WindowMaximized:
			self.webview.close()
			# self.progress_bar(index)
			self.webview.load_pdf(path)
			self.webview.showNormal()
		else:
			self.webview.showNormal()

   
	# @QtCore.Slot(QtCore.QModelIndex)
	def book_instance(self, index):
		if os.path.isfile(os.path.join(return_path, index.data()+".pdf.aes")):
			path = DECRYPT_FILES(os.path.join(return_path, index.data()+".pdf.aes")).decrypt_pdf()
			self.remove_previous_files(path.split("\\")[-1])
			self.webview.load_pdf(path)
			self.check_webview_states(path, index.data())
		elif os.path.isfile(os.path.join(return_path, index.data()+".chm")):
			os.system("hh.exe %s::/4_Userguide.htm#_Toc270510" %os.path.join(return_path, index.data()+".chm"))
		elif os.path.isfile(os.path.join(return_path, index.data()+".xlsx")):
			self.progress_bar(index.data())
			os.startfile(os.path.join(return_path, index.data()+".xlsx"))			
		# print('selected item index found at %s with data: %s' %(index.row(), index.data()))

	def remove_previous_files(self, filename):
		for file in os.listdir(TempPath):
			if file.startswith("tmp"):
				if filename != file:
					os.remove(os.path.join(TempPath, file))

	def close_tab_window(self):
		h,w = 500, 1100
		self.tab_display.hide()
		self.setMinimumSize(QSize(w, h))
		self.resize(QSize(w, h))
	
	@QtCore.Slot(QtCore.QModelIndex)
	def is_active(self, event):
		print(event)
		

	# MOUSE EVENTS 
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragging = True
			self.old_pos = event.globalPos()


	def mouseMoveEvent(self, event):
		if self.dragging:
			delta = event.globalPos() - self.old_pos
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.old_pos = event.globalPos()
	

	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragging = False
	
	def disableMouseEvent(self, event):
		pass
	
	# def open_whatsapp_or_email(self, label):
	# 	if label == "Whatsapp":
	# 		webbrowser.open("https://wa.me/c/237676634413")
	# 	else:
	# 		webbrowser.open("https://google.com")
