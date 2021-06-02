from discord.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.command(name="hello", help="Simple command that sends hello to the server.")
async def hello(ctx):
    await ctx.send("hello!")


'''
This part runs the server, all code should go before this
'''
with open("token.txt", 'r') as token_file:
    TOKEN = token_file.read()
    print("Reading token file")

    bot.run(TOKEN)