#Flowbot by Kr3s
import discord
import asyncio
import urllib.request
import urllib.parse

values = {'q':'u=6380416'}

data = urllib.parse.urlencode(values)
url = 'http://forum.toribash.com/member.php?u=6380416'+data
#data = data.encode('utd-8')

headers = { }
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)

client = discord.Client()

@client.event
async def on_ready():
	print("Bot Online!")
	print("I'm running on " + client.user.name)
	print("ID:" + client.user.id)

@client.event
async def on_message(message):
        if message.author == client.user:
              return
        elif message.content.startswith("!ping"):
              await client.send_message(message.channel, "Pong!")

client.run("process.env.BOT_TOKEN")
