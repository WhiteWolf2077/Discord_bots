import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
@bot.command(name='99', help = 'Responds with Random B99 quote')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates roll dice')
async def roll_dice(ctx, number_of_dice:int, number_of_sides:int):
    dice = [
                str(random.choice(range(1,number_of_sides+1)))
                for _ in range(number_of_dice)
            ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
