# access command line arguments
from operator import sub
import sys
import subprocess
import os 
import time
import wmi 

from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
from PyQt5.QtGui import QDesktopServices, QPixmap, QCursor, QWindow, QIcon, QFontMetrics, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QFrame, QProgressBar, QVBoxLayout, QSizeGrip
from PyQt5.QtCore import (QAbstractItemModel, QTemporaryFile, QIODevice, QFile, QUrl, QDir, Qt, QPoint, QSize, QModelIndex, QTimer)

# GUI FILE
from new import Ui_MainWindow
from setup import SetupWindow
from verify import verify

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
        
    def initUI(self):
        # layout to display splash scrren frame
        layout = QVBoxLayout()
        self.setLayout(layout)
        # splash screen frame
        self.frame = QFrame()
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
        license_path = os.path.join(DIR_PATH,FILE)
        file_exist = os.path.isfile(license_path)
        if file_exist:
            with open(license_path, "r") as f:
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
# class PDFWindow(QtWebEngineWidgets.QWebEngineView):
#     def __init__(self, parent=None):
#         super().__init__(parent)

class BaseGuiWindow(QMainWindow):
    # IMPORT fUNCTIONS
    def __init__(self, *args, obj=None, **kwargs):
        super(BaseGuiWindow, self).__init__(*args, **kwargs)
        from ui_functions import UIFunctions
        self.setMinimumSize(QSize(1431,730))
        # Instances of objects
        self.styles = STYLES()
        self.ui = Ui_MainWindow()
        self.model = QtGui.QStandardItemModel()
        # self.display = PDFWindow()
        self.car_model = QtGui.QStandardItemModel()
        self.functions = UIFunctions

        # SETUP UI
        self.ui.setupUi(self)        

        # DEFAULT PATH
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) #get the directory
        self.logo_path = os.path.join(self.dir_path, "Assets/logos")  
        self.icon_path = os.path.join(self.dir_path, "Assets/icons/24x24/")      

        # Link models
        self.ui.dropdown_menu.setModel(self.car_model)
        self.ui.dropdown_menu.setSpacing(3)
        self.ui.dropdown_tree.setStyleSheet('''font-size: 20px;
        font-weight: bold;
        ''')
        self.ui.label_title_bar_top.setStyleSheet("font-size: 17px")
        self.ui.dropdown_tree.setModel(self.model)

        # Create link object for tree view
        self.ui.dropdown_tree.setHeaderHidden(True)
        
        # Add window icons
        self.functions.set_window_icons(self, "Assets/icons/24x24/cil-window-minimize.png", self.ui.minimize_button)
        self.functions.set_window_icons(self, "Assets/icons/24x24/cil-window-maximize.png", self.ui.maximize_button)
        self.functions.set_window_icons(self, "Assets/icons/24x24/cil-x.png", self.ui.close_button)

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


        # change some fonts
        self.functions.load_fonts(self)
        self.functions.change_fonts(self, "Roboto", self.ui.label_title_bar_top, True)
        self.functions.change_fonts(self, "Montserrat_Alternates", self.ui.groupBox_2, True)
        self.functions.change_fonts(self, "Montserrat", self.ui.dropdown_menu, True)
        self.functions.change_fonts(self, "Roboto", self.ui.dropdown_tree, True)
        self.functions.change_fonts(self, "Montserrat", self.ui.label_2, True)
        self.functions.change_fonts(self, "Montserrat", self.ui.label_3, True)

        self.show()

        # Button tab events
        self.ui.button_17.clicked.connect(lambda: self.functions.sub_content(self, "ECU Datasheet", self.ui.button_17.text()))
        self.ui.button_16.clicked.connect(lambda: self.functions.sub_content(self, "ECU TROUBLESHOOTING", self.ui.button_16.text()))
        self.ui.button_15.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\Prog and Decode", self.ui.button_15.text()))
        self.ui.button_14.clicked.connect(lambda: self.functions.sub_content(self, "ECU Repair and Pinout", self.ui.button_14.text()))
        self.ui.button_13.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\Pinout and wiring", self.ui.button_13.text()))
        self.ui.button_12.clicked.connect(lambda: self.functions.sub_content(self, "Airbag", self.ui.button_12.text()))
        self.ui.button_11.clicked.connect(lambda: self.functions.sub_content(self, "Dashboard repair and reset", self.ui.button_11.text()))
        self.ui.button_10.clicked.connect(lambda: self.functions.sub_content(self, "Immobilizer\EEPROM Location", self.ui.button_10.text()))
        self.ui.button_9.clicked.connect(lambda: self.functions.sub_content(self, "Electronics", self.ui.button_9.text()))

        # populate the QListview by their respective indexes
        self.ui.dropdown_menu.clicked.connect(self.book_instance)
        # self.ui.dropdown_tree.doubleClicked.connect(self.tree_double_clicked)
        self.ui.dropdown_tree.clicked.connect(self.check_indexes)


    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def check_indexes(self, index):
        path = self.functions.add_second_link_context(self)
        if os.path.isfile(os.path.join(path, index.data() + ".exe")):
            subprocess.Popen(os.path.join(path, index.data() + ".exe")) 
        elif os.path.isfile(os.path.join(path, index.data() + ".xls")):
            os.startfile(os.path.join(path, index.data() + ".xls"))
        else:
            self.functions.check_books(self, index)
            self.car_model.layoutChanged.emit()
            print('selected item index found at %s with data: %s' %(index.row(), index.data()))
    
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def book_instance(self, index):
        path = self.functions.add_link_context(self)
        if os.path.isfile(os.path.join(path, index.data()+".exe")):
            subprocess.Popen(os.path.join(path, index.data()+".exe"), shell=True) 
        elif os.path.isfile(os.path.join(path, index.data()+".xls")):
            os.startfile(os.path.join(path, index.data() + ".xls"))
        print('selected item index found at %s with data: %s' %(index.row(), index.data()))
        

    # MOUSE EVENTS 
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BaseGuiWindow()
    window.show()
    sys.exit(app.exec_())