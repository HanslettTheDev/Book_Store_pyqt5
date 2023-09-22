from os.path import join
from PySide2.QtWidgets import QFileIconProvider
from PySide2.QtCore import QFileInfo
from PySide2.QtGui import QIcon

class FileIconProvider(QFileIconProvider):
	def icon(self, name):
		if isinstance(name, QFileInfo):
			info = name.baseName().lower()
			return QIcon(join(f":/icons/logo-{info}.png"))
		return super(FileIconProvider, self).icon(name)