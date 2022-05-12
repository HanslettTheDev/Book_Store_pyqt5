# access command line arguments
import os 
import time
import wmi 
import webbrowser
import logging


from PySide6 import QtCore, QtGui, QtWebEngineWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QFrame, QProgressBar, QVBoxLayout, QFileSystemModel, QAbstractItemView
from PySide6.QtCore import Qt, QSize, QTimer

# GUI FILE
from gui import Ui_MainWindow
from setup import SetupWindow
from verify import verify
from decrypt import DECRYPT_FILES

import resources

# STYLESHEET FILE
from stylesheet import STYLES

class SplashScreen(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(700, 350)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.counter = 0
		self.n = 100 
		self.initUI()
		self.timer = QTimer()
		self.timer.timeout.connect(self.loading)
		self.timer.start(100)
		self.setStyleSheet(STYLES.splash)
		self.frame.setStyleSheet("background-image: url(:/tab_icons/logo.jpg);")
		
	def initUI(self):
		# layout to display splash scrren frame
		layout = QVBoxLayout()
		self.setLayout(layout)
		# splash screen frame
		self.frame = QFrame()
		self.frame.setObjectName("frame")
		layout.addWidget(self.frame)
		# splash screen title
		self.title_label = QLabel(self.frame)
		self.title_label.setObjectName('title_label')
		self.title_label.resize(690, 120)
		self.title_label.move(0, 5) # x, y
		self.title_label.setText('ECU PROTECH')
		self.title_label.setFont(QtGui.QFont("Montserrat Alternates"))
		self.title_label.setAlignment(Qt.AlignCenter)
		# splash screen title description
		self.description_label = QLabel(self.frame)
		self.description_label.resize(690, 40)
		self.description_label.move(0, self.title_label.height())
		self.description_label.setObjectName('desc_label')
		self.description_label.setText('<b>Making sure everything is ready</b>')
		self.description_label.setAlignment(Qt.AlignCenter)
		# splash screen pogressbar
		self.progressBar = QProgressBar(self.frame)
		self.progressBar.resize(self.width() - 200 - 10, 50)
		self.progressBar.move(100, 180) # self.description_label.y()+130
		self.progressBar.setAlignment(Qt.AlignCenter)
		self.progressBar.setFormat('%p%')
		self.progressBar.setTextVisible(True)
		self.progressBar.setRange(0, self.n)
		self.progressBar.setValue(20)
		# spash screen loading label
		self.loading_label = QLabel(self.frame)
		self.loading_label.resize(self.width() - 10, 50)
		self.loading_label.move(0, self.progressBar.y() + 70)
		self.loading_label.setObjectName('loading_label')
		self.loading_label.setAlignment(Qt.AlignCenter)
		self.loading_label.setText('Loading...')

	def loading(self):
		# set progressbar value
		self.progressBar.setValue(self.counter)
		# stop progress if counter
		# is greater than n and
		# display main window app
		if self.counter >= self.n:
			self.timer.stop()
			self.close()
			time.sleep(1)
			self.main_app = self.verify_license()
			self.main_app.show()
		self.counter += 1

	def verify_license(self):
		DIR_PATH = os.getenv('LOCALAPPDATA')
		FILE = "yagamie.key"
		if os.path.isfile(os.path.join(DIR_PATH,"yagamie.key")):
			with open(os.path.join(DIR_PATH,"yagamie.key"), "r") as f:
				key = f.readline()
			chars = key.split("+=")
			key_id = chars[0]
			key_address = chars[1]
			blob = self.get_hardware_id()
			hd_id = blob[0].split(" ")
			
			if (hd_id[-1] == key_id) and verify(key_address):
				return BaseGuiWindow()
			else:
				return SetupWindow()
		else:
			return SetupWindow()
	
	def get_hardware_id(self):
		c = wmi.WMI()
		hardware_id = []
		for item in c.Win32_PhysicalMedia():
			if item.SerialNumber != None:
				hardware_id.append(item.SerialNumber)
		return hardware_id


class DropdownModel(QtCore.QAbstractListModel):
	def __init__(self, *args,  dropdown=None, **Kwargs):
		super().__init__(*args, **Kwargs)
		self.dropdown = dropdown or []

	def data(self, index, role):
		if role == Qt.DisplayRole:
			text = self.dropdown[index.row()]
			return text
	
	def rowCount(self, index):
		return len(self.dropdown)

class CarModel(QtCore.QAbstractListModel):
	def __init__(self, *args,  dropdown=None, **Kwargs):
		super().__init__(*args, **Kwargs)
		self.dropdown = dropdown or []

	def data(self, index, role):
		if role == Qt.DisplayRole:
			text = self.dropdown[index.row()]
			return text

	def rowCount(self, index):
		return len(self.dropdown)
class PDFWindow(QtWebEngineWidgets.QWebEngineView):
	def __init__(self):
		super(PDFWindow, self).__init__()
		self.settings().setAttribute(
			self.settings().PluginsEnabled, True)
		self.settings().setAttribute(
			self.settings().PdfViewerEnabled, True)
		self.settings().setAttribute(
			self.settings().ScreenCaptureEnabled, True)
		self.setWindowTitle("Cartronic Prog Viewer")
		self.setWindowIcon(QIcon(os.path.join(":/tab_icons/logo.jpg")))
	
	def load_pdf(self, pdf_file):
		self.load(QtCore.QUrl.fromUserInput(pdf_file))

class BaseGuiWindow(QMainWindow):
	# IMPORT fUNCTIONS
	def __init__(self, *args, obj=None, **kwargs):
		super(BaseGuiWindow, self).__init__(*args, **kwargs)
		from ui_functions import UIFunctions
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Main Window running...")
		self.setMinimumSize(QSize(1431,730))
		# Instances of objects
		self.styles = STYLES()
		self.ui = Ui_MainWindow()
		self.model = QFileSystemModel()
		# Create ListView Model Object
		self.car_model = QtGui.QStandardItemModel()
		self.functions = UIFunctions
		self.webview = PDFWindow()

		# SETUP UI
		self.ui.setupUi(self)   
		self.setWindowIcon(QIcon(os.path.join(":/tab_icons/logo.jpg")))  

		# DEFAULT PATH
		self.dir_path = os.path.dirname(os.path.realpath(__file__)) #get the directory
		self.temp_files:str = []     
		
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
		
		self.setWindowTitle('Cartronic PROG V2022.1')
		self.ui.nav_title.mouseMoveEvent = move_window
		self.functions.load_ui_tweaks(self)

		# Add button icons
		self.functions.set_button_icons(self, self.ui.button_9, 'electronics')
		self.functions.set_button_icons(self, self.ui.button_10, 'location')
		self.functions.set_button_icons(self, self.ui.button_11, 'dashboard')
		self.functions.set_button_icons(self, self.ui.button_12, 'airbag')
		self.functions.set_button_icons(self, self.ui.button_13, 'eeprom')
		self.functions.set_button_icons(self, self.ui.button_14, 'ecu-pinout')
		self.functions.set_button_icons(self, self.ui.button_15, 'prog')
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
		self.functions.change_fonts(self, "Montserrat", self.ui.label_4, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_5, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_6, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_7, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_8, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_9, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_10, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_11, True)
		self.functions.change_fonts(self, "Montserrat", self.ui.label_12, True)
		self.show()


		# Button tab events
		self.ui.whatsapp_button.clicked.connect(lambda: self.open_whatsapp_or_email('Whatsapp'))
		self.ui.gmail_button.clicked.connect(lambda: self.open_whatsapp_or_email('Gmail'))
		self.ui.button_17.clicked.connect(lambda: self.functions.sub_content(self, "ECU Datasheet", self.ui.label_9.text()))
		self.ui.button_16.clicked.connect(lambda: self.functions.sub_content(self, "ECU TROUBLESHOOTING", self.ui.label_7.text()))
		self.ui.button_15.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\Prog and Decode", self.ui.label_10.text()))
		self.ui.button_14.clicked.connect(lambda: self.functions.sub_content(self, "ECU Repair and Pinout", self.ui.label_5.text()))
		self.ui.button_13.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\Pinout and wiring", self.ui.label_11.text()))
		self.ui.button_12.clicked.connect(lambda: self.functions.sub_content(self, "Airbag", self.ui.label_4.text()))
		self.ui.button_11.clicked.connect(lambda: self.functions.sub_content(self, "Dashboard repair and reset", self.ui.label_6.text()))
		self.ui.button_10.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\EEPROM Location", self.ui.label_12.text()))
		self.ui.button_9.clicked.connect(lambda: self.functions.sub_content(self, "Electronics", self.ui.label_8.text()))

		# populate the QListview by their respective indexes
		# On the other hand the second QListView must have a model where items are added or 
		# removed as they are selected or deselected, 
		# for this you must use the selectionChanged signal of selectionModel() of the first QListView, 
		# that signal transports the information of the selected and deselected items.(
		# Source StackOverflow(https://stackoverflow.com/questions/53270404/two-qlistview-box-one-showing-files-in-a-folder-and-one-shows-selected-files-fro))
		# self.ui.dropdown_tree.selectionModel().selectionChanged.connect(self.book_instance)
		self.ui.dropdown_menu.clicked.connect(self.book_instance)
		self.ui.dropdown_tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.ui.dropdown_tree.clicked.connect(self.check_indexes)


	@QtCore.Slot(QtCore.QModelIndex)
	def check_indexes(self, index):
		self.car_model.removeRows(0,self.car_model.rowCount())
		self.car_model.layoutChanged.emit()
		for filename in os.listdir(index.data(QFileSystemModel.FilePathRole)):
			if os.path.isfile(os.path.join(index.data(QFileSystemModel.FilePathRole), filename)):
				for ext in [".pdf.aes", ".chm", ".xlsx", ".xls"]:
					if filename.endswith(ext):
						item = QtGui.QStandardItem(filename.strip(ext))
						item.setEditable(False)
						self.car_model.appendRow(item)
						break
				global return_path 
				return_path = os.path.join(index.data(QFileSystemModel.FilePathRole))
		print('selected item index found at %s with data: %s' %(index.row(), index.data(QFileSystemModel.FilePathRole)))
	
	def progress_bar(self, item):
		self.ui.message.setText(f" Loading {item} to Viewer")
		self.timer = QTimer()
		self.timer.timeout.connect(lambda: self.completed(item))
		self.timer.start(2000)

	def check_webview_states(self, path, index):
		if self.webview.isVisible():
			if self.webview.isActiveWindow():
				pass
			else:
				self.webview.close()
				self.progress_bar(index)
				self.webview.load_pdf(path)
				self.webview.show()
		elif self.webview.isMinimized():
			self.webview.show()
		else:
			self.webview.show()
	def completed(self, item):
		self.ui.message.setText(f"Successfully Loaded {item}. Check Viewer")

	@QtCore.Slot(QtCore.QModelIndex)
	def book_instance(self, index):
		if os.path.isfile(os.path.join(return_path, index.data()+".pdf.aes")):
			path = DECRYPT_FILES(os.path.join(return_path, index.data()+".pdf.aes")).decrypt_pdf()
			self.temp_files.append(path)
			self.progress_bar(index.data())
			self.webview.load_pdf(path)
			self.check_webview_states(path, index.data())
		elif os.path.isfile(os.path.join(return_path, index.data()+".chm")):
			self.progress_bar(index.data())
			os.system("hh.exe %s::/4_Userguide.htm#_Toc270510" %os.path.join(return_path, index.data()+".chm"))
		elif os.path.isfile(os.path.join(return_path, index.data()+".xlsx")):
			self.progress_bar(index.data())
			os.startfile(os.path.join(return_path, index.data()+".xlsx"))			
		# print('selected item index found at %s with data: %s' %(index.row(), index.data()))


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
