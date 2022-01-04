import os

from main import BaseGuiWindow, DropdownModel
from PyQt5 import (QtCore, QtWidgets, QtGui)
from PyQt5.QtCore import (QAbstractListModel, QPoint, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QStandardItem, QStandardItemModel)
from PyQt5.QtWidgets import *

class UIFunctions(BaseGuiWindow):

    def toggle_active(self, button_name:str):
        if button_name == "airbag":
            # Disable other active buttons
            self.ui.button_5.setStyleSheet("background-color: #AA14F0;")
            self.ui.button_4.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_3.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_2.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_1.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")

        elif button_name == "panel":
            # Disable other active buttons
            self.ui.button_5.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_3.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_2.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_1.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_4.setStyleSheet("background-color: #AA14F0;")
        elif button_name == "immobi":
            # Disable other active buttons
            self.ui.button_5.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_4.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_3.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_1.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_2.setStyleSheet("background-color: #AA14F0;")
        elif button_name == "repair":
            # Disable other active buttons
            self.ui.button_5.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_4.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_3.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_2.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_1.setStyleSheet("background-color: #AA14F0;")
        else:
            # Disable other active buttons
            self.ui.button_5.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_4.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_2.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_1.setStyleSheet("background-color: rgb(5, 13, 25);\ncolor: white;")
            self.ui.button_3.setStyleSheet("background-color: #AA14F0;")

    def immobilizer(self, maxheight, enable):
        if enable:
            # GET WIDTH
            height = self.ui.dropdown_box.height()
            maxExtend = maxheight

            # SET MAX WIDTH
            if height == maxExtend:
                self.ui.dropdown_box.setFixedHeight(0)
            else:
                self.ui.dropdown_box.setFixedHeight(121)
    
    def sub_content(self, main_content, label):
        self.ui.dropdown_box.setFixedHeight(0) #reset existing dropdown height 
        self.model.dropdown = [] # empty the model for each button click
        self.model.layoutChanged.emit()
        self.car_model.dropdown = [] # empty the second list view as well
        self.car_model.layoutChanged.emit()
        # self.ui.label.setText(label)
        dir_path = os.path.dirname(os.path.realpath(__file__)) #get the directory
        global book_path
        book_path = "Lib\{main_content}".format(main_content=main_content)
        file_path = os.path.join(dir_path, book_path)
        print(file_path)
        all_dir = os.listdir(file_path)
        if all_dir != []:
            for ad in all_dir:
                self.model.dropdown.append(ad)
                self.model.layoutChanged.emit()
        else:
            pass
        if main_content == "Immobilizer\EEPROM Location" or main_content == "Immobilizer\Pinout and wiring" or main_content =="Immobilizer\Prog and decode":
            self.ui.dropdown_box.setFixedHeight(0)
    
    def check_books(self, index):
        dir_path = os.path.dirname(os.path.realpath(__file__)) #get the directory
        sub_path = "{sub_index}".format(sub_index=index.data())
        global file_path  
        file_path = os.path.join(dir_path, book_path, sub_path)
        all_dir = os.listdir(file_path)
        if all_dir != []:
            for ad in all_dir:
                self.car_model.dropdown.append(ad)
    
    def book_url(self, index):
        book_name = "{name}".format(name=index.data())
        book_url = os.path.join(file_path, book_name)
        print(book_url)
        return book_url