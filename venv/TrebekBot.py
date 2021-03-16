import discord
from asyncio import sleep
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$buzz'):
        await message.channel.send(str(message.author).split('#')[0])
        await sleep(2)
        await message.channel.send('ERRRRRRR')
        user = message.author
        voice_player = await message.author.voice.channel.connect()
        #voice_channel = user.voice_channel
        #voice_channel.play(discord.FFmpegPCMAudio(stream_url))
        # source = discord.FFmpegPCMAudio("Bong.mp3")
        # player = voice_player.play(source)
        # player.start()


client.run('ODIxMTk2MTc5ODc4NTc2MTM5.YFAMig.QB-4vhqFmf2GOeU-PWHMgaQop7Q')