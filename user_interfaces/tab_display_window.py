from PySide2.QtGui import QStandardItemModel
from PySide2.QtCore import QDir
from PySide2.QtWidgets import QFileSystemModel, QAbstractItemView
from PySide2.QtWidgets import QWidget

# Module Imports
from user_interfaces.utils import FileIconProvider
from generated_gui.tab_display import Ui_tab_display_window

class TabDisplay(QWidget):
	def __init__(self, *args, obj=None, **kwargs) -> None:
		super(TabDisplay, self).__init__(*args, **kwargs)
		self.ui = Ui_tab_display_window()
		self.model = QFileSystemModel()
		self.model.setIconProvider(FileIconProvider())
		self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
		self.car_model = QStandardItemModel()
		self.ui.setupUi(self)

		# set models for QTreeView and QListView
		self.ui.dropdown_tree.setModel(self.model)
		self.ui.dropdown_menu.setModel(self.car_model)

		# Create link object for tree view
		self.ui.dropdown_tree.setHeaderHidden(True)
		
		self.ui.dropdown_menu.setSpacing(2)
		self.ui.dropdown_tree.setStyleSheet('''font-size: 20px;
		font-weight: bold;
		''')

		self.ui.dropdown_tree.setColumnWidth(0,250)
		self.ui.dropdown_tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

		self.ui.dropdown_tree.setAlternatingRowColors(True)
		# Hide the file type, folder size and date created columns
		self.ui.dropdown_tree.hideColumn(1)
		self.ui.dropdown_tree.hideColumn(2)
		self.ui.dropdown_tree.hideColumn(3)

		# Add a background image
		self.ui.frame_center.setStyleSheet('''#frame_center {
		background-image: url(\':/others/bg1.jpeg\');
		}
		''')
		# self.show()