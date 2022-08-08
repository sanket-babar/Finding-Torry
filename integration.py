import search

# instantiate RunPeeWeb class from search.py
search_web = search.RunPeeWeb()

# no result message 
no_result_message = '''Sorry, we can\'t find what you are searching for. Are you sure you typed right?'''


@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  
  if message.content.startswith(f'?torry'):
    await message.channel.send('Hello there! I\'m the bad robot you fart face.')
    
  if f'?search' in message_content:

    key_words, search_words = search_web.key_words_search_words(message_content)
    result_links = search_web.search(key_words)
    links = search_web.send_link(result_links, search_words)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)