from PIL import Image
import pytesseract
import pyautogui
import os
import time


def auto_shutdown():
	# This function automatically shutdowns the computer if the game from steam has finished downloading

	# make the ss object
	ss = pyautogui.screenshot()

	# area for half the screen we need
	area = (round(x / 2), 0, x, y)
	ss_croped = Image.Image.crop(ss, area)

	if debug is True:
		ss_croped.save(directory + r"\outCroped.png")
		ss.save(directory + r"\out.png")

	# convert the ss object into string
	string = pytesseract.image_to_string(ss_croped)
	if debug is True:
		print(string)

	# check if the required text is in the string

	if 'Play' in string:
		if debug is True:
			print("Program works!!")

		else:
			os.system('shutdown -s')

	# if not call the function it self after 5 minutes
	else:
		time.sleep(300)
		auto_shutdown()
	if debug is True:
		input("DEBUG COMPLETED. PRESS ENTER TO CONTINUE...")


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# taking input the from user
x, y = input("Enter your reslotion in this format *1366x768*: ").split('x')

while True:
	try:
		time_in_min = float(input("Enter the estimated time (in minutes) left for the game to be downloaded: "))
		break
	except TypeError:
		print("Wrong input. Please input an integer (in minutes):")

x = int(x) - 1
y = int(y) - 1

time_in_sec = time_in_min * 60

debug = False

if time_in_min == 696969:
	debug = True
	print("NOW IN DEBUG MODE!!!")
	directory = input(r'Directory in which you want to save the debugged screenshots like **D:\anyfolder**: ')
	time_in_sec = float(input("Enter the time in seconds: "))

time.sleep(time_in_sec)
auto_shutdown()
