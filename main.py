# access command line arguments
import sys
import os

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QDesktopServices, QPixmap, QCursor, QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

from PyQt5.QtCore import (QAbstractItemModel, QUrl, Qt, QPoint, QSize, QModelIndex)

# GUI FILE
from BaseGui import Ui_MainWindow

class DropdownModel(QtCore.QAbstractListModel):
    def __init__(self, *args,  dropdown=None, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.dropdown = dropdown or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.dropdown[index.row()]
            return text
        if role == Qt.DisplayRole:
            message = self.sub_dropdown[index.row()]
            return message
    
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

# class BookWindow(QtWidgets.QWidget):
#     def __init__(self, *args, **Kwargs):
#         super().__init__(*args, **Kwargs)

class BaseGuiWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        # IMPORT fUNCTIONS
        from ui_functions import UIFunctions

        super(BaseGuiWindow, self).__init__(*args, **kwargs)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(QSize(1000,795))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = DropdownModel()
        self.car_model = CarModel()
        self.ui.dropdown_menu.setModel(self.model)
        self.ui.dropdown_menu_2.setModel(self.car_model)
        self.show()

        self.ui.dropdown_menu.setStyleSheet("font-size:20px;\n"
        "color: white;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;\n"
        
        )
        self.ui.dropdown_menu_2.setStyleSheet("font-size:20px;\n"
        "color: white;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;\n"
        )
            
    
        # control all category button clicks to toggle slider
        self.ui.button_1.clicked.connect(lambda: UIFunctions.sub_content(self, "ECU Repair and Pinout", self.ui.button_1.text()))
        self.ui.button_2.clicked.connect(lambda: UIFunctions.immobilizer(self, 121, True))
        self.ui.button_3.clicked.connect(lambda: UIFunctions.sub_content(self, "Electronics", self.ui.button_3.text()))
        self.ui.button_4.clicked.connect(lambda: UIFunctions.sub_content(self, "Dashboard repair and reset", self.ui.button_4.text()))
        self.ui.button_5.clicked.connect(lambda: UIFunctions.sub_content(self, "Airbag", self.ui.button_5.text()))

        # Immobilizer button events
        self.ui.button_8.clicked.connect(lambda: UIFunctions.sub_content(self, "Immobilizer\Prog and decode", self.ui.button_8.text()))
        self.ui.button_6.clicked.connect(lambda: UIFunctions.sub_content(self, "Immobilizer\Pinout and wiring", self.ui.button_6.text()))
        self.ui.button_7.clicked.connect(lambda: UIFunctions.sub_content(self, "Immobilizer\EEPROM Location", self.ui.button_7.text()))


        # TOGGLE BUTTON ACTIVE
        # self.ui.button_1.clicked.connect(lambda: UIFunctions.toggle_active(self, "repair"))
        # self.ui.button_2.clicked.connect(lambda: UIFunctions.toggle_active(self, "immobi"))
        # self.ui.button_3.clicked.connect(lambda: UIFunctions.toggle_active(self, "pinout"))
        # self.ui.button_4.clicked.connect(lambda: UIFunctions.toggle_active(self, "panel"))
        # self.ui.button_5.clicked.connect(lambda: UIFunctions.toggle_active(self, "airbag"))

        self.ui.dropdown_menu.clicked.connect(self.check_indexes)
        self.ui.dropdown_menu_2.doubleClicked.connect(self.book_instance)
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def check_indexes(self, index):
        from ui_functions import UIFunctions
        self.car_model.dropdown = []
        self.car_model.layoutChanged.emit()
        if index:
            UIFunctions.check_books(self, index)
            self.car_model.layoutChanged.emit()
            print('selected item index found at %s with data: %s' %(index.row(), index.data()) )
    
    def book_instance(self, index):
        from ui_functions import UIFunctions
        if index:
            url = UIFunctions.book_url(self, index)
            QDesktopServices.openUrl(QUrl.fromLocalFile(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BaseGuiWindow()
    sys.exit(app.exec_())