import os
import discord
import configparser

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(__file__), 'conf/app.conf'))

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

print(cfg["MAIN"]["discord_token"])
client.run(cfg["MAIN"]["discord_token"])
