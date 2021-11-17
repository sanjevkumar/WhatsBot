import os
import getpass

dir = os.getcwd()
dirnew = ""
for i in dir:
    if i == "\\":
        dirnew += "\\"
    dirnew += i
print(dirnew)

# Print the current working directory
print("Current working directory: {0}".format(dir))

user = input("Enter Your Name: ")
changepro = input("Do You Want To Change Profile[Y|N]: ")

whatsbot=open("WhatsBot.py","r")
lines = whatsbot.readlines()
lines[21] = "drivpath = '"+dirnew+"\chromedriver.exe'\n"
lines[22] = "username = '"+user+"'\n"

if changepro == "y" or changepro == "Y":
    prodir = input("Enter Your Profile Name(eg: Profile 1): ")
    sysusername = getpass.getuser()
    proloc = 'opt.add_argument("user-data-dir=C:\\Users\\'+sysusername+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+prodir+'")'
    lines[113] = proloc
elif changepro == "n" or changepro == "N":
    print('Using Default Profile "Chrome\\User Data"')
else:
    print("Invalid Entry")

whatsbot = open("WhatsBot.py", "w")
whatsbot.writelines(lines)
whatsbot.close()


