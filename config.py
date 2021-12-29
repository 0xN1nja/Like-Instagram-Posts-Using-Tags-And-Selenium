from csv import DictWriter
import os
import getpass

WELCOME_MESSAGE = '''
#    #    #   ####    #####    ##     ####   #####     ##    #    #
#    ##   #  #          #     #  #   #    #  #    #   #  #   ##  ##
#    # #  #   ####      #    #    #  #       #    #  #    #  # ## #
#    #  # #       #     #    ######  #  ###  #####   ######  #    #
#    #   ##  #    #     #    #    #  #    #  #   #   #    #  #    #
#    #    #   ####      #    #    #   ####   #    #  #    #  #    #


#####    ####    ####    #####
#    #  #    #  #          #
#    #  #    #   ####      #
#####   #    #       #     #
#       #    #  #    #     #
#        ####    ####      #


#        #    #    #  ######  #####
#        #    #   #   #       #    #
#        #    ####    #####   #    #
#        #    #  #    #       #####
#        #    #   #   #       #   #
######   #    #    #  ######  #    #
'''
print(WELCOME_MESSAGE)
username = input("Enter Your Instagram Username : ").lower()
if len(username) > 0:
    USERNAME = username
else:
    print("Invalid Username!")
    exit()
password = getpass.getpass("Enter Your Instagram Password : ")
if len(password) > 0:
    PASSWORD = password
else:
    print("Invalid Password!")
    exit()
tag = input("Enter Hashtag : ")
if len(tag) > 0:
    TAG = tag
else:
    print("Invalid Hashtag!")
    exit()
try:
    count = int(
        input(
            "Enter Post Like Count (WARNING : DON'T ENTER VALUE MORE THAN 100. YOU MAY LOSE ACCESS TO YOUR ACCOUNT) : "))
except:
    print("Post Like Count Must Be An Integer!")
    exit()
if len(str(count)) > 0:
    COUNT = count
else:
    print("Invalid Input!")
    exit()
chrome_driver_path = input(
    "Enter Chrome Driver Path (Download From https://chromedriver.chromium.org/ According To Your Chrome Version) : ")
if os.path.exists(chrome_driver_path):
    CHROME_DRIVER_PATH = chrome_driver_path
else:
    print("Invalid Chrome Driver Path!")
    exit()
if os.path.exists("config.csv"):
    overwrite = input("It Looks Like You've Already Configured The Bot. Do You Want To Overwrite? (Y/N) : ").lower()
    if overwrite == "y":
        with open("config.csv", "w", newline="") as f:
            writer = DictWriter(f, fieldnames=["username", "password", "tag", "count", "chrome_driver_path"])
            writer.writeheader()
            writer.writerow({
                "username": USERNAME,
                "password": PASSWORD,
                "tag": TAG,
                "count": COUNT,
                "chrome_driver_path": CHROME_DRIVER_PATH,
            })
    elif overwrite == "n":
        print("Abort")
        exit()
    else:
        print("Invalid Input!")
else:
    with open("config.csv", "w", newline="") as f:
        writer = DictWriter(f, fieldnames=["username", "password", "tag", "count", "chrome_driver_path"])
        writer.writeheader()
        writer.writerow({
            "username": USERNAME,
            "password": PASSWORD,
            "tag": TAG,
            "count": COUNT,
            "chrome_driver_path": CHROME_DRIVER_PATH,
        })
print("Done! Now Run bot.py")
