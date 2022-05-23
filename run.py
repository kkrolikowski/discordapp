import os
import discord
import configparser
from lib.discordbot import DiscrodBot

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(__file__), 'conf/app.conf'))

discord_token = cfg["MAIN"]["discord_token"]

bot = DiscrodBot()
bot.run(discord_token)