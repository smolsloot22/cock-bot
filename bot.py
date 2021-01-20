import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
	async def on_ready(self):
		print(f'{client.user} has connected to Discord!')
	async def on_member_join(self, member):
		await member.create_dm()
		await member.dm_channel.send(
			f'Hi {member.name}, remember not to be a poop dog'
		)
	async def on_message(self, message):
		if message.author == client.user:
			return

		#put quotes in here
		cock_quotes = [
			"Woah, that's a pretty nice cock you got there.",
			"Hey that's a pretty good lookin' cock.",
			"Mid. I've *definitely* seen better."
		]

		if message.content == '!cock':
			response = random.choice(cock_quotes)
			await message.channel.send(response)

client = CustomClient()

client.run(TOKEN)