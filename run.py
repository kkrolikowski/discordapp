import os
import configparser
import discord
import asyncio
from lib.edziennik import Edziennik


cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(__file__), 'conf/app.conf'))
credentials_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), cfg["MAIN"]["credentials_dir"])

client = discord.Client()

edziennik = Edziennik(credentials_dir)
print(edziennik.credentials_dir)

regdata = {}

@client.event
async def on_ready():
    print("Bot {} connected to server.".format(client.user.display_name))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "$hello @{}".format(client.user.display_name):
        await message.channel.send('Siema {}!'.format(message.author.nick))

    if message.content.startswith('$register'):
        arguments = message.content.split(" ")
        if len(arguments) < 4:
            help_message = """\
            Aby zarejestrować aplikację w edzienniku musisz zalogować się w przeglądarce do systemu Vulcan i
            wygenerować nowy dostęp mobilny. Na spodzie kodu QR znajdziesz informacjie: Token, Symbol i PIN.
            Musisz je kolejno po spacji wpisać: $register token symbol pin
            """.replace("\n", " ").strip()
            await message.channel.send(help_message)
        else:
            regdata[message.author.nick] = arguments

edziennik.register(regdata)

client.run(cfg["MAIN"]["discord_token"])