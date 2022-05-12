import pyAesCrypt
from enigma.machine import EnigmaMachine
import tempfile
import os

class DECRYPT_FILES:
	def __init__(self, path) -> None:
		self.file_path = path
		self.password = "iamadeveloper catronicprog venomraidershanslett thedev6413v1 point1"
		self.epassword = self.enigma_machine()
		self.bufferSize = 64 * 1024
		
	def enigma_machine(self):
		machine = EnigmaMachine.from_key_sheet(
			rotors='II IV V',
			reflector='B',
			ring_settings=[23, 19, 7],
			plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')
		# set machine initial starting position
		machine.set_display('UPG')
		# decrypt the message key
		msg_key = machine.process_text('GRX')
		# decrypt the cipher text with the unencrypted message key
		msg_key = machine.set_display(msg_key)
		c = machine.process_text(self.password, replace_char='Z')
		return c
	
	def decrypt_pdf(self):
		password = self.epassword
		encFileSize = os.stat(self.file_path).st_size
		if self.file_path.endswith(".aes"):
			with open(self.file_path, "rb") as fIn:
				try:
					with tempfile.NamedTemporaryFile("wb", delete=False) as fOut:
						# decrypt file stream
						pyAesCrypt.decryptStream(fIn, fOut, password, self.bufferSize, encFileSize)
					return fOut.name
				except ValueError:
					return False
					# remove output file on error
					# os.remove(fOut.name)
# main = DECRYPT_FILES("E:\\Software Development\\Book store\\320i - Bosch -0285 010 070 -95640.pdf").decrypt_pdf()
