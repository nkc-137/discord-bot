import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
import json
from googleapiclient import discovery
from flask import Flask
from threading import Thread
import asyncio
from clients.FilthyFrankClient import FilthyFrankClient
from clients.PhasmoClient import PhasmoClient
from utils.utils import get_asset_dir_path
load_dotenv()

# CONSTANTS
CHANNEL_ID = 'UCsAo51oI_6a-rDPxkB7H0bA'
CHANNEL_NAME = 'phasmo-news'
DISCORD_TOKEN = os.getenv('TOKEN')

# phasmo_news_channel = DiscordChannel(CHANNEL_ID, CHANNEL_NAME)

path_json = get_asset_dir_path() + "google.json"

intents = discord.Intents.all()
# intents.message_content = True
# intents.reactions = True
# intents.members = True
# intents.guilds = True
client = discord.Client(intents=intents)
filthy_frank_client = FilthyFrankClient(intents=intents)
phasmo_client = PhasmoClient(intents, CHANNEL_ID, CHANNEL_NAME)


# app = Flask('')

# @app.route('/')
# def main():
#     return "Your Bot Is Ready"

# def run():
#     app.run(host="0.0.0.0", port=8000)
#
#
# def keep_alive():
#     server = Thread(target=run)
#     server.start()


# with open(path_json, 'r') as f:
#     service = json.load(f)
#
# youtube = discovery.build_from_document(service, developerKey=os.getenv('YOUTUBE_API_KEY'))
#

# @discord.tasks.loop(minutes=360)
# async def check_new_videos():
#     try:
#         response = youtube.search().list(part='snippet',
#                                          channelId=CHANNEL_ID,
#                                          maxResults=1,
#                                          order='date').execute()
#         video_id = response['items'][0]['id']['videoId']
#
#         last_video_file = open(get_asset_dir_path() + 'last_video.txt', 'r+')
#         last_video = last_video_file.read()
#         last_video_file.seek(0)
#
#         if last_video != video_id:
#             video_response = youtube.videos().list(part='snippet', id=video_id).execute()
#             video_title = video_response['items'][0]['snippet']['title']
#             video_url = f'https://www.youtube.com/watch?v={video_id}'
#
#             # Announce the new video in the Discord channel
#             channel = discord.utils.get(client.get_all_channels(), name=CHANNEL_NAME)
#             await channel.send(f'New video uploaded: {video_title}\n{video_url}')
#
#             # Update the last video ID
#             last_video_file.write(video_id)
#
#         last_video_file.close()
#
#     except HttpError as e:
#         print(f'An HTTP error occurred: {e}')
#
#     except Exception as e:
#         print(f'An error occurred: {e}')


# @client.event
# async def on_ready():
#     print("We have logged in as {0.user}".format(client))
    # check_new_videos.start()


async def main():
    filthy_frank_client = FilthyFrankClient(intents=intents)
    phasmo_client = PhasmoClient(intents, CHANNEL_ID, CHANNEL_NAME)

    loop = asyncio.get_event_loop()


    task1 = loop.create_task(filthy_frank_client.start(DISCORD_TOKEN))
    task2 = loop.create_task(phasmo_client.start(DISCORD_TOKEN))

    await asyncio.gather(task1, task2)

asyncio.run(main())
