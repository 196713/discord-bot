import discord
from discord.ext import commands

class Mod:
	def __init__(self, client):
		self.client = client

	async def on_member_join(self, member):
	    role = discord.utils.get(member.server.roles, name='Members')
	    await self.client.add_roles(member, role)

def setup(client):
	client.add_cog(Mod(client))