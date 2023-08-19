import csv
import pywhatkit
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message(phoneNo: str, name: str):
    try:
        pywhatkit.sendwhatmsg_instantly(phoneNo,"Your message goes here. Use %s to represent the name or any other variable" % name,15,True,20)
        #15 is web.whatsapp.com 's max loading time under which it must load. You can change it based on your network speed.
        #20 is the time for which the page will stay put. Again, you can change it.
        #Numbers in csv should contain country code and should have no spaces.
        print("Message sent!")
    except Exception as e:
        print(str(e))


try:
    with open("Testing.csv", "r") as F:
        file = csv.reader(F)
        for line in file:
            send_whatsapp_message(line[0],line[1])

    # sending message
    print("Successfully Sent!")


except:
    print("An Unexpected Error!")
