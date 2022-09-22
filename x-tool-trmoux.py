# coded: by akash black hat
# date : 22/09/22
#time  : 09:12:36

import os


def menu():
    print("""
 ██████╗ ██╗ ██████╗     ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔════╝ ██║██╔═══██╗    ██║ ██╔╝██║████╗  ██║██╔════╝ 
██║  ███╗██║██║   ██║    █████╔╝ ██║██╔██╗ ██║██║  ███╗
██║   ██║██║██║   ██║    ██╔═██╗ ██║██║╚██╗██║██║   ██║
╚██████╔╝██║╚██████╔╝    ██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═════╝ ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
⚠️WARNING : I AM NOT RESPONSIBLE FOR THE MISUSE OF THIS TOOL !
         [😡]AIM FOR THE IMPOSSIBLE = GIO KING[😡]
* Author  : Akash Black Hat
* GitHub  : https://github.com/akashblackhat
* YouTub  : TECHNICAL AKASH SKILLS
* FacebooK: https://shorturl.at/MO019
* whatsapp: +91 8389020949       
* Gmail   : akashram8090as@gmail.com
* Created By= HCO_Team
----->
|This tool is available for Termux Only
---------->
==========================================
1. Install HCO-Bomber
2. Install HCO-Phisher
3. Install WaCrasher
4. Install metasploit-framework
5. Install Sherlock
6. Install slowloris
7. Install thc-hydra
8. Install Fsociety Toolkit
------------------------------------------
00. Exit
==========================================
""")


loop = True
while loop:
    menu()
    what = input("$: ")

    if what == "1":
        os.system("cd /data/data/com.termux/files/home && apt update -y && apt upgrade -y")
        os.system("pkg install git -y")
        os.system(
            "cd /data/data/com.termux/files/home && git clone https://github.com/Hackerscolonyofficial/HCO-Bomber.git")
        os.system("cd /data/data/com.termux/files/home && cd HCO-Bomber && chmod +x hco-bomber")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+)HCO-Bomber was successfuly installed :)")
        print("(+)To run HCO-Bomber type./hco-bomber ")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    if what == "2":
        os.system("apt update && apt upgrade -y")
        os.system(
            "cd /data/data/com.termux/files/home && git clone https://github.com/Hackerscolonyofficial/HCO-Phisher.git ")
        os.system(
            "cd /data/data/com.termux/files/home && cd HCO-Phisher && 𝗰𝗵𝗺𝗼𝗱 +𝘅 setup && 𝗯𝗮𝘀𝗵 𝘀𝗲𝘁𝘂𝗽* ")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+)HCo-Phisher was successfully installed :)")
        print("[+]𝗧𝘂𝗿𝗻 𝗼𝗻 𝘆𝗼𝘂𝗿 𝗠𝗼𝗯𝗶𝗹𝗲 𝗵𝗼𝘁𝘀𝗽𝗼𝘁 then  𝗵𝗰𝗼𝗽𝗵𝗶𝘀𝗵 Type  to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("apt update && apt upgrade -y")
        os.system("pkg install python git -y")
        os.system("pip install colorama")
        os.system(
            "cd /data/data/com.termux/files/home && git clone https://github.com/Hackerscolonyofficial/WaCrasher.git")
        os.system("cd /data/data/com.termux/files/home && cd WaCrasher && chmod +x WaCrash.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+) Wacrasher installed successfully :)")
        print("[+] Type python3 WaCrash.py to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    elif what == "4":
        os.system("apt update && apt upgrade -y")
        os.system("apt install wget")
        os.system(
            "cd /data/data/com.termux/files/home && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && chmod +x metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+) metasploit-framework was installed successfully :)")
        print("[+] Type msfconsole to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    elif what == "5":
        os.system("apt update && apt upgrade -y")
        os.system("pkg install python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sherlock-project/sherlock.git")
        os.system("cd /data/data/com.termux/files/home && cd sherlock && python3 -m pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+)Sherlock was installed successfully :)")
        print("[+] Type python3 sherlock --help to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    elif what == "6":
        os.system("apt update && apt upgrade -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/gkbrk/slowloris.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+)Slowloris was installed successfully :)")
        print("(+)Type slowloris.py to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("apt update && apt upgrade -y ")
        os.system("apt install python")
        os.system("apt install php ")
        os.system("apt install curl")
        os.system("apt install wget ")
        os.system("apt install nano")
        os.system("apt install git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/vanhauser-thc/thc-hydra")
        os.system("cd /data/data/com.termux/files/home && cd thc-hydra && ./configure && make && make install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("(+) hydra installed successfully :)")
        print("[+] Type ./hydra -h to run.")
        print("====================================")
        rmenu = input("(+) Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break


