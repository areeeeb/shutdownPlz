from PIL import Image
import pytesseract, pyautogui, os, threading, time,  sched

def autoShutdown():
    '''This function automatically shutdowns the computer if the
        game from steam has finished downloading'''

    #make the ss object
    ss = pyautogui.screenshot()

    #area for half the screen we need
    area = (round(x/2), 0, x, y)
    ssCroped = Image.Image.crop(ss, area)

    if debug == True:
        ssCroped.save(directory + r"\outCroped.png")
        ss.save(directory + r"\out.png")

    #convert the ss object into string
    string = pytesseract.image_to_string(ssCroped)
    if debug == True:
        print(string)

    #check if the required text is in the string

    if 'Play' in string:
        if debug == True:
            print("Program works!!")

        else:
            os.system('shutdown -s')

    #if not call the function it self after 5 minutes
    else:
        time.sleep(300)
        autoShutdown()
    if debug == True:
        input("DEBUG COMPLETED. PRESS ENTER TO CONTINUE...")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


#taking input the from user
while True:
    try:
        x, y = input("Enter your reslotion in this format *1366x768*: ").split('x')
        break
    except:
        print("Wrong input! please enter your resolution in required format..")

while True:
    try:
        timeInMinutes = float(input("Enter the estimated time (in minutes) left for the game to be downloaded: "))
        break
    except:
        print("Wrong input. Please input an integer (in minutes):")



x = int(x) - 1
y = int(y) - 1

timeInSec = timeInMinutes * 60

debug = False

if timeInMinutes == 696969:
    debug = True
    print("NOW IN DEBUG MODE!!!")
    directory = input(r'Input the directory path in which you want to save the debugged screenshots like **D:\anyfolder**: ')
    timeInSec = float(input("Enter the time in seconds: "))

time.sleep(timeInSec)
autoShutdown()

