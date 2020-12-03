from iskabot.commands.base import BaseCommand

class PingCommand(BaseCommand):
    name = "ping"
    param_count = 0
    help_text = "Pings the bot. Also returns the latency"

    @classmethod
    async def run(self, ctx, args):
        await ctx.channel.send(f"Pong! Latency: {round(ctx.bot.latency * 1000)}ms")