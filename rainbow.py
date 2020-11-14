
import discord
import asyncio
import random

token = 'NzMyNTE1MDc3OTgyMzg4MjU0.Xw1t1A.y69Hfhzpm2dvqj_M1T3uMXUIdqI'
delay = 2


client = discord.Client()
colours = [discord.Color.dark_orange,discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(rainbowrolename, serverid):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename, serverid))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename, serverid))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Ready.')
    print('------------')

@client.event
async def on_message(message):
    if message.content == ">>set":
        embed = discord.Embed(title="SET UP", description="Tag Role that you want to make rainbow.")
        await message.channel.send(embed=embed)
        msg = await client.wait_for('message', check=lambda message: message.author == message.author)
        rainbowrolename = msg.content
        serverid = message.guild.id
        client.loop.create_task(rainbowrole(rainbowrolename, serverid))

client.run(token)
