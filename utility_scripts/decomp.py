from zipfile import ZipFile
from enigma.machine import EnigmaMachine
import time
import os

class DECOMPRESS:
	def __init__(self):
		self.zipfile = ZipFile("Cartronic Files.zip")

	def start_screen(self):
		print("==========================")
		print("Cartronic Decompressor V1.0")
		print("==========================")
		time.sleep(2)
		print("")
		print("Developed By HanslettTheDev")
		print("Checking Archive for any error")
		try:
			ZipFile('Cartronic Files.zip').testzip()
		except Exception as e:
			print("File may be corrupt or not found", e)
			input("Enter a key to exit: ")
		else:
			ZipFile("Cartronic Files.zip").printdir()
			print("")
			print("Check Successful")

			print("Please wait until the process is completed")
			print("Archive will be deleted once completed")
			try:
				with ZipFile('Cartronic Files.zip', 'r') as zipobj:
					filenames = zipobj.namelist()
					for filename in filenames:
						print("Decompressing file", filename)
						zipobj.extract(filename, os.path.join(os.environ['WINDIR'].split(':\\')[0] + ":\\", "ProgramData"))
					zipobj.close()
				print("Process Completed")
				os.remove("Cartronic Files.zip")
				input("Enter a key to exit: ")
			except Exception as e:
				print("Something went wrong here", e)
				input("Press any Key and hit enter to exit: ")

if __name__ == '__main__':
	DECOMPRESS().start_screen()