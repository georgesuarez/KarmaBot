#!/usr/bin/env python3

import discord
import praw 
import os

from discord import Intents, Client, app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Client(commands.Bot):
    async def on_ready(self):
        print('Logged in')
        print(f'Name: {self.user}')
        print(f'ID: {discord_app_id}')
        print(f'Discord.py version: {discord.__version__}')
        print('========')
        await client.change_presence(status=discord.Status.online, activity=game)
        
        try:
            guild = discord.Object(id=313180439483252737)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")


    async def on_message(self, message):
        """
        Greets a user when they send a message.
    
        """
        if message.author == client.user:
            return

        if message.content.lower() in ["hello", "hi", "hey"]:
            await message.channel.send(f"Hello, {message.author.mention}!")


   

""" Load API Keys """
praw_client_id = os.getenv("PRAW_CLIENT_ID")
praw_client_secret = os.getenv("PRAW_CLIENT_SECRET")
praw_user_agent = os.getenv("PRAW_USER_AGENT")

discord_api_token = os.getenv("DISCORD_API_TOKEN")
discord_app_id = os.getenv("DISCORD_APP_ID")
discord_user_name = os.getenv("DISCORD_USER_NAME")

intents: Intents = Intents.default()
intents.message_content = True
client = Client(command_prefix='!', intents=intents)

# Changing the activity of the bot in discord
game = discord.Game("Hello World!")

# Authorizing Reddit API
# redditbot = praw.Reddit(client_id=praw_client_id,
#                         client_secret=praw_client_secret,
#                         user_agent=praw_user_agent)

GUILD_ID = discord.Object(id=313180439483252737)

ALLOWED_USERS = {274042160855121921}

@client.tree.command(name="get_id", description="Get Discord User ID", guild=GUILD_ID)
async def get_id(interaction: discord.Interaction, member: discord.Member = None):
    if member is None:
        member = interaction.message.author
    await interaction.response.send_message(f"{member.display_name}'s ID is `{member.id}`")

@client.tree.command(name="clear", description="Clear messages given a number.", guild=GUILD_ID)
async def clear(interaction: discord.Interaction, amount: int):
    """
    Deletes the specified number of messages in the channel.
    Only allowed users can use this command.
    Usage: !clear <number>

    """
    
    # if interaction.message.author.id not in ALLOWED_USERS:
    #     await interaction.channel.send("You are not authorized to use this command.", delete_after=5)
    #     return

    if amount < 1:
        await interaction.response.defer()
        await interaction.response.send_message("Please specify a number greater than 0.", delete_after=5)
        return

    deleted = await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"Deleted {len(deleted)} messages.", delete_after=3)

def main() -> None: 
    client.run(token=discord_api_token)

if __name__ == '__main__':
    main()
