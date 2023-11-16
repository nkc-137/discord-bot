import discord
from discord.ext import commands, tasks
import asyncio

class MessageSenderBot(commands.Bot):
    def __init__(self, command_prefix, channel_id, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.channel_id = channel_id
        self.token = 'MTEyMDg3NDc1OTcxMDg0Mjk2MA.GgfLNK.zysKYQTxKhd3uxZrBth2AlwEMs6nT_1csCUJ9A'

    async def on_ready(self):
        print(f'We have logged in as {self.user.name}')
        await self.send_message()

    @tasks.loop(seconds=2)
    async def send_message(self):
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send("This is a message sent every 2 secs.")

if __name__ == '__main__':
    intents = discord.Intents.all()
    bot = MessageSenderBot(command_prefix='!', channel_id=1120925296586149929, intents=intents)
    bot.run(bot.token)

