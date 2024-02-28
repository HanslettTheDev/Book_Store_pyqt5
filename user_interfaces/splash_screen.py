# access command line arguments
import os 
import time
import wmi 

from PySide2.QtWidgets import (QMainWindow, QGraphicsDropShadowEffect)
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QColor
from config import Config

from setup import SetupWindow
from user_interfaces import verify

# STYLESHEET FILE
from stylesheet import STYLES

from user_interfaces.home_window import BaseGuiWindow
from qt_ui_files.ui_splash_screen import Ui_SplashScreen

# GLOBALS
counter = 0
jumper = 10

class SplashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_SplashScreen()
		self.ui.setupUi(self)

		## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
		self.progressBarValue(0)

		## ==> REMOVE STANDARD TITLE BAR
		self.setWindowFlags(Qt.FramelessWindowHint) # Remove title bar
		self.setAttribute(Qt.WA_TranslucentBackground) # Set background to transparent

		## ==> APPLY DROP SHADOW EFFECT
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 120))
		self.ui.circularBg.setGraphicsEffect(self.shadow)

		## QTIMER ==> START
		self.timer = QTimer()
		self.timer.timeout.connect(self.progress)
		# TIMER IN MILLISECONDS
		self.timer.start(15)

		## SHOW ==> MAIN WINDOW
		########################################################################
		self.show()
		## ==> END ##

	def progress(self):
		global counter
		global jumper
		value = counter

		# HTML TEXT PERCENTAGE
		htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

		# REPLACE VALUE
		newHtml = htmlText.replace("{VALUE}", str(jumper))

		if(value > jumper):
			# APPLY NEW PERCENTAGE TEXT
			self.ui.labelPercentage.setText(newHtml)
			jumper += 2

		# SET VALUE TO PROGRESS BAR
		# fix max value error if > than 100
		if value >= 100: value = 1.000
		self.progressBarValue(value)

		# CLOSE SPLASH SCREE AND OPEN APP
		if counter > 100:
			# STOP TIMER
			self.timer.stop()

			# SHOW MAIN WINDOW
			self.main_app = self.verify_license()
			self.main_app.show()

			# CLOSE SPLASH SCREEN
			self.close()

		# INCREASE COUNTER
		counter += 0.5

	def progressBarValue(self, value):

		# PROGRESSBAR STYLESHEET BASE
		styleSheet = """
		QFrame{
			border-radius: 150px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
		}
		"""

		# GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
		# stop works of 1.000 to 0.000
		progress = (100 - value) / 100.0

		# GET NEW VALUES
		stop_1 = str(progress - 0.001)
		stop_2 = str(progress)

		# SET VALUES TO NEW STYLESHEET
		newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

		# APPLY STYLESHEET WITH NEW VALUES
		self.ui.circularProgress.setStyleSheet(newStylesheet)

	def verify_license(self):
		DIR_PATH = os.getenv('LOCALAPPDATA')
		FILE = "yagamie.key"
		if os.path.isfile(os.path.join(DIR_PATH, FILE)):
			with open(os.path.join(DIR_PATH, FILE), "r") as f:
				key = f.readline()
			chars = key.split("+=")
			key_id = chars[0]
			key_address = chars[1]
			blob = self.get_hardware_id()
			
			if (blob == key_id) and verify(key_address):
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
		return hardware_id[0].strip(" ")
