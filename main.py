import logging
import sys

from PySide2.QtWidgets import QApplication
from user_interfaces.splash_screen import SplashScreen

def main():
	''' Main application which loads every component and shows the GUI '''
	logging.basicConfig(filename='cartronic_log.log', level=logging.DEBUG, filemode="w", format='%(asctime)s: %(lineno)d: %(funcName)s: %(levelname)s: %(message)s')
	logger = logging.getLogger(__name__)

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