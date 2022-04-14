import revolt
from revolt.ext import commands

class OwnerCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.is_bot_owner()
	async def reload(self, ctx: commands.Context):
		'''Reloads all of the bot's cogs.'''
		cogs = list(self.bot.extensions)
		for cog in cogs:
			self.bot.reload_extension(cog)
		await ctx.send("Reloaded cogs.")

def setup(bot):
	bot.add_cog(OwnerCog(bot))


