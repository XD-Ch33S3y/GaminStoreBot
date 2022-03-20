from datetime import datetime
import discord

from discord.ext import commands
from discord import ApplicationContext, Option

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="?",intents=intents)

@bot.event
async def on_ready():
    print(f"I have started up and logged in {bot.user.name}{bot.user.discriminator}!")

@bot.slash_command(name="stock", description="Check how much we have in stock.", guild_ids=[922298888994553917])
async def stock(ctx: ApplicationContext):
    embed = discord.Embed()
    embed.title = "Hypixel Coins"
    embed.color = 0x00ffff
    embed.set_footer(text="We'll match any big/reputable server.")
    embed.timestamp = datetime.now()

    stock = 0

    with open("stock.txt", "r") as _:
        stock = int(_.read())

    embed.description = f"We have `{'{:,.2f}'.format(stock)}` Hypixel Coins.\n\nHead over to <#put channel id> to buy."

    await ctx.respond(embed=embed)

@bot.slash_command(name="rate", description="Check how much you would get for your budget.", guild_ids=[922298888994553917])
async def rate(ctx: ApplicationContext,
    money:Option(float, "How much money you wanna spend.")
):
    embed = discord.Embed()
    embed.title = "Hypixel Coins"
    embed.color = 0x00ffff
    embed.set_footer(text="We'll match any big/reputable server.")
    embed.timestamp = datetime.now()

    rate = 0

    with open("rate.txt", "r") as _:
        rate = float(_.read())

    embed.description = f"With `${'{:,.2f}'.format(money)}`, you would get `{'{:,.2f}'.format((money*rate) * 1000000)}` Hypixel Coins.\n\nHead over to <#put channel id> to buy."

    await ctx.respond(embed=embed)

bot.run("bot token")