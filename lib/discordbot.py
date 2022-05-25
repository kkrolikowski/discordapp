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
            await message.channel.send("Rejestruję konto w edzienniku dla " + str(message.author.nick))
            arguments = message.content.split(" ")
            if len(arguments) < 4:
                await message.channel.send("Aby zarejestrować aplikację w edzienniku musisz podać: Token, Miasto i PIN")
            else:
                await message.channel.send("Token: " + arguments[1] + ", Miasto: " + arguments[2] + ", PIN: " + arguments[3])