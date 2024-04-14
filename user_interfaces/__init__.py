import os

from PySide2.QtCore import QUrl

from config import Config


TempPath = os.path.join(os.environ['WINDIR'].split(':\\')[0] + ":\\", Config.PARENT_TEMP_LOCATION, Config.TEMP_LOCATION)
PDFJS = QUrl.fromLocalFile(os.path.join(TempPath, Config.PDFJS_VIEWER_PATH)).toString()