import sys
import wmi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PyQt5.QtCore import (Qt, QPoint, QSize)

from PyQt5 import QtCore, QtGui, QtWidgets

from setup_gui import PromptWindow
from verify import verify

class SetupWindow(QMainWindow, PromptWindow):
    def __init__(self):
        super().__init__()
        self.ui = PromptWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(self.stylesheet())
        self.get_hardware_id()
        self.show()

        self.ui.confirm.clicked.connect(self.check_license)

    def get_hardware_id(self):
        # get the hardware id and rename the hardware label to the id gotten 
        # from the os
        c = wmi.WMI()
        hardware_id = []
        for item in c.Win32_PhysicalMedia():
            if item.SerialNumber != None:
                hardware_id.append(item.SerialNumber)
        self.ui.hardware_id_label.setText(hardware_id[0])

    def stylesheet(self):
        styles = '''
        Qlabel {
            font-size: 30px;
        }
        #hardware_id_label, #license_box {
            font-size: 20px;
        }
        #key_label, #id_label {
            font-size: 15px;
        }
        '''
        return styles
    
    def check_license(self):
        print("checking")
        key = self.ui.license_box.text()

        if verify(key):
            print("license verified")
        else: 
            print("license check failed")   



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SetupWindow()
    sys.exit(app.exec_())