import revolt
from revolt.ext import commands

import asyncio
import aiohttp
import requests
import re
import json

#relative imports
import auth
import config

class Bot(commands.CommandsClient):
	def __init__(self, session, token, cogs: 'list[str]'):
		super().__init__(session,token)
		for cog in cogs:
			self.load_extension(cog)

	async def get_prefix(self, message: revolt.Message):
		return config.prefixes

async def main():
	async with aiohttp.ClientSession() as session:
		client = Bot(session, auth.token, cogs=config.cogs)
		await client.start()

asyncio.run(main())