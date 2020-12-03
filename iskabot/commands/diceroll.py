from iskabot.commands.base import BaseCommand
import random

class DiceRollCommand(BaseCommand):
    name = "diceroll"
    aliases = ["dice"]
    param_count = 0
    help_text = "Rolls a 6-sided die."

    @classmethod
    async def run(self, ctx, params):
        await ctx.channel.send(f"Dice shows: {random.randint(1, 6)}")