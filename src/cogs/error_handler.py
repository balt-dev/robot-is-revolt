from revolt.ext import commands

class ErrorHandlerCog(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

#	@commands.Cog.listener()
#	async def on_command_error(self, ctx: commands.Context, error: Exception):
#		print(error.__traceback__)

def setup(bot):
	bot.add_cog(ErrorHandlerCog(bot))