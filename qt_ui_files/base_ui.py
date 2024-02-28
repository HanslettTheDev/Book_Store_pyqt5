# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1376, 658)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy)
        self.frame_main.setStyleSheet(u"#frame_main {\n"
"border: 1px solid #22577E;\n"
"}")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_bar = QFrame(self.frame_main)
        self.window_bar.setObjectName(u"window_bar")
        self.window_bar.setMaximumSize(QSize(16777215, 40))
        self.window_bar.setStyleSheet(u"background-color: #4D77FF;\n"
"color: white;")
        self.window_bar.setFrameShape(QFrame.NoFrame)
        self.window_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.window_bar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.navbar = QFrame(self.window_bar)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 40))
        self.navbar.setMaximumSize(QSize(16777215, 40))
        self.navbar.setStyleSheet(u"background-color: #22577E;")
        self.navbar.setFrameShape(QFrame.NoFrame)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.navbar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.nav_title = QFrame(self.navbar)
        self.nav_title.setObjectName(u"nav_title")
        self.nav_title.setMinimumSize(QSize(0, 0))
        self.nav_title.setStyleSheet(u"")
        self.nav_title.setFrameShape(QFrame.NoFrame)
        self.nav_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.nav_title)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.label_title_bar_top = QLabel(self.nav_title)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"background: none;\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.nav_title)

        self.nav_buttons = QFrame(self.navbar)
        self.nav_buttons.setObjectName(u"nav_buttons")
        self.nav_buttons.setMaximumSize(QSize(120, 16777215))
        self.nav_buttons.setStyleSheet(u"QPushButton {\n"
"background-position: left center;\n"
"}\n"
"\n"
"#minimize_button:hover, #maximize_button:hover {\n"
"background-color: rgb(44, 49, 60);\n"
"}\n"
"\n"
"#close_button:hover {\n"
"color: #F7E2E2;\n"
"}")
        self.nav_buttons.setFrameShape(QFrame.NoFrame)
        self.nav_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.nav_buttons)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.nav_buttons)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy1)
        self.minimize_button.setToolTipDuration(2000)
        self.minimize_button.setStyleSheet(u"text-align: center;\n"
"margin-bottom: 2px;")

        self.horizontalLayout_9.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self.nav_buttons)
        self.maximize_button.setObjectName(u"maximize_button")
        sizePolicy1.setHeightForWidth(self.maximize_button.sizePolicy().hasHeightForWidth())
        self.maximize_button.setSizePolicy(sizePolicy1)
        self.maximize_button.setToolTipDuration(2000)
        self.maximize_button.setStyleSheet(u"text-align: center;\n"
"margin-bottom: 2px;")

        self.horizontalLayout_9.addWidget(self.maximize_button)

        self.close_button = QPushButton(self.nav_buttons)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setToolTipDuration(2000)
        self.close_button.setStyleSheet(u"#close_button {\n"
"text-align: center;\n"
"margin-bottom: 2px;\n"
"background-color: rgb(255, 52, 55);\n"
"}\n"
"\n"
"#close_button:hover {\n"
"background-color: #F7E2E2;\n"
"}")

        self.horizontalLayout_9.addWidget(self.close_button)


        self.horizontalLayout_8.addWidget(self.nav_buttons)


        self.verticalLayout_5.addWidget(self.navbar)


        self.verticalLayout.addWidget(self.window_bar)

        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 50))
        self.frame_top.setMaximumSize(QSize(16777215, 100))
        self.frame_top.setStyleSheet(u"#frame_top {\n"
"color: white;\n"
"background: #1c242c;\n"
"}\n"
"QPushButton {\n"
"background-color: white;\n"
"font-size: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #F0E5CF;\n"
"}\n"
"QLabel {\n"
"color: white;\n"
"font-size: 12px;\n"
"}")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_top)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(30, 9, 90, -1)
        self.button_14 = QPushButton(self.frame_6)
        self.button_14.setObjectName(u"button_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_14.sizePolicy().hasHeightForWidth())
        self.button_14.setSizePolicy(sizePolicy2)
        self.button_14.setMinimumSize(QSize(0, 0))
        self.button_14.setMaximumSize(QSize(16777215, 16777215))
        self.button_14.setToolTipDuration(2000)
        self.button_14.setCheckable(True)
        self.button_14.setChecked(False)
        self.button_14.setFlat(False)

        self.verticalLayout_7.addWidget(self.button_14)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_top)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(30, 9, 90, -1)
        self.button_11 = QPushButton(self.frame_7)
        self.button_11.setObjectName(u"button_11")
        sizePolicy2.setHeightForWidth(self.button_11.sizePolicy().hasHeightForWidth())
        self.button_11.setSizePolicy(sizePolicy2)
        self.button_11.setMinimumSize(QSize(0, 0))
        self.button_11.setMaximumSize(QSize(16777215, 16777215))
        self.button_11.setToolTipDuration(2000)
        self.button_11.setCheckable(True)
        self.button_11.setChecked(False)
        self.button_11.setFlat(False)

        self.verticalLayout_8.addWidget(self.button_11)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_top)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(30, 9, 90, -1)
        self.button_16 = QPushButton(self.frame_8)
        self.button_16.setObjectName(u"button_16")
        sizePolicy2.setHeightForWidth(self.button_16.sizePolicy().hasHeightForWidth())
        self.button_16.setSizePolicy(sizePolicy2)
        self.button_16.setMinimumSize(QSize(0, 0))
        self.button_16.setMaximumSize(QSize(16777215, 16777215))
        self.button_16.setToolTipDuration(2000)
        self.button_16.setCheckable(True)
        self.button_16.setChecked(False)
        self.button_16.setFlat(False)

        self.verticalLayout_9.addWidget(self.button_16)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_top)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(30, 9, 90, -1)
        self.button_9 = QPushButton(self.frame_11)
        self.button_9.setObjectName(u"button_9")
        sizePolicy2.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy2)
        self.button_9.setMinimumSize(QSize(0, 0))
        self.button_9.setMaximumSize(QSize(16777215, 16777215))
        self.button_9.setToolTipDuration(2000)
        self.button_9.setCheckable(True)
        self.button_9.setChecked(False)
        self.button_9.setFlat(False)

        self.verticalLayout_13.addWidget(self.button_9)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_top)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(30, 9, 90, -1)
        self.button_17 = QPushButton(self.frame_12)
        self.button_17.setObjectName(u"button_17")
        sizePolicy2.setHeightForWidth(self.button_17.sizePolicy().hasHeightForWidth())
        self.button_17.setSizePolicy(sizePolicy2)
        self.button_17.setMinimumSize(QSize(0, 0))
        self.button_17.setMaximumSize(QSize(16777215, 16777215))
        self.button_17.setToolTipDuration(2000)
        self.button_17.setCheckable(True)
        self.button_17.setChecked(False)
        self.button_17.setFlat(False)

        self.verticalLayout_14.addWidget(self.button_17)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frame_top)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(30, 9, 90, -1)
        self.button_10 = QPushButton(self.frame_10)
        self.button_10.setObjectName(u"button_10")
        sizePolicy2.setHeightForWidth(self.button_10.sizePolicy().hasHeightForWidth())
        self.button_10.setSizePolicy(sizePolicy2)
        self.button_10.setMinimumSize(QSize(0, 0))
        self.button_10.setMaximumSize(QSize(16777215, 16777215))
        self.button_10.setToolTipDuration(2000)
        self.button_10.setCheckable(True)
        self.button_10.setChecked(False)
        self.button_10.setFlat(False)

        self.verticalLayout_12.addWidget(self.button_10)

        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_12.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"#frame_center {\n"
"background-color: #D1D1D1;\n"
"}\n"
"QListView {\n"
"background-color: white;\n"
"}\n"
"#view, #groupBox_2, #groupBox_3 {\n"
"background-color: #D1D1D1;\n"
"}")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_center)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.view = QFrame(self.frame_center)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(0, 350))
        self.view.setMaximumSize(QSize(16777215, 450))
        self.view.setStyleSheet(u"font-size: 20px;\n"
"")
        self.view.setFrameShape(QFrame.StyledPanel)
        self.view.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.view)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.view)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 500))
        self.groupBox_3.setStyleSheet(u"#groupBox_3 {\n"
"border: 2px solid #EFEFEF;\n"
"background-color: #D1D1D1;\n"
"border-radius: 10px;\n"
"}")
        self.groupBox_3.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.dropdown_tree = QTreeView(self.groupBox_3)
        self.dropdown_tree.setObjectName(u"dropdown_tree")
        self.dropdown_tree.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.dropdown_tree)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.frame_3 = QFrame(self.view)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setMaximumSize(QSize(100, 480))
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"background-color: grey;\n"
"color: white;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_3)

        self.groupBox_2 = QGroupBox(self.view)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 500))
        self.groupBox_2.setStyleSheet(u"#groupBox_2 {\n"
"border: 2px solid #EFEFEF;\n"
"background-color: #D1D1D1;\n"
"border-radius: 10px;\n"
"}")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(100)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, 9, -1)
        self.dropdown_menu = QListView(self.groupBox_2)
        self.dropdown_menu.setObjectName(u"dropdown_menu")

        self.verticalLayout_2.addWidget(self.dropdown_menu)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_4.addWidget(self.view)


        self.verticalLayout.addWidget(self.frame_center)

        self.footer = QFrame(self.frame_main)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 70))
        self.footer.setMaximumSize(QSize(16777215, 70))
        self.footer.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 249, 250);\n"
"font-size: 15px;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(50, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.logo_button = QPushButton(self.frame_2)
        self.logo_button.setObjectName(u"logo_button")
        sizePolicy1.setHeightForWidth(self.logo_button.sizePolicy().hasHeightForWidth())
        self.logo_button.setSizePolicy(sizePolicy1)
        self.logo_button.setStyleSheet(u"border: none;")
        self.logo_button.setIconSize(QSize(50, 55))

        self.verticalLayout_16.addWidget(self.logo_button)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.label_3 = QLabel(self.footer)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMargin(4)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.whatsapp_button = QPushButton(self.footer)
        self.whatsapp_button.setObjectName(u"whatsapp_button")
        self.whatsapp_button.setMinimumSize(QSize(0, 30))
        self.whatsapp_button.setMaximumSize(QSize(150, 16777215))
        self.whatsapp_button.setStyleSheet(u"background-color: gray;")

        self.horizontalLayout_5.addWidget(self.whatsapp_button)

        self.gmail_button = QPushButton(self.footer)
        self.gmail_button.setObjectName(u"gmail_button")
        self.gmail_button.setMinimumSize(QSize(0, 30))
        self.gmail_button.setMaximumSize(QSize(150, 16777215))
        self.gmail_button.setStyleSheet(u"background-color: gray;")

        self.horizontalLayout_5.addWidget(self.gmail_button)

        self.book_status = QLabel(self.footer)
        self.book_status.setObjectName(u"book_status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.book_status.sizePolicy().hasHeightForWidth())
        self.book_status.setSizePolicy(sizePolicy3)
        self.book_status.setMinimumSize(QSize(0, 0))
        self.book_status.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.book_status, 0, Qt.AlignRight)

        self.message = QLabel(self.footer)
        self.message.setObjectName(u"message")
        self.message.setFocusPolicy(Qt.StrongFocus)
        self.message.setStyleSheet(u"color: #49FF00;")

        self.horizontalLayout_5.addWidget(self.message)

        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(45, 40))
        self.label_2.setMargin(5)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(20, 20))
        self.size_grip.setMaximumSize(QSize(20, 20))
        self.size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.size_grip.setFrameShape(QFrame.NoFrame)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout_2.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"CarTronic PROG V2022.1", None))
#if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_button.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
#if QT_CONFIG(tooltip)
        self.button_14.setToolTip(QCoreApplication.translate("MainWindow", u"ECU Repair|Pinout", None))
#endif // QT_CONFIG(tooltip)
        self.button_14.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ECU Repair|Pinout", None))
#if QT_CONFIG(tooltip)
        self.button_11.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard Repair and Reset", None))
#endif // QT_CONFIG(tooltip)
        self.button_11.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dashboard Repair|Reset", None))
#if QT_CONFIG(tooltip)
        self.button_16.setToolTip(QCoreApplication.translate("MainWindow", u"ECU Troubleshooting", None))
#endif // QT_CONFIG(tooltip)
        self.button_16.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ECU Troubleshooting", None))
#if QT_CONFIG(tooltip)
        self.button_9.setToolTip(QCoreApplication.translate("MainWindow", u"Electronics", None))
#endif // QT_CONFIG(tooltip)
        self.button_9.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Electronics", None))
#if QT_CONFIG(tooltip)
        self.button_17.setToolTip(QCoreApplication.translate("MainWindow", u"ECU Datasheet", None))
#endif // QT_CONFIG(tooltip)
        self.button_17.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ECU Datasheet", None))
#if QT_CONFIG(tooltip)
        self.button_10.setToolTip(QCoreApplication.translate("MainWindow", u"Immobilizer EEPROM Location", None))
#endif // QT_CONFIG(tooltip)
        self.button_10.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IMMO EEPROM Location", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Car Brand", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Model", None))
        self.logo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9\ufe0f 2024 Powered by LockSmith Inos Mechatronics services. All rights reserved", None))
#if QT_CONFIG(accessibility)
        self.whatsapp_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.whatsapp_button.setText(QCoreApplication.translate("MainWindow", u"+237 676634413", None))
#if QT_CONFIG(accessibility)
        self.gmail_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.gmail_button.setText(QCoreApplication.translate("MainWindow", u"clivcb56@gmail.com", None))
        self.book_status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.message.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"V1.5", None))
    # retranslateUi

