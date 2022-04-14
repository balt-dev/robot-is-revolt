import revolt
from revolt.ext import commands

import re
import json
import requests

class MessageCog(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	async def on_message(self, message: revolt.Message):
		match = re.fullmatch(r'(?:i\'m|i am|im) (.+)',message.content.lower())
		if match is not None:
			nick = match.group(1)
			if nick.find('!!') != -1:
				return await message.channel.send(content=f'<@{message.author.id}> $\\textsf{{IS }}\color{{red}}\\textsf{{NOT}}$ `{nick}` (that nickname has spoilers!)')
			elif len(nick) > 32:
				return await message.channel.send(content=f'<@{message.author.id}> $\\textsf{{IS }}\color{{red}}\\textsf{{NOT}}$ `{nick[:32]}...` (that nickname is too long!)')
			r = requests.patch(
				f'https://api.revolt.chat/servers/{message.server.id}/members/{message.author.id}',
				headers={'x-bot-token':self.bot.token},
				data=json.dumps({'nickname':nick})
			)
			return await message.channel.send(content=f'<@{message.author.id}> $\\textsf{{IS}}$ `{nick}`')
		else:
			self.bot.process_commands(message)

def setup(bot):
	bot.add_cog(MessageCog(bot))