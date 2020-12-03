from iskabot.commands.base import BaseCommand
import random

DEFEATS_DICT = {
    "rock" : "scissors",
    "scissors" : "paper",
    "paper" : "rock"
}

class RockPaperScissorsCommand(BaseCommand):
    name = "rockpaperscissors"
    aliases = ["rps"]
    param_count = 1
    help_text = "Plays a game of rock-paper-scissors."

    @classmethod
    async def run(self, ctx, params):
        rps = params[0]
        if rps not in DEFEATS_DICT:
            await ctx.channel.send(f"Sorry, wrong parameter. Must be either of 'rock', 'paper' or 'scissors'.")
            return
        rps_pc = random.choice(list(DEFEATS_DICT.keys()))
        await ctx.channel.send(f"Iska rolled {rps_pc}")
        if DEFEATS_DICT[rps] == rps_pc:
            await ctx.channel.send(f"Nice {ctx.author.mention}! You won!")
        elif DEFEATS_DICT[rps_pc] == rps:
            await ctx.channel.send(f"Haha {ctx.author.mention}! I win!")
        else:
            await ctx.channel.send(f"Let's go again! Shall we {ctx.author.mention}?")
