import discord
from discord.ext import tasks

class ReminderClient(discord.Client):

    def __init__(self, intents):
        print("Created reminders")
        super().__init__(intents=intents)
        self.send_message_task()

    async def on_ready(self):
        print("We have logged in as {0.user} running filthy frank".format(self))
        try:
            channel = self.get_channel(1120925296586149929)
        except Exception as e:
            print(e)
        await channel.send('Hello, Discord!')

    @tasks.loop(seconds=5)
    async def send_message_task(self):
        try:
            channel = self.get_channel(1120925296586149929)
        except Exception as e:
            print(e)
        print("Chek this")
        print(channel)
        if channel:
            await channel.send("Hello! Trying this out")


