import Trash
from bots.FilthyFrankBot import FilthyFrankClient


# Just used for testing
# TODO: Remove this class
class DiscordChannel:
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    def __init__(self, client, channelId, channel_name):
        second_client = FilthyFrankClient(client)
        channelId = channelId
        channel_name = channel_name

    def run_client(self, token):
        self.client.run(token)



