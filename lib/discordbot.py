import discord

class DiscordBot(discord.Client):
    async def on_ready(self):
        print('We have logged in as {}'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Siema wariacie')
        if message.content.startswith('$register'):
            await message.channel.send("Rejestruję konto w edzienniku dla " + str(message.author.name))
            await message.channel.send("Rejestruję konto w edzienniku dla " + str(message))