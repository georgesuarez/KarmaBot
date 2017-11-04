import discord
import random
import requests
import praw
import asyncio
import imgurbot
import prawbot
import bot_token

from bs4 import BeautifulSoup
from discord.ext import commands
from imgurpython import ImgurClient

description = 'KarmaBot'
bot_prefix = '!'

bot = commands.Bot(description=description, command_prefix=bot_prefix)


@bot.event
async def change_presence():
    await bot.change_presence(game=discord.Game(name='Beep-bop'))


"""Authorizing Imgur API"""
client_id = imgurbot.client_id
client_secret = imgurbot.client_secret
client = ImgurClient(client_id, client_secret)

"""Authorizing Reddit API"""
redditbot = praw.Reddit(client_id=prawbot.client_id,
                        client_secret=prawbot.client_secret,
                        user_agent=prawbot.user_agent)

"""Log in the discord bot"""


@bot.event
async def on_ready():
    print('Logged in')
    print('Name: {}'.format(bot.user.name))
    print('ID : {}'.format(bot.user.id))
    print(discord.__version__)
    print('========')

"""Bot commands go here"""
# Clear messages up to 14 days old
# Can only clear up to 2 to 100 messages at a time


@bot.command(pass_context=True)
async def clear(ctx, number):
    number = int(number)
    messages_to_delete = []

    async for x in bot.logs_from(ctx.message.channel, limit=number):
        messages_to_delete.append(x)
    await bot.delete_messages(messages_to_delete)

# Imugr command v1.0


@bot.command()
async def imgur(query: str):
    subreddit = client.subreddit_gallery(
        query, sort='top', window='day', page=0)

    url_links = []
    title_of_links = []

    for submission in subreddit:
        title_of_links.append(submission.title)
        url_links.append(submission.link)

    submissions = dict(zip(title_of_links, url_links))

    title, url_link = random.choice(list(submissions.items()))

    await bot.say(title)
    await bot.say(url_link)

# Reddit command v1.0


@bot.command()
async def reddit(query: str):
    subreddit = redditbot.subreddit(query)
    url_links = []
    title_of_links = []

    for submission in subreddit.top(limit=50):
        title_of_links.append(submission.title)
        url_links.append(submission.url)

    submissions = dict(zip(title_of_links, url_links))

    title, url_link = random.choice(list(submissions.items()))

    await bot.say(title)
    await bot.say(url_link)

# Always put this last!!!
bot.run(bot_token.token)
