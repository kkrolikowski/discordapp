import discord

class DiscordBot(discord.Client):
    async def on_ready(self):
        print('We have logged in as {}'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')