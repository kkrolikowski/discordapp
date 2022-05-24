import os
import discord
import configparser
from lib.discordbot import DiscordBot
from lib.edziennik import Edziennik

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(__file__), 'conf/app.conf'))

datadir = os.path.join(os.path.dirname(__file__), "data")
edziennik = Edziennik(datadir, **cfg["VULCAN"])
print(edziennik.pin)
print(edziennik.symbol)
print(edziennik.token)
print(edziennik.datadir)

discord_token = cfg["MAIN"]["discord_token"]
bot = DiscordBot()
bot.run(discord_token)