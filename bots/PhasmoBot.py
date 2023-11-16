import discord
import json
import os
from discord.ext import tasks
from googleapiclient import discovery
from utils.utils import get_asset_dir_path


class PhasmoClient(discord.Client):

    def __init__(self, intents, channel_id, channel_name):
        print("Created phasmo bot")
        super().__init__(intents=intents)
        channel_id = channel_id
        channel_name = channel_name

        path_json = get_asset_dir_path() + "google.json"
        with open(path_json, 'r') as f:
            service = json.load(f)

        youtube = discovery.build_from_document(service, developerKey=os.getenv('YOUTUBE_API_KEY'))

    async def on_ready(self):
        print("We have logged in as {0.user} running phasmo".format(self))



    @tasks.loop(seconds=5)
    async def send_message_task(self):
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send("Hello! This is a message sent every 10 minutes.")

    # @tasks.loop(seconds=1)
    async def __check_new_videos(self):
        try:
            print("Happening")
            response = self.youtube.search().list(part='snippet',
                                             channelId=self.channel_id,
                                             maxResults=1,
                                             order='date').execute()
            video_id = response['items'][0]['id']['videoId']

            last_video_file = open(get_asset_dir_path() + 'last_video.txt', 'r+')
            last_video = last_video_file.read()
            last_video_file.seek(0)

            if last_video != video_id:
                video_response = self.youtube.videos().list(part='snippet', id=video_id).execute()
                video_title = video_response['items'][0]['snippet']['title']
                video_url = f'https://www.youtube.com/watch?v={video_id}'

                # Announce the new video in the Discord channel
                channel = discord.utils.get(self.get_all_channels(), name=self.CHANNEL_NAME)
                await channel.send(f'New video uploaded: {video_title}\n{video_url}')

                # Update the last video ID
                last_video_file.write(video_id)

            last_video_file.close()

        except HttpError as e:
            print(f'An HTTP error occurred: {e}')

        except Exception as e:
            print(f'An error occurred: {e}')


