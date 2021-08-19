import asyncio
from discord.ext import commands
from termcolor import cprint
from os import system, name

class ConsoleMessage:
    def __init__(self, content, bot):
        self.content = content.strip()
        self.channel = bot.channel
        self.guild = getattr(bot.channel, 'guild', False) or None

class Context(commands.Context):
    def __init__(self, **attrs):
        self.bot = attrs.pop('bot', None)
        self.view = attrs.pop('view', None)
        self.command = attrs.pop('command', None)
        self.message = ConsoleMessage(attrs.pop('message', None), self.bot)

        self.channel = self.bot.channel
        self.guild = getattr(self.bot.channel, 'guild', False) or None

        self.check_channel()

    def check_channel(self):
        if self.channel is None:
            system('clear')
            try:
                self.bot.channel = self.bot.get_channel(int(self.message.content))
            except ValueError:
                cprint('Channel not set. Send a channel ID to start the program', 'red')
            else:
                if self.bot.channel is None:
                    cprint('Invalid text channel.', 'red')
                else:
                    if hasattr(self.bot.channel, "name"):
                        cprint('Text channel set: #{}'.format(self.bot.channel.name), 'green')
                    else:
                        cprint('Text channel set: #{}'.format(self.bot.channel), 'green')

    async def send(self, *args, **kwargs):
        await self.channel.send(*args, **kwargs)
