import os

dir = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(dir))

user = input(Enter Your Name: ")

whatsbot=open("WhatsBot.py","r")
lines = whatsbot.readlines()
lines[21] = "drivpath = '"+dir+"\chromedriver.exe')\n"
lines[22] = "username = '"+user+"'\n"

whatsbot = open("WhatsBot.py", "w")
whatsbot.writelines(lines)
whatsbot.close()


