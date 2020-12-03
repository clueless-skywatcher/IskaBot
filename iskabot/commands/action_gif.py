from iskabot.commands.base import BaseCommand
from iskabot.api.tenor_api import TenorFetcher, TenorException, TenorGIFNotFoundException
from discord.embeds import Embed
import discord

from decouple import config

class ActionGIFCommand(BaseCommand):
    param_count = 1
    tenor_api = TenorFetcher(config("TENOR_API_KEY"))
    search_key = ""
    description = ""

    @classmethod
    def parse_description(self, *args):
        pass

    @classmethod
    async def run(self, ctx, params):
        param = params[0]
        gif = self.tenor_api.search_gif(self.search_key)
        embed = Embed(
            description = self.parse_description(ctx.author.mention, param),
            colour = discord.Colour.blue()
        )
        embed.set_image(url=gif)
        await ctx.channel.send(embed = embed)

class SlapCommand(ActionGIFCommand):
    name = "slap"
    help_text = "Helps the author slap a mentioned member"
    search_key = "anime slap"

    @classmethod
    def parse_description(self, slapper, slapped):
        return f"{slapper} slapped {slapped}"

class PunchCommand(ActionGIFCommand):
    name = "punch"
    help_text = "Helps the author punch a mentioned member"
    search_key = "anime punch"

    @classmethod
    def parse_description(self, puncher, punched):
        return f"{puncher} punched {punched}"

class KickCommand(ActionGIFCommand):
    name = "kick"
    help_text = '''
    Helps the author kick a mentioned member. 
    NOT to be confused with server kick, which is done by the skick command.
    '''
    search_key = "anime kick"

    @classmethod
    def parse_description(self, kicker, kicked):
        return f"{kicker} kicked {kicked}"

class HugCommand(ActionGIFCommand):
    name = "hug"
    help_text = "Helps the author hug a mentioned member"
    search_key = "anime hug"

    @classmethod
    def parse_description(self, hugger, hugged):
        return f"{hugger} hugged {hugged}"

class KissCommand(ActionGIFCommand):
    name = "hug"
    help_text = "Helps the author kiss a mentioned member"
    search_key = "anime kiss"

    @classmethod
    def parse_description(self, hugger, hugged):
        return f"{hugger} kissed {hugged}"