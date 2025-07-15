from typing import Any
class Final:
    pass

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
from Michela_responder import get_Michela_response
from Tadpole_responder import get_Tadpole_response

#is step 0, load token
load_dotenv()
#TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
TOKEN: str = os.getenv('DISCORD_TOKEN')
SERVER: str = os.getenv('DISCORD_SERVER')

GUILD_ID = discord.Object(SERVER)

print(TOKEN)



class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

        # Sync commands with Discord
        try:
            #synced = await self.tree.sync(guild=GUILD_ID)
            #print(f"Synced {len(synced)} command(s) to guild {GUILD_ID.id}")


            synced = await self.tree.sync()
            print(f"Globally synced {len(synced)} command(s)")


        except Exception as e:
            print(f"Failed to sync commands: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('helllo'):
            await message.channel.send(f'Hi there {message.author}')

    #async def on_reaction_add(self, reaction, user):
    #    await reaction.message.channel.send('You reacted')


#intents: Intents = Intents.default()
intents = discord.Intents.default()
intents.message_content = True   #this is to be toggleable depending whether or not I'm on the server

client = Client(command_prefix="!", intents=intents)


@client.tree.command(
    name="tadpole",
    description="Tadpole Steno Theory",
    #guild=GUILD_ID
)
@app_commands.describe(
    lookup="word or raw steno",
    info_type="1: summarise, 2: explain, 3: list all"
)
async def tadpoleResponse(
    interaction: discord.Interaction,
    lookup: str,
    info_type: int = 2  # Default value set here
):
    response = get_Tadpole_response(lookup, info_type)
    await interaction.response.send_message(response)


@client.tree.command(
    name="michela",
    description="English Michela Phonetic Steno Theory for Piano/CharaChorder",
    #guild=GUILD_ID
)
@app_commands.describe(
    lookup="word or raw steno",
    info_type="1: summarise, 2: explain, 3: list all"
)
async def michelaResponse(
    interaction: discord.Interaction,
    lookup: str,
    info_type: int = 2  # Default value set here
):
    response = get_Michela_response(lookup, info_type)
    await interaction.response.send_message(response)


def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()

"""
async def send_message(message:Message, user_message:str) -> None:
    if not user_message:
        #print('message was empty')
        return

    if not user_message.startswith(":>"):
        #print('message was irrelevant')
        return

    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        response:str = get_response(user_message)
        await message.author.send(response) if is_private else  await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')



@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)



def main() -> None:
    client.run(TOKEN)


if __name__ == '__main__':
    main()
"""