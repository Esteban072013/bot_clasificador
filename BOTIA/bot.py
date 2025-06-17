import discord
from discord.ext import commands
from modelo import get_class

#permisos
intencions = discord.Intents.default()
intencions.message_content = True

#Objeto bot
bot = commands.Bot(command_prefix='!', intents=intencions)

@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord')
    
#primer comando
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for img in ctx.message.attachments:
            nombre_img = img.filename
            await img.save(f'imagenes/{nombre_img}')
            await ctx.send("Imagen guardada")

            resultado = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=f'imagenes/{nombre_img}'
                    )
            await ctx.send(f"RESULTADO 🔎 {resultado}")

#Correr    
token = ''
bot.run(token)
