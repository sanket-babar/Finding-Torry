import discord
import os
from dotenv import load_dotenv
load_dotenv()
 
client = discord.Client()

# bot online
@client.event
async def on_ready():
  print(f'{client.user} is now online!')

# ?torry command
@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  
  message_content = message.content.lower()  
  
  if message.content.startswith('?torry'):
    await message.channel.send('Hello fellow scrooges! I\'m Torry. Please read my manual by typing ?help or ?commands while I\'m away.')

# gets bot token
client.run(os.getenv('TOKEN'))