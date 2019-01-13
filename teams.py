import discord
from discord.ext import commands
import random

class Matchmaking:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def teams(self, arg, *args):
		formatnum = int(arg)
		players = list(args)
		numplayers = len(players)
		output = ''
		if (numplayers % formatnum) != 0:
			await self.client.say('```Make sure the number of players is a multiple of ' + str(formatnum) + ' (The Format)```')
		else:
			numteams = numplayers // formatnum
			team = 1
			while len(players) > 0:
				output += '`Team ' + str(team) + ':` '
				for k in range(formatnum):
					randnum = random.randint(0, len(players)-1)
					tempname = players.pop(randnum)
					if k == formatnum - 1:
						output += tempname + ''
					else:
						output += tempname + ' '
				output += '\n'
				team += 1
			await self.client.say(output)


def setup(client):
	client.add_cog(Matchmaking(client))