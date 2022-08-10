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
    await message.channel.send('Hello fellow scrooges! I\'m Torry. Please read my manual by typing ?t help or ?t commands while I\'m away.')

  if (message.content.startswith('?t help') or message.content.startswith('?t commands')):
    await message.channel.send('''Here are the list of commands Torry supports:
    ?torry: Say hello to Torry
    ?t find <search your torrent here> or ?t search <search your torrent here>: Searches your torrent and returns top 5 results
    ?t help or ?t commands: To view commands
    Note: Torry scrapes through hundreds of pages and might take a few seconds. Please be patient <3''')
    

  if (f'?t find' in message_content or f'?t search' in message_content):
    key_words, search_words = search_web.key_words_search_words(message_content)
    result_links = search_web.search(key_words)
    links = search_web.send_link(result_links, search_words)
    magnet_links,seeders,leechers,size,title = search_web.magnet(links)
  
    if len(magnet_links) > 0:
      for i in range(len(magnet_links)):
        shorten_link = requests.get(f"http://mgnet.me/api/create?&format=json&opt=&m={magnet_links[i]}&_=1595006240839",
      headers = {
                "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
                "accept-language": "en-US,en;q=0.9",
                "x-requested-with": "XMLHttpRequest",
                
      }).json()["shorturl"]
        desc = f"📂 Size: {size[i]} ▪️▪️ ⬆️ Seeders: {seeders[i]} ▪️▪️ ⬇️ Leechers: {leechers[i]}"
        embedVar = discord.Embed(title=title[i], url=shorten_link, description=desc, color=0xff61f4)
        # embedVar.add_field(f"Movie title [Movie name]({link})")
        await message.channel.send(embed=embedVar) 
      await message.channel.send("Didn't get what you searched for? Try being more specific")
    else:
      await message.channel.send(no_result_message)   

# gets bot token
client.run(os.getenv('TOKEN'))
