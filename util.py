import discord
from discord.ext import commands
import re

class Util:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self):
	    await self.client.say('Pong!')

	@commands.command()
	async def say(self, *, arg):
		await self.client.say(arg)

	@commands.command(pass_context=True)
	async def sayd(self, ctx, *, arg):
	  await self.client.say(arg)
	  await self.client.delete_message(ctx.message)

	@commands.command(pass_context=True)
	async def clear(self, ctx, amount=100):
	    channel = ctx.message.channel
	    messages = []
	    async for message in self.client.logs_from(channel, limit=int(amount) + 1):
	        messages.append(message)
	    await self.client.delete_messages(messages)
	    await self.client.say('Messages deleted.')

	@commands.command()
	async def avatar(self, arg):
	    userid = re.sub('<|@|!|>', '', arg)
	    user = await self.client.get_user_info(userid)
	    useravi_url = re.sub('.webp', '.png', user.avatar_url)
	    embed_msg = discord.Embed(
	        title = str(user),
	        description = '[Direct Link]('+useravi_url+')'
	        )
	    embed_msg.set_image(url=useravi_url)
	    await self.client.say(embed = embed_msg)

	@commands.command(pass_context=True)
	async def changenick(self, ctx, *, arg=None):
		nickname = arg
		await self.client.change_nickname(ctx.message.author, nickname)
		await self.client.say('I have changed your nickname to **'+nickname+'**.')

def setup(client):
	client.add_cog(Util(client))