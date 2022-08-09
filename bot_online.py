
import discord
import os
import search
import requests
import json

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
  # if f'?search' in message_content:

  #   key_words, search_words = search_web.key_words_search_words(message_content)
  #   result_links = search_web.search(key_words)
  #   links = search_web.send_link(result_links, search_words)
  #   magnet_links = search_web.magnet(links)
    
  #   if len(magnet_links) > 0:
  #     for link in magnet_links:
  #       await message.channel.send(link)
  #   else:
  #     await message.channel.send(no_result_message)

  if f'?find' in message_content:
    key_words, search_words = search_web.key_words_search_words(message_content)
    result_links = search_web.search(key_words)
    links = search_web.send_link(result_links, search_words)
    magnet_links,seeders,leechers,size,title = search_web.magnet(links)
  
    x = len(magnet_links)
    if len(magnet_links) > 0:
      for i in range(x):
        shorten_link = requests.get(f"http://mgnet.me/api/create?&format=json&opt=&m={magnet_links[i]}&_=1595006240839",
      headers = {
                "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
                "accept-language": "en-US,en;q=0.9",
                "x-requested-with": "XMLHttpRequest",
                
      }).json()["shorturl"]
        desc = f"size: {size[i]}\tseeders:{seeders[i]}\tleechers: {leechers[i]}"
        embedVar = discord.Embed(title=title[i], url=shorten_link, description=desc, color=0xffffff)
        # embedVar.add_field(f"Movie title [Movie name]({link})")
        await message.channel.send(embed=embedVar) 
    else:
      await message.channel.send(no_result_message)   

# gets bot token
client.run(os.getenv('TOKEN'))
