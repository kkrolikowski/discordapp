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
            arguments = message.content.split(" ")
            if len(arguments) < 4:
                help_message = """\
                Aby zarejestrować aplikację w edzienniku musisz zalogować się w przeglądarce do systemu Vulcan i
                wygenerować nowy dostęp mobilny. Na spodzie kodu QR znajdziesz informacjie: Token, Symbol i PIN.
                Musisz je kolejno po spacji wpisać: $register token symbol pin
                """.replace("\n", " ").strip()
                await message.channel.send(help_message)
            else:
                await message.channel.send("Rejestruję konto w edzienniku dla " + str(message.author.nick))
                await message.channel.send("Token: " + arguments[1] + ", Miasto: " + arguments[2] + ", PIN: " + arguments[3])