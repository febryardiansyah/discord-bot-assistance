import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('ready')

#check ping
@client.command()
async def ping(ctx):
    await ctx.send(f'your ping is {round(client.latency * 1000)}ms')

#clear text
@client.command()
async def clear(ctx,ammount=5):
    await ctx.channel.purge(limit=ammount)

#kick command
@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)

#ban command
@client.command()
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

#unban command
@client.command()
async def unban(ctx,*,member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_user:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member.name, member.discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unban {user.mention}')
            return
            
client.run('YOUR_TOKEN')