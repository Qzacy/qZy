import os, getpass
from time import sleep

passwd = getpass.getpass()
to_install = []
if not os.path.isfile("/usr/bin/dig"):
    to_install.append("dig")
    sleep(0.5)
    print("[dig]            Not found.")
else:
    sleep(0.5)
    print("[dig]            Found.")
if not os.path.isfile("/usr/bin/whois"):
    to_install.append("whois")
    sleep(0.5)
    print("[whois]          Not found.")
else:
    sleep(0.5)
    print("[whois]          Found.")
if not os.path.isfile("/usr/bin/traceroute"):
    to_install.append("traceroute")
    sleep(0.5)
    print("[traceroute]     Not found.")
else:
    sleep(0.5)
    print("[traceroute]     Found.")
if not os.path.isfile("/usr/bin/nmap"):
    to_install.append("nmap")
    sleep(0.5)
    print("[nmap]           Not found.")
else:
    sleep(0.5)
    print("[nmap]           Found.")
if not os.path.isfile("/usr/bin/curl"):
    to_install.append("curl")
    sleep(0.5)
    print("[curl]           Not found.")
else:
    sleep(0.5)
    print("[curl]           Found.")
if not to_install:
    sleep(1)
    print("Installing Python3 requirements...")
    os.system("pip3 install -r requirements.txt")
    sleep(1)
    print("All requirements are installed.")
else:
    sleep(1)
    print("Installing System requirements...")
    os.system("echo %s|sudo -S apt-get install %s" % (passwd, " ".join(to_install)))
    sleep(1)
    print("Installing Python3 requirements...")
    os.system("pip3 install -r requirements.txt")
    sleep(1)
    print("All requirements are installed.")
