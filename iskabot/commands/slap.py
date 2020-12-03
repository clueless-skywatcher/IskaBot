from iskabot.commands.base import BaseCommand
from iskabot.api.tenor_api import TenorFetcher, TenorException, TenorGIFNotFoundException
from discord.embeds import Embed
import discord

from decouple import config

class SlapCommand(BaseCommand):
    name = "slap"
    param_count = 1
    help_text = "Helps the author slap a mentioned member"
    tenor_api = TenorFetcher(config("TENOR_API_KEY"))

    @classmethod
    async def run(self, ctx, params):
        slapped = params[0]
        gif = self.tenor_api.search_gif("anime slap")
        embed = Embed(
            description = f"{ctx.author.mention} slapped {slapped}",
            colour = discord.Colour.blue()
        )
        embed.set_image(url = gif)
        await ctx.send(embed = embed)
