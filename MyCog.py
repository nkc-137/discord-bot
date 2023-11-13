import discord
import asyncio
import os

from clients.FilthyFrankClient import FilthyFrankClient
from clients.PhasmoClient import PhasmoClient

intents = discord.Intents.default()
intents.message_content = True
DISCORD_TOKEN = 'MTEyMDg3NDc1OTcxMDg0Mjk2MA.GgfLNK.zysKYQTxKhd3uxZrBth2AlwEMs6nT_1csCUJ9A'
class MyClient1(discord.Client):
    async def on_ready(self):
        print(f'Client 1 is ready. Logged in as {self.user.name}')

    # Add your event handlers and commands for Client 1 here

class MyClient2(discord.Client):
    async def on_ready(self):
        print(f'Client 2 is ready. Logged in as {self.user.name}')

    # Add your event handlers and commands for Client 2 here

async def main():
    # Replace 'YOUR_TOKEN_1' and 'YOUR_TOKEN_2' with the actual tokens for your clients
    client1 = FilthyFrankClient(intents=intents)
    client2 = PhasmoClient(intents,'UCsAo51oI_6a-rDPxkB7H0bA', 'phasmo-news')

    loop = asyncio.get_event_loop()
    print(DISCORD_TOKEN)

    # Start each client in a separate asyncio event loop
    task1 = loop.create_task(client1.start(DISCORD_TOKEN))
    task2 = loop.create_task(client2.start(DISCORD_TOKEN))

    # Wait for both tasks to finish
    await asyncio.gather(task1, task2)


asyncio.run(main())