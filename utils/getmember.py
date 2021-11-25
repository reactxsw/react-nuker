import discum
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--channel', type=str, required=True)
args = parser.parse_args()

with open('../config/config.json') as setting:
    config = json.load(setting)

SERVER_ID = config.get("SERVER_ID")
TOKEN = config.get("TOKEN")

bot = discum.Client(token=TOKEN,log={
    "console": False, "file": False
    })

print("Scraping...")
def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
    bot.gateway.command({
        'function': close_after_fetching, 'params': {
            'guild_id': guild_id
            }
        })
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members(SERVER_ID, args.channel)
memberslist = []

for memberID in members:
    memberslist.append(memberID)

with open(f"../output/scrape/[{SERVER_ID}].txt", "w") as file:
    for member in memberslist:
        file.write(member + "\n")
    file.close()
print(f"Scraped {len(memberslist)} Members")