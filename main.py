import qrcode
import sys
import base64
from AesEverywhere import aes256
import os

# ------------ Functions -----------------

# Dictionary representing the morse code chart
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ',':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-', '&':'.-...',
					'=':'-...-', '+':'.-.-.', '@':'.--.-.',
					'_':'..--.-', '\'':'.-.-', '$':'...-..-',
					'!':'---.', '"':'.-..-.', ':':'---...',
					';':'-.-.-', '%':'...-.-', '|':'-...-',
					'#':'.-.-.-', '~':'..--.-', '`':'.-..-',
					'^':'...-.-', '&':'...-..-', '*':'.-.-.-',
					'\r':'', '\n':'', '\t':'' }

# Function to encrypt the string
# according to the morse code chart
def encryptMorse(message):
	cipher = ''
	for letter in message.upper():
		if letter != ' ':

			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

# Function to decrypt the string
# from morse to english
def decryptMorse(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

# morse to sound
def morse_to_sound(message):

    mixer.init()
    
    for letter in message:
        if letter == '.':
            mixer.music.load("morse-beep01.mp3")
            mixer.music.play()
            time.sleep(0.3)
        elif letter == '-':
            mixer.music.load("morse_beep02.mp3")
            mixer.music.play()
            time.sleep(0.3)
        else:
            time.sleep(0.5)


# Create qr code
def createQR(text, qr_file):
    qr = qrcode.QRCode( version=3 )
    qr.add_data(text.rstrip())
    qr.error_correction = qrcode.constants.ERROR_CORRECT_H
    qr.make(fit=True)

    # Create qr image
    img_qr = qr.make_image(fill_color="white", back_color="black")
    # Save qr image
    img_qr.save(qr_file)


# Execute shell command
def gpgCommand(text):
    # Execute gpg command
    command = "echo '" + text + "' | gpg --s2k-mode 3 --s2k-count 65011712 --s2k-digest-algo sha512 --cipher-algo AES256 --symmetric --armor > encrypted.txt"
    #print("Executing command: " + command)
    os.system(command)

def rm(files):
    # Execute gpg command
    command = " rm " + files + " encrypted.txt"
    #print("Executing command: " + command)
    os.system(command)




   













# ------------ Main -----------------
# ARGV
# 1: -f input txt file
# 2: -p password

argv = sys.argv

if argv[1] == "-f":
    file = argv[2]
    mode = "encrypt"
    if argv[3] == "-m":
        mode = "qr"
    

if mode == "encrypt":
    # Read input txt file
    with open(file, "r") as f:
        text = f.read()
    gpgCommand(text)

if mode == "qr":
    # Read input txt file
    with open("encrypted.txt", "r") as f:
        text = f.read()
    qr_file = file + ".png"
    createQR(text, qr_file)
    rm(file)

sys.exit()