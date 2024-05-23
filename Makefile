compile:
	pyinstaller "ecufixtronic.spec" -y

build-decomp:
	pyinstaller "decompiler.spec"

build-resources:
	pyside2-rcc resources.qrc -o resources.py

build-ui:
	pyside2-uic qt_ui_files/tab_display.ui -o generated_gui/tab_display.py
	pyside2-uic qt_ui_files/base.ui -o generated_gui/gui.py
	del base_ui.py tab_display.py

install:
	pip install -r requirements.txt

decomp:
	python ./utility_scripts/decomp.py

run-decomp:
	./"Catronic Decompiler.exe"

run:
	python main.py

launch: install, run 

install-build: install, build-decomp, run-decomp, build, launch