import os
import configparser
import asyncio
from lib.discordbot import DiscordBot
from lib.edziennik import Edziennik

async def main() -> None:
    cfg = configparser.ConfigParser()
    cfg.read(os.path.join(os.path.dirname(__file__), 'conf/app.conf'))

    credentials_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), cfg["MAIN"]["credentials_dir"])
    edziennik = Edziennik(credentials_dir)
    print(edziennik.credentials_dir)

    discord_token = cfg["MAIN"]["discord_token"]
    bot = DiscordBot()
    bot.run(discord_token)

if __name__ == "__main__":
    asyncio.run(main())