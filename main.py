import discord
import os

from dotenv import load_dotenv
from googleapiclient import discovery
import asyncio
from bots.FilthyFrankBot import FilthyFrankClient
from bots.PhasmoBot import PhasmoClient
from bots.ReminderBot import ReminderClient
from utils.utils import get_asset_dir_path
load_dotenv()

# CONSTANTS
CHANNEL_ID = 'UCsAo51oI_6a-rDPxkB7H0bA'
CHANNEL_NAME = 'phasmo-news'
DISCORD_TOKEN = os.getenv('TOKEN')

# phasmo_news_channel = DiscordChannel(CHANNEL_ID, CHANNEL_NAME)

path_json = get_asset_dir_path() + "google.json"

intents = discord.Intents.all()
client = discord.Client(intents=intents)
filthy_frank_client = FilthyFrankClient(intents=intents)
phasmo_client = PhasmoClient(intents, CHANNEL_ID, CHANNEL_NAME)
reminder_client = ReminderClient(intents=intents)

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
    loop = asyncio.get_event_loop()

    task1 = loop.create_task(filthy_frank_client.start(DISCORD_TOKEN))
    task2 = loop.create_task(phasmo_client.start(DISCORD_TOKEN))
    task3 = loop.create_task(reminder_client.start(DISCORD_TOKEN))
    task4 = loop.create_task(reminder_client.send_message_task())

    await asyncio.gather(task1, task2, task3, task4)

asyncio.run(main())
