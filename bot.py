import discord
from discord.ext import commands
from pathlib import Path
from random import choice
import json

def load_config():
    try:
        with open(str(Path(__file__).parent.absolute()) + '/config.json', 'r') as json_file:
            config = json.load(json_file)
        return config
    except FileNotFoundError:
        print("Confing file not found!")
        print("Exiting...")
        exit()
        
def load_token():
    try:
        with open(str(Path(__file__).parent.absolute()) + '/token.json', 'r') as json_file:
            config = json.load(json_file)
        return config
    except FileNotFoundError:
        print("Confing file not found!")
        print("Exiting...")
        exit()
    
config = load_config()
tok = load_token()

bot = commands.Bot(command_prefix=config['prefix'], help_command=None)


@bot.event
async def on_ready():
    activity = discord.Game(name="with my Rocks, Paper, and Scissors untill someone uses `rps help`", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('My Rocks, Paper, and Scissors are ready!')
    

#Rock

@bot.command(aliases=['Rock', 'r', 'R'])
async def rock(ctx):
    embed=discord.Embed(title=(choice(config['rock'])),color =discord.Colour.random())
    await ctx.send(embed=embed)
    
#Paper

@bot.command(aliases=['Paper','p','P'])
async def paper(ctx):
    embed=discord.Embed(title=(choice(config['paper'])),color =discord.Colour.random())
    await ctx.send(embed=embed)
    
#Scissors

@bot.command(aliases=['Scissors','s','S'])
async def scissors(ctx,):
    embed=discord.Embed(title=(choice(config['scissors'])),color =discord.Colour.random())
    await ctx.send(embed=embed)

#Help
    
@bot.command(aliases=['h','H','Help'])
async def help(ctx):
    embed=discord.Embed(title="How To Use RPS", description="RPS is a Discord bot written in python to allow you to play Rock Paper Scissors", color =discord.Colour.random())
    embed.add_field(name="Rock", value="`Rock, rock, R, r` - Choose rock as your move", inline=True)
    embed.add_field(name="Paper", value="`Paper, paper, P, p` - Choose paper as your move", inline=True)
    embed.add_field(name="Scissors", value="`Scissors, scissors, S, s` - Choose scissors as your move", inline=True)
    await ctx.send(embed=embed)
    
    
@commands.is_owner()
@bot.command()
async def reload(ctx):
    config = load_config()
    await ctx.send('Config reloaded.')

bot.run(tok['token'])

