from generated_gui.tab_display import Ui_tab_display_window
from PySide2.QtWidgets import QWidget

class TabDisplay(QWidget):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(TabDisplay, self).__init__(*args, **kwargs)
        self.ui = Ui_tab_display_window()

        self.ui.setupUi(self)
        self.show()
