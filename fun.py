import discord
from discord.ext import commands
import random
import json
from urllib.request import urlopen
from threading import Timer

class Fun:
	def __init__(self, client):
		self.client = client

	@commands.command(name="8ball")
	async def _ball(self):
		await self.client.say(':8ball: **'+random.choice(["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."])+'**')

	@commands.command()
	async def dice(self):
		await self.client.say(random.choice(['1', '2', '3', '4', '5', '6']))

	@commands.command()
	async def choose(self, *, args):
		items = args.split('|')
		await self.client.say(random.choice(items))

	@commands.command()
	async def rps(self, arg):
		if arg == 'rock' or arg == 'paper' or arg == 'scissors':
			pick = arg
			cpupick = random.choice(['rock', 'paper', 'scissors'])
			if youwin(pick, cpupick) == True:
				await self.client.say('**I chose '+cpupick+'. You win!**')
			elif youwin(pick, cpupick) == False:
				await self.client.say('**I chose '+cpupick+'. You lose.**')
			else:
				await self.client.say('**We both chose '+cpupick+'. Draw!**')
		else:
			await self.client.say('Invalid move. Play either rock, paper, or scissors.')

#Functions to help with fun commands
def youwin(yourmove, cpumove):
	if yourmove == 'rock' and cpumove == 'paper':
		return False
	elif yourmove == 'rock' and cpumove == 'scissors':
		return True
	elif yourmove == 'paper' and cpumove == 'rock':
		return True
	elif yourmove == 'paper' and cpumove == 'scissors':
		return False
	elif yourmove == 'scissors' and cpumove == 'rock':
		return False
	elif yourmove == 'scissors' and cpumove == 'paper':
		return True
	else:
		return

def setup(client):
	client.add_cog(Fun(client))