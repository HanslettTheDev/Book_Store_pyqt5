from distutils import dir_util
import os

from main import BaseGuiWindow
from PyQt5 import (QtCore, QtWidgets, QtGui)
from PyQt5.QtCore import (QAbstractListModel, QIODevice, QDir, QFile, QByteArray, QPoint, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QStandardItem, QStandardItemModel)
from PyQt5.QtWidgets import *

from resource import resources

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
            icon.addFile(u"Assets/icons/24x24/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.maximize_button.setIcon(icon)
        else:
            WINDOW_STATE = 0
            self.showNormal()
            self.ui.centralwidget.setContentsMargins(10,10,10,10)
            self.ui.maximize_button.setToolTip("Maximize")
            icon = QIcon()
            icon.addFile(u"Assets/icons/24x24/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
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

        self.ui.close_button.clicked.connect(lambda: self.close())
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_button.clicked.connect(lambda: self.functions.maximize_window(self))
        QSizeGrip(self.ui.size_grip)#resize option
        

    def sub_content(self, main_content, label):
        self.model.removeRows(0, self.model.rowCount()) # empty the model for each button click
        self.model.layoutChanged.emit()
        self.car_model.removeRows(0, self.car_model.rowCount()) # empty the second list view as well
        self.car_model.layoutChanged.emit()
        self.ui.groupBox_2.setTitle(label) #change label 4 text to the label selected
        book_path = "Lib\{main_content}".format(main_content=main_content)
        global file_path, all_dir
        file_path = os.path.join(self.dir_path, book_path)
        all_dir = os.listdir(file_path)
        if os.path.isdir(file_path):
            all_dir = os.listdir(file_path)
            for ad in all_dir:
                try:
                    if os.path.isfile(os.path.join(file_path, ad)):
                        removed_ext = os.path.splitext(ad)
                        item = QtGui.QStandardItem(removed_ext[0])
                        self.model.appendRow(item)
                        item.setEditable(False)
                    else:
                        folder = QtGui.QStandardItem(ad)
                        folder.setEditable(False)
                        self.model.appendRow(folder)
                        car = ad.lower()
                        folder.setData(QIcon(os.path.join(self.logo_path, 'logo-{car}.png'.format(car=car))), QtCore.Qt.DecorationRole)
                        for vb in os.listdir(os.path.join(file_path, ad)):
                            removed_ext = os.path.splitext(vb)
                            sub_item = QtGui.QStandardItem(removed_ext[0])
                            sub_item.setEditable(False)
                            folder.appendRow(sub_item)     
                except Exception as e:
                    print(e)
        else:
            self.book_instance(file_path)
    
    def check_books(self, index):
        try:
            if all_dir != []:
                for ad in all_dir:
                    if os.path.isdir(os.path.join(file_path, ad, index.data())):
                        self.car_model.removeRows(0,self.car_model.rowCount()) # empty the model for each button click
                        self.car_model.layoutChanged.emit()
                        for file in os.listdir(os.path.join(file_path, ad, index.data())):
                            global book_link
                            book_link = os.path.join(file_path, ad, index.data())
                            removed_ext = os.path.splitext(file)
                            item = QtGui.QStandardItem(removed_ext[0])
                            item.setEditable(False)
                            self.car_model.appendRow(item)
                    
        except Exception as e:
            print(e)
    
    def add_link_context(self):
        return book_link
    
    def add_second_link_context(self):
        return file_path
    
    def set_window_icons(self, url, button):
        path = os.path.join(self.dir_path, url)
        icon = QIcon()
        icon.addFile(path)
        button.setIcon(icon)
    
    def set_button_icons(self, button, icon_name):
        icon_path = os.path.join(self.icon_path, icon_name+".png")
        button.setIcon(QtGui.QIcon(icon_path))
        button.setIconSize(QtCore.QSize(20,20))
    
    def load_fonts(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        font_path = os.path.join(dir_path, "Assets/fonts/")
        QtCore.QDir("Montserrat_Alternates")
        QtCore.QDir("Montserrat")
        QtCore.QDir("Roboto")
        QtGui.QFontDatabase().addApplicationFont(font_path + "Roboto/Roboto-bold.ttf")
        QtGui.QFontDatabase().addApplicationFont(font_path + "Montserrat/Montserrat-Bold.ttf")
        QtGui.QFontDatabase().addApplicationFont(font_path + "Montserrat_Alternates/MontserratAlternates-Regular.ttf")
        print(os.path.isfile(font_path + "Montserrat_Alternates/MontserratAlternates-bold.ttf"))
    
    def change_fonts(self, font_type, button_object, is_bold=False):
        font = QtGui.QFont(font_type)
        font.setBold(is_bold)
        button_object.setFont(font)
        # change some fonts

