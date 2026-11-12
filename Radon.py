import sys
import discord
import subprocess
import os

if len(sys.argv) < 2:
    print("Error: No bot token provided!")
    sys.exit(1)

TOKEN = sys.argv[1]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    # FIX: Define 'content' so commands can be evaluated properly
    content = message.content.strip()

    if content == "!status":
        await message.channel.send("Online")
        return

    elif content == "!screenshot":
        try:
            import mss
            with mss.mss() as sct:
                sct.shot(output="/tmp/screenshot.png")
            with open("/tmp/screenshot.png", "rb") as f:
                await message.channel.send("Here is the current screen:", file=discord.File(f, "screenshot.png"))
        except Exception as e:
            await message.channel.send(f"Failed to take screenshot: {e}")
        return
        
    elif content.startswith("!terminal"):
        term_cmd = content.replace("!terminal", "", 1).strip()
        if not term_cmd:
            term_cmd = "bash"
        
        try:
            env_cmd = f"export DISPLAY=:0 && gnome-terminal -- bash -c '{term_cmd}; exec bash'"
            subprocess.run(env_cmd, shell=True)
            await message.channel.send("Terminal window spawned on desktop!")
        except Exception as e:
            await message.channel.send(f"Could not open terminal: {e}")
        return

    elif content.startswith("!run "):
        command = content.replace("!run ", "", 1)
        result = subprocess.run(command, capture_output=True, shell=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        await message.channel.send(f"```{output[:1900]}```" if output else "Executed with no output!")

client.run(TOKEN)
