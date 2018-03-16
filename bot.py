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
