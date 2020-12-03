from iskabot.commands.base import BaseCommand
import random

class CoinFlipCommand(BaseCommand):
    name = "coinflip"
    aliases = ["cf"]
    param_count = 0
    help_text = "Flips a coin"

    @classmethod
    async def run(self, ctx, args):
        await ctx.channel.send(f"Flipping the coin")
        await ctx.channel.send(f"The result is {random.choice(['Heads', 'Tails'])}")