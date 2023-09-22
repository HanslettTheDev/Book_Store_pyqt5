# access command line arguments
import os
import shutil

from PySide2 import QtCore, QtWebEngineWidgets
from PySide2.QtGui import QIcon

from user_interfaces import TempPath, PDFJS


class PDFWindow(QtWebEngineWidgets.QWebEngineView):
	def __init__(self):
		super(PDFWindow, self).__init__()
		self.setWindowTitle("Cartronic Prog Viewer")
		self.setWindowIcon(QIcon(os.path.join(":/tab_icons/logo.jpg")))

	def load_pdf(self, filename):
		try:
			shutil.move(filename, TempPath)
			url = QtCore.QUrl.fromLocalFile(os.path.join(TempPath, filename.split("\\")[-1])).toString()
		except shutil.Error:
			url = QtCore.QUrl.fromLocalFile(os.path.join(TempPath, filename.split("\\")[-1])).toString()
		self.load(QtCore.QUrl.fromUserInput("%s?file=%s" % (PDFJS, url)))

	def sizeHint(self):
		return QtCore.QSize(640, 480)
