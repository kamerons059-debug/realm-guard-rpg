import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("DISCORD_TOKEN"))
from discord import app_commands
import discord

class MainMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Stats", style=discord.ButtonStyle.primary)
    async def stats(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("📊 Stats tab coming soon!", ephemeral=True)

    @discord.ui.button(label="Inventory", style=discord.ButtonStyle.success)
    async def inventory(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("🎒 Inventory tab coming soon!", ephemeral=True)

    @discord.ui.button(label="Archive", style=discord.ButtonStyle.secondary)
    async def archive(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("📜 Archive tab coming soon!", ephemeral=True)

    @discord.ui.button(label="Avatar", style=discord.ButtonStyle.danger)
    async def avatar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("🧙 Avatar tab coming soon!", ephemeral=True)

    @discord.ui.button(label="Quests", style=discord.ButtonStyle.primary)
    async def quests(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("🗺️ Quest tab coming soon!", ephemeral=True)
      @bot.command()
async def menu(ctx):
    await ctx.send("🎮 **Realm Guard Menu**", view=MainMenu())
