#!/usr/bin/env python3

import praw # type: ignore
import os

from discord import Intents, Client, Message
from dotenv import load_dotenv

load_dotenv()

"""Load API Keys"""
praw_client_id = os.getenv("PRAW_CLIENT_ID")
praw_client_secret = os.getenv("PRAW_CLIENT_SECRET")
praw_user_agent = os.getenv("PRAW_USER_AGENT")

discord_api_token = os.getenv("DISCORD_API_TOKEN")
discord_app_id = os.getenv("DISCORD_APP_ID")
discord_user_name = os.getenv("DISCORD_USER_NAME")

intents: Intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Authorizing Reddit API
# redditbot = praw.Reddit(client_id=praw_client_id,
#                         client_secret=praw_client_secret,
#                         user_agent=praw_user_agent)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

def main() -> None: 
    client.run(token=discord_api_token)

if __name__ == '__main__':
    main()
