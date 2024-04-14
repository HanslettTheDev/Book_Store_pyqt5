from zipfile import ZipFile
import time
import os

class DECOMPRESS:
	def __init__(self, app_name:str, name:str):
		self.name = name
		self.app_name = app_name
		try:
			self.zipfile = ZipFile(self.name)
		except FileNotFoundError:
			print(f"You need the \"{self.name}\" to decompile")
			input("")
			import sys
			sys.exit(1)
	def start_screen(self):
		print("==========================")
		print(self.app_name)
		print("==========================")
		time.sleep(2)
		print("")
		print("Developed By HanslettTheDev")
		print("Checking Archive for any error")
		try:
			ZipFile(self.name).testzip()
		except Exception as e:
			print("File may be corrupt or not found", e)
			input("Enter a key to exit: ")
		else:
			ZipFile(self.name).printdir()
			print("")
			print("Check Successful")

			print("Please wait until the process is completed")
			print("Archive will be deleted once completed")
			try:
				with ZipFile(self.name, 'r') as zipobj:
					filenames = zipobj.namelist()
					for filename in filenames:
						print("Decompressing file", filename)
						zipobj.extract(filename, os.path.join(os.environ['WINDIR'].split(':\\')[0] + ":\\", "ProgramData"))
					zipobj.close()
				print("Process Completed")
				os.remove(self.name)
				input("Enter a key to exit: ")
			except Exception as e:
				print("Something went wrong here", e)
				input("Press any Key and hit enter to exit: ")

if __name__ == '__main__':
	app_name = "EcuFixTronic Decompiler V2.0"
	name = "EcuFixTronic Files.zip"
	DECOMPRESS(app_name, name).start_screen()