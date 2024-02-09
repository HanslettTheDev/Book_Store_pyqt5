# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_display.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tab_display_window(object):
    def setupUi(self, tab_display_window):
        if not tab_display_window.objectName():
            tab_display_window.setObjectName(u"tab_display_window")
        tab_display_window.resize(862, 466)
        tab_display_window.setMinimumSize(QSize(862, 466))
        self.verticalLayout = QVBoxLayout(tab_display_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_bar = QFrame(tab_display_window)
        self.window_bar.setObjectName(u"window_bar")
        self.window_bar.setMaximumSize(QSize(16777215, 40))
        self.window_bar.setStyleSheet(u"background-color: #4D77FF;\n"
"color: white;")
        self.window_bar.setFrameShape(QFrame.NoFrame)
        self.window_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.window_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.navbar = QFrame(self.window_bar)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 40))
        self.navbar.setMaximumSize(QSize(16777215, 40))
        self.navbar.setStyleSheet(u"background-color: #22577E;")
        self.navbar.setFrameShape(QFrame.NoFrame)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.navbar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_title_bar_top = QLabel(self.navbar)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setLayoutDirection(Qt.LeftToRight)
        self.label_title_bar_top.setStyleSheet(u"background: none;\n"
"margin-left: 5px;")
        self.label_title_bar_top.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_title_bar_top)

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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy)
        self.minimize_button.setToolTipDuration(2000)
        self.minimize_button.setStyleSheet(u"text-align: center;\n"
"margin-bottom: 2px;")

        self.horizontalLayout_9.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self.nav_buttons)
        self.maximize_button.setObjectName(u"maximize_button")
        sizePolicy.setHeightForWidth(self.maximize_button.sizePolicy().hasHeightForWidth())
        self.maximize_button.setSizePolicy(sizePolicy)
        self.maximize_button.setToolTipDuration(2000)
        self.maximize_button.setStyleSheet(u"text-align: center;\n"
"margin-bottom: 2px;")

        self.horizontalLayout_9.addWidget(self.maximize_button)

        self.close_button = QPushButton(self.nav_buttons)
        self.close_button.setObjectName(u"close_button")
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
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


        self.horizontalLayout_3.addWidget(self.nav_buttons)


        self.horizontalLayout_2.addWidget(self.navbar)


        self.verticalLayout.addWidget(self.window_bar)

        self.frame_center = QFrame(tab_display_window)
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
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.view = QFrame(self.frame_center)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(781, 350))
        self.view.setMaximumSize(QSize(16777215, 450))
        self.view.setStyleSheet(u"font-size: 20px;\n"
"")
        self.view.setFrameShape(QFrame.StyledPanel)
        self.view.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.view)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 9, -1)
        self.groupBox_3 = QGroupBox(self.view)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
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

        self.groupBox_2 = QGroupBox(self.view)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
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


        self.retranslateUi(tab_display_window)

        QMetaObject.connectSlotsByName(tab_display_window)
    # setupUi

    def retranslateUi(self, tab_display_window):
        tab_display_window.setWindowTitle(QCoreApplication.translate("tab_display_window", u"Form", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("tab_display_window", u"CarTronic PROG V2022.1", None))
#if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("tab_display_window", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_button.setToolTip(QCoreApplication.translate("tab_display_window", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("tab_display_window", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("tab_display_window", u"Car Brand", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("tab_display_window", u"Model", None))
    # retranslateUi

