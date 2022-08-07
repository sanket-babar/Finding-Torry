import discord
import os
from dotenv import load_dotenv
load_dotenv()

# instantiate discord client 
client = discord.Client()

@client.event
async def on_message(message): 
  # make sure bot doesn't respond to it's own messages to avoid infinite loop
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  
  
  if message.content.startswith(f'?hello'):
    await message.channel.send('''Hello fellow scrooges! I\'m Torry. Please read my manual by typing ?help or ?commands while I'm away.''')