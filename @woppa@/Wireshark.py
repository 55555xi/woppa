import logging
import hashlib
import os
import sys
from time import sleep
from keyauth import api
from bot.woppabot import WoppaBot
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
def print_colored_art():
    print(Colors.RED + "                     Discord:821.                       " + Colors.RESET)
    print(Colors.RED + "                     -------------                       " + Colors.RESET)
    print(Colors.MAGENTA + "                 ___====-_  _-====___" + Colors.RESET)
    print(Colors.MAGENTA + "           _--^^^#####//      \\#####^^^--_" + Colors.RESET)
    print(Colors.MAGENTA + "        _-^##########// (    ) \\##########^-_" + Colors.RESET)
    print(Colors.MAGENTA + "       -############//  |\\^^/|  \\############-" + Colors.RESET)
    print(Colors.MAGENTA + "     _/############//   (@::@)   \\############\\_" + Colors.RESET)
    print(Colors.MAGENTA + "    /#############((     \\\\//     ))#############\\" + Colors.RESET)
    print(Colors.MAGENTA + "   -###############\\\\    (oo)    //###############-" + Colors.RESET)
    print(Colors.MAGENTA + "  -#################\\\\  / VV \\  //#################-" + Colors.RESET)
    print(Colors.MAGENTA + " -###################\\\\/      \\/###################-" + Colors.RESET)
    print(Colors.MAGENTA + "_#/|##########/\\######(   /\\   )######/\\##########|\\#_" + Colors.RESET)
    print(Colors.MAGENTA + "|/ |#/\\#/\\#/\\/  \\#/\\##\\  |  |  /##/\\#/  \\/\\#/\\#/\\#| \\|" + Colors.RESET)
    print(Colors.MAGENTA + "`  |/  V  V  `   V  \\#\\| |  | |/#/  V   '  V  V  \\|  '" + Colors.RESET)
    print(Colors.MAGENTA + "   `   `  `      `   / | |  | | \\   '      '  '   '" + Colors.RESET)
    print(Colors.MAGENTA + "                    (  | |  | |  )" + Colors.RESET)
    print(Colors.MAGENTA + "                   __\\ | |  | | /__" + Colors.RESET)
    print(Colors.MAGENTA + "                  (vvv(VVV)(VVV)vvv)" + Colors.RESET)
def getchecksum():
    md5_hash = hashlib.md5()
    try:
        with open(sys.argv[0], "rb") as file:
            md5_hash.update(file.read())
    except FileNotFoundError:
        logging.error("File not found: %s", sys.argv[0])
        return ""
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name="woppa",  # Application Name
    ownerid="OCpqVmrZx0",  # Owner ID
    secret="4f8fc6c005696e4845666e5f39877df56ec8fd8fc25c1377ed5f116d7afa644d",  # Application Secret
    version="1.0",  # Application Version
    hash_to_check=getchecksum()
)
def answer():
    try:
        print("1-Wireshark")
        ans = input("Select Wireshark: ")
        if ans == "1":
            user = input('Wireshark u: ')
            password = input('Wireshark p: ')
            keyauthapp.login(user, password)
            print("\nWireshark: ")
            print("Wireshark: " + keyauthapp.user_data.username)
            print("IP address: " + keyauthapp.user_data.ip)
            print("Hardware-Id: " + keyauthapp.user_data.hwid)
            print(Colors.RED + "       " + Colors.RESET)
            print(Colors.MAGENTA + "      _,     ,_" + Colors.RESET)
            print(Colors.MAGENTA + "    .'/  ,_   \\'. " + Colors.RESET)
            print(Colors.MAGENTA + "   |  \\__( >__/  |" + Colors.RESET)
            print(Colors.MAGENTA + "   \\     821.    /" + Colors.RESET)
            print(Colors.MAGENTA + "    '-..__ __..-'" + Colors.RESET)
            print(Colors.MAGENTA + "         /_\\" + Colors.RESET)            
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_colored_art()
            bot = WoppaBot()
            bot.starter()
        else:
            print("\n")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            answer()
    except KeyboardInterrupt:
        logging.error("KeyboardInterrupt exception occurred")
        os._exit(1)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))
        raise
if __name__ == "__main__":
    try:
        print_colored_art()
        answer()
    except Exception as e:
        logging.error("Failed to start the application: %s", str(e))
