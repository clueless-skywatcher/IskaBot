class BaseCommand():
    name = "base"
    help_text = "Base class for all commands for this bot"
    aliases = []
    param_count = 0

    @classmethod
    async def call(self, ctx, params):
        if len(params) != self.param_count:
            await ctx.channel.send(f"Wrong command syntax")
            return
        await self.run(ctx, params)

    @classmethod
    async def run(self, ctx, params):
        pass