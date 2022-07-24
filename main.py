import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('metallica'):
        await message.channel.send(
            'Metallica is the best band ever. Nothing else matters is my favorite song. You cannot talk like that.'
        )

    if message.content.startswith('megadeth'):
        await message.channel.send(
            "Dave Mustaine's crying project about being kicked out :)")

    if message.content.startswith('poser'):
        await message.channel.send(
            "I am a poser? It is not my fault that you don't know what good music is. I bet you also don't like Enter Sandman or, The Unforgiven."
        )


client.run('TOKEN')  # paste token here
