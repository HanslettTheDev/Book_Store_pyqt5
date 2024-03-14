# access command line arguments
import os 
import webbrowser
import logging

from PySide2 import QtGui
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QFileSystemModel, QAbstractItemView
from PySide2.QtCore import Qt, QSize, QTimer

# GUI FILE
from generated_gui.gui import Ui_MainWindow
from utility_scripts.decrypt_pdf import DECRYPT_FILES

# STYLESHEET FILE
from stylesheet import STYLES

from user_interfaces import TempPath, logger
from user_interfaces.utils import FileIconProvider
from user_interfaces.pdf_viewer import PDFWindow

class BaseGuiWindow(QMainWindow):
	# IMPORT fUNCTIONS
	def __init__(self, *args, obj=None, **kwargs):
		super(BaseGuiWindow, self).__init__(*args, **kwargs)
		from user_interfaces.customize_ui import UIFunctions
		self.logger = logger
		logger.debug("Main Window running...")
		self.setMinimumSize(QSize(1431,730))
		# Instances of objects
		self.styles = STYLES()
		self.ui = Ui_MainWindow()
		self.model = QFileSystemModel()
		self.model.setIconProvider(FileIconProvider())
		# Create ListView Model Object
		self.car_model = QtGui.QStandardItemModel()
		self.functions = UIFunctions
		self.webview = PDFWindow()

		# SETUP UI
		self.ui.setupUi(self)   
		self.setWindowIcon(QIcon(os.path.join(":/tab_icons/logo.jpg")))  

		# DEFAULT PATH and temp variable
		self.dir_path = os.path.join(os.environ['WINDIR'].split(':\\')[0] + ":\\", "ProgramData", "Software") #get the directory 
		
		# set models for QTreeView and QListView
		self.ui.dropdown_tree.setModel(self.model)
		self.ui.dropdown_menu.setModel(self.car_model)

		# Create link object for tree view
		self.ui.dropdown_tree.setHeaderHidden(True)
		
		self.ui.dropdown_menu.setSpacing(2)
		self.ui.dropdown_tree.setStyleSheet('''font-size: 20px;
		font-weight: bold;
		''')
		# Set SizeGrip Image
		self.ui.size_grip.setStyleSheet("QSizeGrip {\n"
		"background-image: url(\':/tab_icons/cil-size-grip.png\');\n"
		"}")

		self.ui.frame_center.setStyleSheet('''#frame_center {
		background-image: url(\':/tab_icons/background.jpg\');
		}
		''')

		# Overide default styles
		self.ui.label_title_bar_top.setStyleSheet("font-size: 15px")

		# Add window icons
		self.functions.set_window_icons(self, ":/tab_icons/cil-window-minimize.png", self.ui.minimize_button)
		self.functions.set_window_icons(self, ":/tab_icons/cil-window-maximize.png", self.ui.maximize_button)
		self.functions.set_window_icons(self, ":/tab_icons/cil-x.png", self.ui.close_button)

		# ==> BUTTON CONNECTIONS AND FUNCTIONS
		# self.setStyleSheet(self.styles.default_styles)
		def move_window(event):
			if self.functions.return_status() == 1:
				self.functions.maximize_window()
			# move window
			if Qt.LeftButton and self.moveFlag:
				self.move(event.globalPos() - self.movePosition)
				event.accept()
		
		self.ui.label_title_bar_top.setText('Cartronic PROG')
		self.ui.nav_title.mouseMoveEvent = move_window
		self.functions.load_ui_tweaks(self)

		# Add button icons
		self.functions.set_button_icons(self, self.ui.button_9, 'electronics')
		self.functions.set_button_icons(self, self.ui.button_10, 'eeprom')
		self.functions.set_button_icons(self, self.ui.button_11, 'dashboard')
		self.functions.set_button_icons(self, self.ui.button_14, 'ecu-pinout')
		self.functions.set_button_icons(self, self.ui.button_16, 'troubleshooting')
		self.functions.set_button_icons(self, self.ui.button_17, 'datasheet')
		self.functions.set_button_icons(self, self.ui.whatsapp_button, 'whatsapp', width=20, height=20)
		self.functions.set_button_icons(self, self.ui.gmail_button, 'gmail', width=20, height=20)

		# LOGO BUTTON ICON
		self.ui.logo_button.setIcon(QIcon(":/tab_icons/logo.jpg"))

		# change some fonts
		self.functions.load_fonts(self)
		self.functions.change_fonts(self, "Roboto", self.ui.label_title_bar_top, True)
		self.functions.change_fonts(self, "Montserrat_Alternates", self.ui.groupBox_2, True)
		self.functions.change_fonts(self, "Montserrat_Alternates", self.ui.groupBox_3, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.dropdown_menu, True)
		self.functions.change_fonts(self, "Roboto", self.ui.dropdown_tree, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_2, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_3, True)

		# QLabel 
		self.functions.change_fonts(self, "Montserrat", self.ui.label_5, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_6, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_7, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_8, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_9, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_12, True)
		self.show()


		# Button tab events
		self.ui.whatsapp_button.clicked.connect(lambda: self.open_whatsapp_or_email('Whatsapp'))
		self.ui.gmail_button.clicked.connect(lambda: self.open_whatsapp_or_email('Gmail'))
		self.ui.button_17.clicked.connect(lambda: self.functions.sub_content(self, "ECU Datasheet", self.ui.label_9.text()))
		self.ui.button_16.clicked.connect(lambda: self.functions.sub_content(self, "ECU TROUBLESHOOTING", self.ui.label_7.text()))
		self.ui.button_14.clicked.connect(lambda: self.functions.sub_content(self, "ECU Repair and Pinout", self.ui.label_5.text()))
		self.ui.button_11.clicked.connect(lambda: self.functions.sub_content(self, "Dashboard repair and reset", self.ui.label_6.text()))
		self.ui.button_10.clicked.connect(lambda: self.functions.sub_content(self, "EEPROM Location", self.ui.label_12.text()))
		self.ui.button_9.clicked.connect(lambda: self.functions.sub_content(self, "Electronics", self.ui.label_8.text()))

		# populate the QListview by their respective indexes
		# On the other hand the second QListView must have a model where items are added or 
		# removed as they are selected or deselected, 
		# for this you must use the selectionChanged signal of selectionModel() of the first QListView, 
		# that signal transports the information of the selected and deselected items.(
		# Source StackOverflow(https://stackoverflow.com/questions/53270404/two-qlistview-box-one-showing-files-in-a-folder-and-one-shows-selected-files-fro))
		self.ui.dropdown_menu.clicked.connect(self.book_instance)
		self.ui.dropdown_tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.ui.dropdown_tree.clicked.connect(self.check_indexes)


	# @QtCore.Slot(QtCore.QModelIndex)
	def check_indexes(self, index):
		self.car_model.removeRows(0,self.car_model.rowCount())
		self.car_model.layoutChanged.emit()
		for filename in os.listdir(index.data(QFileSystemModel.FilePathRole)):
			if os.path.isfile(os.path.join(index.data(QFileSystemModel.FilePathRole), filename)):
				for ext in [".pdf.aes", ".chm", ".xlsx", ".xls"]:
					if filename.endswith(ext):
						print(filename.split(ext)[0])
						item = QtGui.QStandardItem(filename.split(ext)[0])
						item.setEditable(False)
						self.car_model.appendRow(item)
						break
				global return_path 
				return_path = os.path.join(index.data(QFileSystemModel.FilePathRole))
		# print('selected item index found at %s with data: %s' %(index.row(), index.data(QFileSystemModel.FilePathRole)))
	
	def progress_bar(self, item):
		self.ui.message.setText(f" Loading {item} to Viewer")
		self.timer = QTimer()
		self.timer.timeout.connect(lambda: self.completed(item))
		self.timer.start(2000)

	def check_webview_states(self, path, index):
		if self.webview.windowState() == Qt.WindowMinimized:
			self.webview.close()
			self.progress_bar(index)
			self.webview.load_pdf(path)
			self.webview.showNormal()
		elif self.webview.windowState() != Qt.WindowActive:
			self.webview.close()
			self.progress_bar(index)
			self.webview.load_pdf(path)
			self.webview.showNormal()
		if self.webview.windowState() == Qt.WindowMaximized:
			self.webview.close()
			self.progress_bar(index)
			self.webview.load_pdf(path)
			self.webview.showNormal()
		else:
			self.webview.showNormal()

	def completed(self, item):
		self.ui.message.setText(f"Successfully Loaded {item}. Check Viewer")

	# @QtCore.Slot(QtCore.QModelIndex)
	def book_instance(self, index):
		if os.path.isfile(os.path.join(return_path, index.data()+".pdf.aes")):
			path = DECRYPT_FILES(os.path.join(return_path, index.data()+".pdf.aes")).decrypt_pdf()
			self.progress_bar(index.data())
			self.remove_previous_files(path.split("\\")[-1])
			self.webview.load_pdf(path)
			self.check_webview_states(path, index.data())
		elif os.path.isfile(os.path.join(return_path, index.data()+".chm")):
			self.progress_bar(index.data())
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



	# MOUSE EVENTS 
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.moveFlag = True
			self.movePosition = event.globalPos() - self.pos()
			event.accept()

	def mouseReleaseEvent(self, event):
		self.offset = None
		super().mouseReleaseEvent(event)  
	
	def open_whatsapp_or_email(self, label):
		if label == "Whatsapp":
			webbrowser.open("https://wa.me/c/237676634413")
		else:
			webbrowser.open("https://google.com")