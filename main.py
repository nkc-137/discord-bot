import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks
from googleapiclient.errors import HttpError
import json
from googleapiclient import discovery
from flask import Flask
from threading import Thread
from commands import *

load_dotenv()

app = Flask('')

@app.route('/')
def main():
    return "Your Bot Is Ready"


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()

assets_path = r"/home/wolf/PhasmoBot/assets/"
# Path to the json file you downloaded:
path_json = assets_path + "google.json"

def get_asset_path(asset_name):
    return assets_path+asset_name
    
async def send_media(channel, media_name):
    with open(get_asset_path(media_name), 'rb') as f:
        media = discord.File(f)
        await channel.send(file=media)
        

with open(path_json, 'r') as f:
    service = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
CHANNEL_ID = 'UCsAo51oI_6a-rDPxkB7H0bA'
CHANNEL_NAME = 'phasmo-news'

youtube = discovery.build_from_document(
    service, developerKey=os.getenv('YOUTUBE_API_KEY'))


@tasks.loop(minutes=360)
async def check_new_videos():
    try:
        response = youtube.search().list(part='snippet',
                                         channelId=CHANNEL_ID,
                                         maxResults=1,
                                         order='date').execute()
        video_id = response['items'][0]['id']['videoId']

        last_video_file = open(assets_path+'last_video.txt', 'r+')
        last_video = last_video_file.read()
        last_video_file.seek(0)

        if last_video != video_id:
            video_response = youtube.videos().list(part='snippet', id=video_id).execute()
            video_title = video_response['items'][0]['snippet']['title']
            video_url = f'https://www.youtube.com/watch?v={video_id}'

            # Announce the new video in the Discord channel
            channel = discord.utils.get(client.get_all_channels(), name=CHANNEL_NAME)
            await channel.send(f'New video uploaded: {video_title}\n{video_url}')

            # Update the last video ID
            last_video_file.write(video_id)

        last_video_file.close()

    except HttpError as e:
        print(f'An HTTP error occurred: {e}')

    except Exception as e:
        print(f'An error occurred: {e}')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    check_new_videos.start()


@client.event
async def on_message(message):
    if message.content == hello:
        await message.channel.send('Hello!')

    if message.content == franku:
        await send_media(message.channel,'filthy_frank.jpg')

    if message.content == yamete:
        await send_media(message.channel, 'yamete.gif')
        
    if message.content == prankd:
        await send_media(message.channel, 'prankd.gif')

    if message.content == noobsai:
        await send_media(message.channel, 'noobsai.gif')
    
    if message.content == noshit:
        await send_media(message.channel, 'filthy-frank-nobody-cares.gif')

    if message.content == help:
        with open(get_asset_path('help.txt'), 'r') as f:
            help_txt = f.read()
        await message.channel.send(help_txt)
    
        


client.run(os.getenv('TOKEN'))
