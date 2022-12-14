import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True



joker_ascii = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣷⡿⠋⢁⣀⣤⣴⣶⣶⣶⣾⣿⣿⣷⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣋⣭⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠞⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠛⠉⠸⣿⡿⣿⣿⠿⢿⡿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⠀
⠀⠀⠀⠀⢰⡏⠀⠀⠉⠛⠛⠛⠛⠉⠁⠈⠛⠛⠉⠁⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣷⣦⣝⠻⣿⣿⣿⣶⣶⣶⡶⢒⡿⢋⡀
⠀⠀⠀⠀⠸⣼⣷⣄⡀⠀⢀⣴⣿⣿⣶⣦⣄⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣠⣖⣩⣶⡟⠁
⠀⠀⠀⠀⠀⠉⠻⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣣⢔⡿⠟⠉⠁⠀⠀⠀⢀⣠⣠⣤⣿⣿⣟⣛⣿⣧⣤⣶⣾⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⠿⣿⣿⣿⣿⢟⠕⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠈⠉⠛⠃⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡿⠛⠛⢻⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠢⡀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⠏⠀⡠⢮⢿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠈⠢⣀⠊⠀⠀⠀⢀⣀⡠⠤⠶⢶⡾⠋⠀⠀⠈⢻⢀⡮⢶⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣀⣀⣀⣀⣤⣬⠷⠤⠖⠚⠯⣥⣄⣠⣴⠟⠁⠀⠀⠀⠀⠈⡉⠀⠞⢀⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⢿⠶⣤⣀⣭⡏⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠒⠒⠂⠀⠹⡤⠴⢯⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠈⠙⢳⠁⠀⠀⠀⠀⣀⠄⠚⠉⠉⢉⡝⠉⣲⣄⠀⠀⠀⢧⠀⠀⠙⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣰⣎⡉⢸⠀⠀⡠⣲⠏⠁⠀⢀⡠⡖⠁⢧⠀⣿⠈⠆⠀⠀⢸⠀⠀⠀⠀⠈⡒⢤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⣇⠈⢻⣾⠀⣠⣊⣤⠤⣶⠚⠉⠀⡇⠀⢸⡄⡿⠀⠀⠀⠀⣼⠀⠀⠀⡜⠀⡇⠀⠈⠑
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣎⠀⠀⢙⣾⡅⢸⠀⠀⠸⡄⠀⠀⡇⠀⣸⣷⡇⠀⠀⠀⣴⠏⠀⠀⣸⠁⢠⠇⠀⠀⠀
⠀⠀⠀⠀DON'T⠀⠀⠀⠀⠀⠈⢣⡀⠈⠸⢷⣈⣇⣀⣀⣳⡄⠠⠓⡎⠁⣾⠀⠀⠀⣼⠟⠀⠀⢠⠃⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀FORGET⠀⠀⠀⠀⠀⠱⡄⠐⡏⠁⠈⡆⠀⠀⢳⠀⠀⢳⣰⠃⠀⠀⣼⡟⠀⠀⢀⠎⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀THE⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⢸⡀⠀⡇⠀⠀⠈⡆⣀⣼⠏⠀⢠⣾⠟⠀⠀⠀⡞⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀JOKER⠀⠀⠀⠀⠀⠀⠈⢎⠛⠿⠿⠷⠶⠶⠭⠗⠋⠀⣰⡿⠧⠤⠤⣀⡼⠁⠀⢀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠙⢆⠀⠀⡜⠁⠀⠀⣸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣱⡀⠀⠀⠀⢀⡴⠛⠦⡀⠀⠀⢣⠞⠀⠀⣀⡠⠧⠒⠲⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠀⠹⡄⠀⡠⠮⠤⠤⢄⣈⣓⣖⣫⡤⠖⠉⠁⠀⠀⠀⢀⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠙⠚⢣⠀⠀⠀⠀⠀⢹⡀⠘⡆⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⢙⠶⣷⡀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣼⢧⠀⠀⠀⡰⡏⢸⠇⣿⠲⣄⠀⠀⠀⡎⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⠈⣆⢀⡜⢡⠃⡞⠇⣿⠀⢸⠳⢄⣠⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠊⠀⡞⠀⣿⡀⣿⠀⡎⠀⠀⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠉⠙⢻⡇⢹⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠷⠋⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠧⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
		
		"""

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print("The Joker has arrived.")

@client.event
async def on_message(message):

	if message.author == client.user:
		return

	if message.content.startswith("$joker"):
		await message.channel.send(joker_ascii)
	elif message.content.lower() != "$joker" and ("joker" in message.content.lower() or "forget" in message.content.lower() or "forgot" in message.content.lower()):
		if message.author.id == 155901476999266305: # checks to see if Harlock is the author, gives 50% chance of returning special message
			harlockrandom = random.randrange(0,2)
			if harlockrandom == 0:
				await message.reply("Take your turn, Harlock!\nhttps://media.giphy.com/media/8JNX7PoLnQuB2wSFB7/giphy.gif")
				return
		await message.reply(joker_reply())

def joker_reply():
	reply_list = [
	"Don't forget The Joker!",
	"Don't forget The Joker!",
	"Psst, hey... don't forget The Joker.",
	"Good job on not forgetting The Joker!",
	"Don't you dare forget.",
	"https://tenor.com/view/joker-hehe-hahaha-laughing-batman-gif-17677598",
	"https://tenor.com/view/bh187-dc-joker-smile-gif-19166369",
	joker_ascii,
	"https://tenor.com/view/lego-batman-movie-legojoker-wave-gif-18258596",
	"Please remain mindful of the painted harlequin of crime.",
	"The clown becomes sad when people forget him. Don't be that guy. Remember The Joker.",
	"You know who's a pretty cool guy worth remembering? The Joker.",
	"https://i.imgur.com/fDYW58C.jpeg",
	"Don't forget The Joker!"
	]
	return reply_list[random.randrange(0, len(reply_list))] # returns a random reply from the above list

client.run(os.getenv("TOKEN"))


"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣷⡿⠋⢁⣀⣤⣴⣶⣶⣶⣾⣿⣿⣷⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣋⣭⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠞⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠛⠉⠸⣿⡿⣿⣿⠿⢿⡿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⠀
⠀⠀⠀⠀⢰⡏⠀⠀⠉⠛⠛⠛⠛⠉⠁⠈⠛⠛⠉⠁⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣷⣦⣝⠻⣿⣿⣿⣶⣶⣶⡶⢒⡿⢋⡀
⠀⠀⠀⠀⠸⣼⣷⣄⡀⠀⢀⣴⣿⣿⣶⣦⣄⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣠⣖⣩⣶⡟⠁
⠀⠀⠀⠀⠀⠉⠻⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣣⢔⡿⠟⠉⠁⠀⠀⠀⢀⣠⣠⣤⣿⣿⣟⣛⣿⣧⣤⣶⣾⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⠿⣿⣿⣿⣿⢟⠕⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠈⠉⠛⠃⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡿⠛⠛⢻⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠢⡀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⠏⠀⡠⢮⢿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠈⠢⣀⠊⠀⠀⠀⢀⣀⡠⠤⠶⢶⡾⠋⠀⠀⠈⢻⢀⡮⢶⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣀⣀⣀⣀⣤⣬⠷⠤⠖⠚⠯⣥⣄⣠⣴⠟⠁⠀⠀⠀⠀⠈⡉⠀⠞⢀⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⢿⠶⣤⣀⣭⡏⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠒⠒⠂⠀⠹⡤⠴⢯⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠈⠙⢳⠁⠀⠀⠀⠀⣀⠄⠚⠉⠉⢉⡝⠉⣲⣄⠀⠀⠀⢧⠀⠀⠙⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣰⣎⡉⢸⠀⠀⡠⣲⠏⠁⠀⢀⡠⡖⠁⢧⠀⣿⠈⠆⠀⠀⢸⠀⠀⠀⠀⠈⡒⢤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⣇⠈⢻⣾⠀⣠⣊⣤⠤⣶⠚⠉⠀⡇⠀⢸⡄⡿⠀⠀⠀⠀⣼⠀⠀⠀⡜⠀⡇⠀⠈⠑
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣎⠀⠀⢙⣾⡅⢸⠀⠀⠸⡄⠀⠀⡇⠀⣸⣷⡇⠀⠀⠀⣴⠏⠀⠀⣸⠁⢠⠇⠀⠀⠀
⠀⠀⠀⠀THIS ⠀⠀⠀⠀⠀⠈⢣⡀⠈⠸⢷⣈⣇⣀⣀⣳⡄⠠⠓⡎⠁⣾⠀⠀⠀⣼⠟⠀⠀⢠⠃⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀IS    ⠀⠀⠀⠀⠀⠱⡄⠐⡏⠁⠈⡆⠀⠀⢳⠀⠀⢳⣰⠃⠀⠀⣼⡟⠀⠀⢀⠎⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀FOR   ⠀⠀⠀⠀⠀⠘⣄⢸⡀⠀⡇⠀⠀⠈⡆⣀⣼⠏⠀⢠⣾⠟⠀⠀⠀⡞⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀STACHE    ⠀⠀⠈⢎⠛⠿⠿⠷⠶⠶⠭⠗⠋⠀⣰⡿⠧⠤⠤⣀⡼⠁⠀⢀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠙⢆⠀⠀⡜⠁⠀⠀⣸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣱⡀⠀⠀⠀⢀⡴⠛⠦⡀⠀⠀⢣⠞⠀⠀⣀⡠⠧⠒⠲⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠀⠹⡄⠀⡠⠮⠤⠤⢄⣈⣓⣖⣫⡤⠖⠉⠁⠀⠀⠀⢀⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠙⠚⢣⠀⠀⠀⠀⠀⢹⡀⠘⡆⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⢙⠶⣷⡀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣼⢧⠀⠀⠀⡰⡏⢸⠇⣿⠲⣄⠀⠀⠀⡎⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⠈⣆⢀⡜⢡⠃⡞⠇⣿⠀⢸⠳⢄⣠⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠊⠀⡞⠀⣿⡀⣿⠀⡎⠀⠀⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠉⠙⢻⡇⢹⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠷⠋⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠧⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
		

"""