from os.path import join
from PySide2.QtWidgets import QFileIconProvider
from PySide2.QtCore import QFileInfo
from PySide2.QtGui import QIcon

from config import Config


class FileIconProvider(QFileIconProvider):
	def icon(self, name):
		if isinstance(name, QFileInfo):
			info = name.baseName().lower()
			# Show an icon even when the name doesn't match
			if Config.ICON_UPDATES.get(info):
				return QIcon(join(f":/icons/logo-{Config.ICON_UPDATES.get(info)}.png"))
			# else just return the default icon	
			return QIcon(join(f":/icons/logo-{info}.png"))
		return super(FileIconProvider, self).icon(name)