import sys
import webbrowser

from PySide6.QtWidgets import QApplication, QMainWindow

from setup_gui import PromptWindow

class SetupWindow(QMainWindow, PromptWindow):
	def __init__(self):
		super().__init__()
		self.ui = PromptWindow()
		self.ui.setupUi(self)
		self.show()

		self.ui.close_button.clicked.connect(lambda: self.close())
	
	def close_window(self):
		webbrowser.open("https://wa.me/c/237676634413")
		self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = SetupWindow()
	sys.exit(app.exec())