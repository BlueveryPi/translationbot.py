import discord
import asyncio
from discord.ext import commands
from translatiey import trans, check

bot = commands.Bot(command_prefix="<><><><><<>")


activated={}


@bot.event
async def on_ready():
    print("ready")


async def transmain(ctx, native, content, webhook):
    if not(check(content, native)) and trans(content, native)!=False:
        await webhook.send(trans(content, native), ephemeral=True)

def checklist(ctx):
    """
    checks if activated is empty for the given channel and sets it up.
    """
    try:
        activated[str(ctx.channel.id)]
    except:
        activated[str(ctx.channel.id)]=[]


@bot.slash_command(guild_ids=[820964115131793449])
async def deactivate(ctx):
    """
    deactivates translation on this channel.
    """
    checklist(ctx)
    for c in activated[str(ctx.channel.id)]:
        if c[0].author.id==ctx.author.id:
            activated[str(ctx.channel.id)].remove(c)

    await ctx.respond("translation is deactivated!", ephemeral=True)


@bot.slash_command(guild_ids=[820964115131793449])
async def translate(ctx, native: str):
    """
    translate all text sent in this channel, and show it privately.
    """
    checklist(ctx)
    try:
        check("hello", native)
    except:
        await ctx.respond("wrong destination language!", ephemeral=True)
    activated[str(ctx.channel.id)].append([ctx, native, ctx.followup])
    await ctx.respond("translation turned on", ephemeral=True)
    #await ctx.defer(ephemeral=True)


@bot.event
async def on_message(ctx):
    if str(ctx.author.id) != str(bot.user.id):
        checklist(ctx)
        for user in activated[str(ctx.channel.id)]:
            await transmain(user[0], user[1], ctx.content, user[2])
            #await user[0].defer(ephemeral=True)


bot.run("your_token_here")
#Made by I_Love_Python#1862. All rights reserved.
