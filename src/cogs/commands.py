import revolt
from revolt.ext import commands
import requests
import json
import re

class CommandsCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



def setup(bot):
	bot.add_cog(CommandsCog(bot))