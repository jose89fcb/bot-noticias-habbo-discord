import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import os
import json
import urllib.request
 

with open("config.json") as f:
    config = json.load(f) 
 
bot = commands.Bot(command_prefix=config["comando"], description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 


HotelNoticia=config["NoticiasHotel"] ## es -> en -> it -> de-> fr -> fi -> fi -> tr -> nl -> pt 
url = f"https://images.habbo.com/habbo-web-news/{HotelNoticia}/production/front.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

hotel=config["hotel"] ## es -> com ->it -> de -> fr -> com.tr ->nl -> com.br

titulo = soup.find_all('h2', class_='news-header__title')[1].text

imagen = soup.find_all('img')[2]

urlNoticia = soup.find_all('a')[3]

descripcion = soup.find_all('p', class_='news-header__wrapper news-header__summary')[1].text




os.system(f"TITLE Noticias habbo - HOTEL: habbo.{hotel}")
os.system("cls")


  


@bot.command()
async def noticias(ctx): 
    embed = discord.Embed(title=f"{titulo}", description=f"{descripcion}" f"\n\n\n[Ver Noticia en Habbo.{hotel}]"+"("+ f"https://habbo.{hotel}"+urlNoticia['href']+ ")", color=discord.Colour.random())
    embed.set_image(url=f"{imagen['src']}" )
    embed.set_author(name=f"Habbo [{HotelNoticia}]",  icon_url=config["Bandera"])
    embed.set_footer(text=f"habbo [{HotelNoticia}]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)
   
 
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('El comando no existe 🤷🏼‍♂️🔍')
  

@bot.event
async def on_ready():
    print("BOT listo!")





bot.run(config["token_discord"])