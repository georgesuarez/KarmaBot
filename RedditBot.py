#!/usr/bin/env python3

import discord
import random
import requests
import praw
import asyncio
import os

import imgurbot
import prawbot
import bot_token

from discord.ext.commands import Bot
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

description = 'KarmaBot'
bot_prefix = '!'

bot = Bot(description=description, command_prefix=bot_prefix)

"""Authorizing Imgur API"""
client_id = imgurbot.client_id
client_secret = imgurbot.client_secret
imgur_client = ImgurClient(client_id, client_secret)

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
    await bot.change_presence(game=discord.Game(name='!reddit'))


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

# Imugr command v1.0.1


@bot.command()
async def imgur(query: str):
    subreddit = imgur_client.subreddit_gallery(
        query, sort='top', window='day', page=0)

    url_links = []
    titles_of_link = []

    for submission in subreddit:
        titles_of_link.append(submission.title)
        url_links.append(submission.link)

    submissions = dict(zip(titles_of_link, url_links))

    title, url_link = random.choice(list(submissions.items()))

    embed = discord.Embed(title=title, url=url_link, color=0xff0404)
    embed.set_image(url=url_link)
    await bot.say(embed=embed)

# Reddit command v1.0.1


@bot.command()
async def reddit(query: str):
    subreddit = redditbot.subreddit(query)
    title_of_links = []
    url_links = []

    for submission in subreddit.hot(limit=50):
        title_of_links.append(submission.title)
        url_links.append(submission.url)

    submissions = dict(zip(title_of_links, url_links))

    title, url_link = random.choice(list(submissions.items()))

    embed = discord.Embed(title=title, url=url_link, color=0xff0404)
    embed.set_image(url=url_link)
    await bot.say(embed=embed)


@bot.command()
async def anime_irl():
    subreddit = redditbot.subreddit('anime_irl')
    title_of_links = []
    url_links = []

    for submission in subreddit.hot(limit=50):
        title_of_links.append(submission.title)
        url_links.append(submission.url)

    submissions = dict(zip(title_of_links, url_links))

    title, url_link = random.choice(list(submissions.items())

    embed=discord.Embed(title=title, url=url_link, color=0xff0404)
    embed.set_image(url=url_link)
    await bot.say(embed=embed)

@bot.command()
async def BBB():
    its_about_that_time='https://streamable.com/fu61x'
    await bot.say(its_about_that_time)

# Always put this last!!!
bot.run(bot_token.token)
