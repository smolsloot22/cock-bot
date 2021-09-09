import os
import secrets

import discord

TOKEN = os.getenv('BOT_TOKEN')

class CustomClient(discord.Client):

	async def on_ready(self):
		print(f'{client.user} is ready to rate some cocks!')

	async def on_message(self, message):
		#put quotes in here
		cock_quotes = [
			"Woah, that's a nice cock you got there. 8/10",
			"Hey that's a pretty good lookin' cock. 7/10",
			"Mid. I've *definitely* seen better. 5/10",
			"I would hide that stublet, I'm sorry... I truly am, the world can be a cruel place. 1/10",
			"I could smell that thing before I even looked, personal hygiene is important my friend, now go wash that up. 2/10",
			"This cock has seen better days, the burdens of the past can weight heavy, treat yourself better, that should reinvigorate the potential you hold in that penis. 3/10",
			"I'd say that's a passable penis. It has well shaped tip but a little on the short side, not a problem if wielded with skill. 4/10",
			"Quite an underwhelming member, I had expected better from a person of your stature, but I guess we can't all be perfect. 4.5/10",
			"Not the best I've seen, but not the worst either. Enough to satisfy, maybe not the most memorable, a passing grade. 5/10",
			"Passable, humble, yet somewhat homely, size is not everything, it is definitely good enough. 5.5/10",
			"Girthy, lengthy, and just about everything you could ask for, looks a little inexperienced, but I'm sure that can be fixed. 6/10",
			"Pheromones are overwhelming, but looks a little undesirable, what a predicament, unfortunately I'd have to take off some points for that. 6.5/10",
			"Quite the exotic cock, although a little lacking in volume, it promises to be a bundle of excitement and surprise. 7/10",
			"Very solid cock, all the signs of a healthy penis that has seen lots of action, and for good reason I'm sure. 7.5/10",
			"Fragrant? Not the word I thought I'd use, but you must take really good care of your body, very refreshing, almost soothing. What a fine cock. 8/10",
			"Hey, that's pretty good. Nice shape, looks firm, bush could use a slight trim, but overall a cock to be proud of. 8.5/10",
			"That is a cock close to perfection, impressive, one of the best I've seen. 9/10",
			"An outstanding specimen, as if brought to life by the great renaissance, a work of art, truly. 9.5/10",
			"Holy... I've never seen anything like this. Now that's a cock of biblical proportions, to be worshiped for generations. 10/10",
			"A gift from the gods, so shapely and succulent with a clean tip, it's cocks like yours that inspired ancient religion to revere the phallus. 11/10",
			'"A super dimensional being... heh, this may actually be a fair fight!"  - Fighting Solaris as Super Shadow in Sonic \'06.',
			'"I am Shadow the Hedgehog. A research experiment, gone deadly wrong. I\'ve caused so much destruction, I should have never been created. This is who I am." - From one of the many endings in Shadow The Hedgehog.',
			'"Chaos.... CONTROL!" - Right before delivering das boot to Silver\'s yee yee headass',
			"The Urology Care Foundation only recommends penis enhancement surgery for people with a rare condition called micropenis where a penis is two or more standard deviations below the average size. Click here to learn more about penis enlargement methods. 2/10"
		]
		if message.content.startswith('!'):
			channel = message.channel

			if 'cock' or 'cyak' in message.content.lower():
				response = secrets.choice(cock_quotes)
				await channel.send('```'+response+'```')

client = CustomClient()
client.run(TOKEN)
