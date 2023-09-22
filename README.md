# Cartronic Prog

Built with Python, PyQT and Qt Designer

Here are some of the project requirements you will need

### Requirement(s)
1. Catronic Files.zip
2. resources.py (This is optional as you can use the resources.qrc file to generate a new resource memory file)



### Installation Guide
After downloading the Cartronic files.zip, you can proceed with generating either the exe files or simply installing the packages to run it from the command line

1. Install the requirements.txt file
```cmd
make install
```

2. Decompile the Cartronic Files.zip using the decomp.py
**NOTE**: Ensure that the **decomp.py** or the **Cartronic Decompiler.exe** and the **Cartronic Files.zip** are in the same location else the process script won't work
```python
python decomp.py
```
or alternatively using the MakeFile Method and build the exe file
```cmd
make build-decomp
```

3. Download the Hardware ID Generator and run it to generate a hardware ID for your computer. Once Completed, Use the License Generator to generate a license valid only for your computer.
**NOTE**: Without the License Key, You won't be able to run the software


4. Run or Build from source
```cmd
python main.py
```
or 
```cmd
pyinstaller "Cartronic Prog.spec"
```

**BONUS**: You can use the MAKEFILE to run some shortcut commands and build automatically

- Install requirements, decompile and run
```cmd
make install-run
```

- Install requirements, decompile and build
```cmd
make install-build
```

**NOTE**: Check the build directory after running pyinstaller to see the executable file