import os
import discord
import configparser
from lib.discordbot import DiscordBot
from lib.edziennik import Edziennik

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(__file__), 'conf/app.conf'))

edziennik = Edziennik(cfg["VULCAN"]["vulcan_token"], cfg["VULCAN"]["vulcan_symbol"], cfg["VULCAN"]["vulcan_pin"])
print(edziennik.pin)
print(edziennik.symbol)
print(edziennik.token)

discord_token = cfg["MAIN"]["discord_token"]
bot = DiscordBot()
bot.run(discord_token)