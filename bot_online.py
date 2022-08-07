import discord
import os
from dotenv import load_dotenv
load_dotenv()

# instantiate discord client 
client = discord.Client()

# discord event to check when the bot is online 
@client.event
async def on_ready():
  print(f'{client.user} is now online!')

# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))