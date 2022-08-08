import discord
import os
import search

from dotenv import load_dotenv
load_dotenv()
 
client = discord.Client()
search_web = search.Search()
no_result_message = '''Sorry, we can\'t find what you are searching for. Are you sure you typed right?'''
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
  if f'?search' in message_content:

    key_words, search_words = search_web.key_words_search_words(message_content)
    result_links = search_web.search(key_words)
    links = search_web.send_link(result_links, search_words)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)  

# gets bot token
client.run(os.getenv('TOKEN'))