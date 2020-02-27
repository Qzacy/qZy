#!/usr/bin/python3
# by Qzacy


import os, sys, datetime, getpass, re, requests, urllib, json, phonenumbers, smtplib, socket, dns.resolver
from phonenumbers import geocoder, carrier, timezone
from bs4 import BeautifulSoup
from time import sleep

user = getpass.getuser()
uos = os.uname().sysname
unode = os.uname().nodename
cdir = os.path.dirname(os.path.realpath(__file__))
current = open(cdir + "/setup/version.txt", "r")
current = current.readline(5)
dt = str(datetime.datetime.now()) + "\b\b\b\b\b\b\b"
hh = """
>>> Domains commands
sn                       Subnet Lookup
hd                       Get http-headers
os                       OS Detection (nmap)
op                       Open Ports (nmap)
tr                       Traceroute
dns                      DNS Lookup (A, AAAA, ALIAS, CNAME, MX, NS, SOA, PTR)
gip                      GeoIP (IP-API)
ms                       Mails Scraper
shot                     Screenshot

>>> Numbers commands
pl                       Python Scan (using phonenumbers lib)
nv                       Numverify Scan*
antd                     Antideo Scan
verp                     Veriphone Scan*

>>> Mails commands
ml                       Python Scan (using different libs)
xa                       WhoIsXMLAPI Scan*

>>> Setup
add [nv|verp|xa]         Add an API
checks                   Check the servers.
checka                   Check if the APIs exist.

>>> Utility
update
restart
clear
banner

credits
exit
'*' requires an API.
"""
banner = """
         _
qZy     |E] Coded by Qzacy,              *         
      .-|=====-. Running:        %s   |_Phone                       
      | | Mail | OS:             %s  (O)           
v%s|________| User:           %s     |#|                     
    ¯¯¯   ||            _                '-'
          ||           |-|  __                            
          ||           |=| [Ll] PC  
          ||           "^" ====`o
""" % (uos, unode, current, user)
cred = """
> Qzacy - qZy
Mail: qzacycoder@pm.me
Github: Qzacy


> Scott Brady - Python Mail Verification

Mail: scott@scottbrady91.com
Website: https://www.scottbrady91.com


> APIs used: 
WhoIsXMLAPI, Numverify, Veriphone, Antideo, IP-API.
(Links in README.md)
"""

def sel():
      try:
            cmd = input("[" + user + "]-[qZy] > ")
            cmd = cmd.lower()
            if cmd == "help" or cmd == "h":
                  sleep(0.3)
                  print(hh)
                  sel()
            elif cmd == "sn":
                  ws = input("Enter the domain: ")
                  if "." not in ws:
                        print("Error, enter a valid domain.")
                        sel()
                  ip = socket.gethostbyname(ws)
                  snet(ws, ip)
            elif cmd == "hd":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  ghd(ws, ip)
            elif cmd == "os":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  osd(ws, ip)
            elif cmd == "op":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  npscan(ws, ip)
            elif cmd == "tr":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  trace(ws, ip)
            elif cmd == "dns":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  dnsl(ws, ip)
            elif cmd == "gip":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  gipl(ws, ip)
            elif cmd == "shot":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  sshot(ws, ip)
            elif cmd == "ms":
                  ws = input("Enter the domain: ")
                  ip = socket.gethostbyname(ws)
                  msc(ws, ip)
            elif cmd == "pl":
                  unumber = input("Enter the complete phone number: ")
                  if not unumber.startswith("+"):
                        print("Error, enter a complete phone number. (using '+')")
                  if len(unumber) < 12:
                        print("Error, enter a valid phone number.")
                        sel()
                  plscan(unumber)
            elif cmd == "nv":
                  unumber = input("Enter the complete phone number: ")
                  if not unumber.startswith("+"):
                        print("Error, enter a complete phone number. (using '+')")
                  if len(unumber) < 12:
                        print("Error, enter a valid phone number.")
                        sel()
                  nvscan(unumber)
            elif cmd == "antd":
                  unumber = input("Enter the complete phone number: ")
                  if not unumber.startswith("+"):
                        print("Error, enter a complete phone number. (using '+')")
                  if len(unumber) < 12:
                        print("Error, enter a valid phone number.")
                        sel()
                  antdscan(unumber)
            elif cmd == "verp":
                  unumber = input("Enter the complete phone number: ")
                  if not unumber.startswith("+"):
                        print("Error, enter a complete phone number. (using '+')")
                        sel()
                  if len(unumber) < 12:
                        print("Error, enter a valid phone number.")
                        sel()
                  verpscan(unumber)
            elif cmd == "ml":
                  umail = input("Enter the email: ")
                  umail = umail.lower()
                  scheck = re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", umail)
                  if scheck == None:
                        print("Enter a valid email address.")
                        sel()
                  else:
                        mlscan(umail)  
            elif cmd == "xa":
                  umail = input("Enter the email: ")
                  umail = umail.lower()
                  scheck = re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", umail)
                  if scheck == None:
                        print("Enter a valid email address.")
                        sel()
                  else:
                        xascan(umail) 
            elif cmd == "add":
                  print("Error, this requires another value: [nv|verp|xa]")
                  sel()
            elif cmd == "add nv":
                  name = "numv"
                  add(name)
            elif cmd == "add verp":
                  name = "verp"
                  add(name)
            elif cmd == "add xa":
                  name = "xmlapi"
                  add(name)
            elif cmd == "checks":
                  checkservers()
            elif cmd == "checka":
                  checkapis()
            elif cmd == "update":
                  update()
            elif cmd == "restart":
                  restart()
            elif cmd == "clear":
                  os.system("clear")
                  sel()
            elif cmd == "banner":
                  print(banner)
                  sel()
            elif cmd == "credits":
                  os.system("clear")
                  print(cred)
                  sel()
            elif cmd == "exit":
                  print("\nQuitting...")
                  sleep(0.5)
                  sys.exit()
            else:
                  print("Please, enter a valid option.")
                  sel()
      except Exception as err:
            print("\nError: '" + str(err) + "',\nwrite me to fix the issue.\n\nPress [ENTER] to continue...")
            input()
            sel()
      except KeyboardInterrupt:
            print("\nFound: '^C', use 'exit' to close the script.")
            sel()

def restart():
      os.system("clear")
      print("Restarting...")
      sleep(0.5)
      os.system("clear && python3 " + cdir + "/qzy.py -r")

def update():
      print("\nChecking...")
      sleep(1.5)
      last = urllib.request.urlopen("https://raw.githubusercontent.com/Qzacy/qZy/master/setup/version.txt")
      last = str(last.read())
      last = "".join([char for char in last if char not in "b'\\n"])
      if current == last:
            print("[qZy] is up to date.\n")
            sel()
      else:
            print("[" + last + "] - New version available:\nhttps://github.com/Qzacy/qZy.git\n")
            sel()

def checkapis():
      print("\nChecking...")
      sleep(1.5)
      if os.stat(cdir + "/setup/nvapi.txt").st_size == 0:
            nvapi = "not found."
      else:
            nvapi = "found."
      if os.stat(cdir + "/setup/verpapi.txt").st_size == 0:
            verpapi = "not found."
      else:
            verpapi = "found."
      if os.stat(cdir + "/setup/xapi.txt").st_size == 0:
            xapi = "not found."
      else:
            xapi = "found."
      print("\n[Numverify API] " + nvapi)
      print("[Veriphone API] " + verpapi)
      print("[WhoIsXMLAPI API] " + xapi + "\n")
      sel()

def checkservers():
      print("\nChecking...")
      sleep(1.5)
      nvfile = open(cdir + "/setup/nvapi.txt", "r")
      nvkey = nvfile.readline() 
      verpfile = open(cdir + "/setup/verpapi.txt", "r")
      verpkey = verpfile.readline()
      xafile = open(cdir + "/setup/xapi.txt", "r")
      xakey = xafile.readline()
      nvr = requests.get("http://apilayer.net/api/validate?access_key=" + nvkey + "&number=+11111111111")
      nvstatus = nvr.status_code
      verpr = requests.get("https://api.veriphone.io/v2/verify?phone=+11111111111&key=" + verpkey)
      verpstatus = verpr.status_code
      xar = requests.get("https://emailverification.whoisxmlapi.com/api/v1?apiKey=" + xakey + "&emailAddress=support@whoisxmlapi.com")
      xastatus = xar.status_code
      print("\nNumverify response: " + str(nvstatus))
      print("Veriphone response: " + str(verpstatus))
      print("WhoIsXMLAPI response: " + str(xastatus) + "\n")
      sel()

def add(name):
      if name == "numv":
            f = cdir + "/setup/nvapi.txt" 
      elif name == "verp":
            f = cdir + "/setup/verpapi.txt"
      elif name == "xmlapi":
            f = cdir + "/setup/xapi.txt"
      key = input("Enter the key: ")
      if len(key) < 32:
            print("Error: 'Invalid key'.")
            add(name)
      try:
            if os.stat(f).st_size == 0:
                  print("Writing the file...")
            else:
                  print("Rewriting the file...") 
            f = open(f, "w")
            f.write(key)
            sleep(0.5)
            f.close()
            print("Successfully wrote.")
            sel()
      except Exception as err:
            print("Error: '" + str(err) + "' while writing the file,\ncheck 'README.md' to set the api_key manually.")
            sel()

def xascan(umail):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + umail + "]\nMode:   [WhoIsXMLAPI Scan]\n")
      sleep(0.5)
      api_file = open(cdir + "/setup/xapi.txt", "r")
      api_key = api_file.readline()
      r = requests.get("https://emailverification.whoisxmlapi.com/api/v1?apiKey=" + api_key + "&emailAddress=" + umail)
      data = r.json()
      if data["formatCheck"] == "false":
            data["formatCheck"] = "suspicious"
      else:
            data["formatCheck"] = "ok"
      print("Format: " + data["formatCheck"])
      print("SMTP: " + data["smtpCheck"])
      print("DNS: " + data["dnsCheck"])
      print("Free: " + data["freeCheck"])
      print("Disposable: " + data["disposableCheck"])
      print("MX Records: " + " ".join(data["mxRecords"]) + "\n")

      sel()

def mlscan(umail):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + umail + "]\nMode:   [Local Scan]\n")
      sleep(0.5)
      records = dns.resolver.query("emailhippo.com", "MX")
      record = str(records[0].exchange)
      host = socket.gethostname()
      server = smtplib.SMTP()
      server.set_debuglevel(0)
      server.connect(record)
      server.helo(host)
      server.mail("me@domain.com")
      code = server.rcpt(str(umail))
      server.quit()

      if 250 in code:
            print("Real: true")
            sel()
      else:
            print("Real: false")
            sel()
      
def verpscan(unumber):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + unumber + "]\nMode:   [Veriphone Scan]\n")
      sleep(0.5)
      api_file = open(cdir + "/setup/verpapi.txt", "r")
      api_key = api_file.readline()
      r = requests.get("https://api.veriphone.io/v2/verify?phone=" + unumber + "&key=" + api_key)
      data = r.json()

      print("\nInternational format: " + data["international_number"])
      print("Local format: " + data["local_number"])
      print("Country name: " + data["country"])
      print("Country prefix: " + data["country_prefix"])
      print("Country code: " + data["country_code"])
      print("Region: " + data["phone_region"])
      print("Carrier: " + data["carrier"])
      print("Line type: " + data["phone_type"] + "\n")
   
      sel()

def antdscan(unumber):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + unumber + "]\nMode:   [Antideo Scan]\n")
      sleep(0.5)
      r = requests.get("http://api.antideo.com/phone/" + unumber)
      data = r.json()

      print("\nInternational format: " + data["formats"]["international"])
      print("Local format: " + data["formats"]["national"])
      print("City: " + data["location"])
      print("Line type: " + data["type"])
      print("Timezone: " + ' '.join(data["timezones"]) + "\n")
  
      sel()

def nvscan(unumber):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + unumber + "]\nMode:   [Antideo Scan]\n")
      sleep(0.5)
      api_file = open(cdir + "/setup/nvapi.txt", "r")
      api_key = api_file.readline()
      r = requests.get("http://apilayer.net/api/validate?access_key=" + api_key + "&number=" + unumber)
      data = r.json()

      print("\nInternational format: " + data["international_format"])
      print("Local format: " + data["local_format"])
      print("Country name: " + data["country_name"])
      print("Country prefix: " + data["country_prefix"])
      print("Country code: " + data["country_code"])
      print("City: " + data["location"])
      print("Carrier: " + data["carrier"])
      print("Line type: " + data["line_type"] + "\n")
   
      sel()

def plscan(unumber):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + unumber + "]\nMode:   [Local Scan]\n")
      sleep(0.5)
      try:
            numberObj = phonenumbers.parse(unumber, None)
      except Exception as err:
          print("\n\nError: " + str(err))
          sel()
      else:
            if not phonenumbers.is_valid_number(numberObj):
                return False    
            iNum = phonenumbers.format_number(numberObj, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            cCode = phonenumbers.format_number(numberObj, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
            lNum = phonenumbers.format_number(numberObj, phonenumbers.PhoneNumberFormat.E164).replace(cCode, '')
            country = geocoder.country_name_for_number(numberObj, "en")
            city = geocoder.description_for_number(numberObj, "en")
            nCarrier = carrier.name_for_number(numberObj, "en")
            timezones = str(timezone.time_zones_for_number(numberObj))
            d = "'()"
            for char in d:
                  timezones = timezones.replace(char, "")
        
            print("\nInternational format: {}".format(iNum))
            print("Local format: {}".format(lNum))
            print("Country: {}".format(country))
            print("Country Code: {}".format(cCode))
            print("City: {}".format(city))
            print("Carrier: {}".format(nCarrier))
            print("Timezones: {}\n".format(timezones))

            sel()

def gipl(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [GeoIP Lookup]\n")
      sleep(0.5)
      r = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
      data = r.json()
      print("\nStatus: " + data["status"])
      if data["status"] == "fail":
          print("Error: '" + data["message"] + "'.")
          sel()
      print("Continent: " + data["continent"])
      print("Continent Code: " + data["continentCode"])
      print("Country: " + data["country"])
      print("Country Code: " + data["countryCode"])
      print("Region: " + data["region"])
      print("Region Name: " + data["regionName"])
      print("City: " + data["city"])
      print("District: " + data["district"])
      print("Zip: " + data["zip"])
      print("Latitude: " + str(data["lat"]))
      print("Longitude: " + str(data["lon"]))
      print("Timezone: " + data["timezone"])
      print("Currency: " + data["currency"])
      print("ISP: " + data["isp"])
      print("ORG: " + data["org"])
      print("AS: " + data["as"])
      print("AS Name: " + data["asname"])
      print("Reverse: " + data["reverse"])
      print("Mobile: " + str(data["mobile"]))
      print("Proxy: " + str(data["proxy"]) + "\n")

      sel()

def dnsl(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [DNS Lookup]\n")
      sleep(0.5)
      print("")
      os.system("dig +noall +answer " + ws + " A && dig +noall +answer " + ws + " AAAA && dig +noall +answer " + ws + " CNAME && dig +noall +answer " + ws + " MX && dig +noall +answer " + ws + " NS")
      print("")

      sel()

def trace(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [Traceroute]\n")
      sleep(0.5)
      print("")
      os.system("traceroute -m 10 " + ws)
      print("")

      sel()

def npscan(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [NMAP Port Scan]\n")
      sleep(0.5)
      print("")
      os.system("nmap --open " + ws)
      print("")

      sel()

def osd(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [OS Detection]\n")
      sleep(0.5)
      print("")
      os.system("echo %s|sudo nmap -sA -O --osscan-guess %s" % (passwd, ws))
      print("")

      sel()

def ghd(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [HTTP - Headers]\n")
      sleep(0.5)
      print("")
      os.system("curl -I " + ws)
      print("")

      sel()

def snet(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [Subnet Lookup]\n")
      sleep(0.5)
      r = requests.get("https://api.hackertarget.com/subnetcalc/?q=" + ws)
      data = r.text
      print(data + "\n")

      sel()

def sshot(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [Website Shot]\n")
      sleep(0.5)
      api_file = open(cdir + "/setup/xapi.txt", "r")
      api_key = api_file.readline()
      try:
            urllib.request.urlretrieve("https://website-screenshot-api.whoisxmlapi.com/api/v1?apiKey=" + api_key + "&url=" + ws + "&fullPage", cdir + "/wshots/" + ws + ".png")
            print("Saved in:\n" + cdir + "/wshots/" + ws + ".png\n")
            sel()
      except Exception as err:
            print("Error: '" + str(err) + "' while writing the image.")
            sel()

def msc(ws, ip):
      os.system("clear")
      print("Started - " + dt + "                              qZy - by Qzacy")
      print("Target: [" + ws + "] [" + ip + "]\nMode:   [Mails Scrape]\n")
      sleep(0.5)
      if "http://" not in ws:
            ws = "http://" + ws
      r = requests.get(ws)
      s = BeautifulSoup(r.text, "lxml")
      text = s.text
      mails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
      if not mails:
            print("Nothing found. Maybe the website has an email-protection.")
            sel()
      else:
            print("Mails:\n" + "\n".join(mails))
            sel()

if __name__ == "__main__":
      try:
            passwd = getpass.getpass()
      except Exception:
            print("\nEnter your sudo passwd.")
            sys.exit()
      if len(sys.argv) != 1:
            os.system("clear")
            print(banner)
            sel()
      else:
            os.system("clear")
            print("Starting...")
            sleep(0.5)
            os.system("clear")
            print(banner)
            sel()
