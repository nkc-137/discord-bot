import discord
from discord.ext import commands

from commands import *
from utils.utils import get_asset_path


class FilthyFrankClient(discord.Client):

    def __init__(self, intents):
        print("Created filthy frank bot")
        super().__init__(intents=intents)

    async def on_ready(self):
        print("We have logged in as {0.user} running filthy frank".format(self))
        bot = commands.Bot(intents=self.intents, command_prefix='!')
        try:
            channel = self.get_channel(1120925296586149929)
        except Exception as e:
            print(e)
        await channel.send('Hello, Discord!')

    async def on_message(self, message):
        if message.content == hello:
            await message.channel.send('Hello!')

        if message.content == franku:
            await self.__send_media(message.channel, 'filthy_frank.jpg')

        if message.content == yamete:
            await self.__send_media(message.channel, 'yamete.gif')

        if message.content == prankd:
            await self.__send_media(message.channel, 'prankd.gif')

        if message.content == noobsai:
            await self.__send_media(message.channel, 'noobsai.gif')

        if message.content == noshit:
            await self.__send_media(message.channel, 'filthy-frank-nobody-cares.gif')

        if message.content == help:
            with open(get_asset_path('help.txt'), 'r') as f:
                help_txt = f.read()
            await message.channel.send(help_txt)

    async def __send_media(self, channel, media_name):
        with open(get_asset_path(media_name), 'rb') as f:
            media = discord.File(f)
            await channel.send(file=media)

    def get_chans(self, channel_name):
        return discord.utils.get(self.get_all_channels(), name=channel_name)

