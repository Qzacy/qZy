import os, getpass

passwd = getpass.getpass()
to_install = []
if not os.path.isfile("/usr/bin/dig"):
    to_install.append("dig")
    print("[dig]            Not found.")
else:
    print("[dig]            Found.")
if not os.path.isfile("/usr/bin/whois"):
    to_install.append("whois")
    print("[whois]          Not found.")
else:
    print("[whois]          Found.")
if not os.path.isfile("/usr/bin/traceroute"):
    to_install.append("traceroute")
    print("[traceroute]     Not found.")
else:
    print("[traceroute]     Found.")
if not os.path.isfile("/usr/bin/nmap"):
    to_install.append("nmap")
    print("[nmap]           Not found.")
else:
    print("[nmap]           Found.")
if not os.path.isfile("/usr/bin/curl"):
    to_install.append("curl")
    print("[curl]           Not found.")
else:
    print("[curl]           Found.")
if not to_install:
    os.system("pip install -r requirements.txt")
    print("All requirements are installed.")
else:
    print("Installing all requirements...")
    os.system("echo %s|sudo -S apt-get install %s" % (passwd, " ".join(to_install)))
    os.system("pip3 install -r requirements.txt")
    print("All requirements are installed.")
