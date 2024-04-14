compile:
	pyinstaller "ecufixtronic.spec"

build-decomp:
	pyinstaller "decompiler.spec"

build-resources:
	pyside2-rcc resources.qrc -o resources.py

build-ui:
	pyside2-uic qt_ui_files/tab_display.ui -o tab_display.py
	pyside2-uic qt_ui_files/base.ui -o base_ui.py

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