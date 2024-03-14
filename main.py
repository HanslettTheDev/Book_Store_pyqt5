import sys

from PySide2.QtWidgets import QApplication
from user_interfaces.splash_screen import SplashScreen
from user_interfaces import logger

def main():
	''' Main application which loads every component and shows the GUI '''
	try:
		app = QApplication(sys.argv)
		logger.debug('Application started')
		import resources
		window = SplashScreen()
		window.show()
		sys.exit(app.exec_())
	except Exception as e:
		logger.critical("Application crashed. Below is why:", exc_info=True)
		sys.exit(1)

if __name__ == '__main__':
	main()