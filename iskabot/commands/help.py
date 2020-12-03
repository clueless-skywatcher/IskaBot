from iskabot.commands import *
import discord

class HelpCommand(BaseCommand):
    name = "help"
    help_text = '''
    Produces a help text listing all bot commands. 
    If a command name is provided, it shows help for only that command
    '''
    param_count = 1

    @classmethod
    async def call(self, ctx, params):
        if len(params) > self.param_count:
            await ctx.channel.send(f"Wrong command syntax")
            return
        await self.run(ctx, params)

    @classmethod
    async def run(self, ctx, params):
        commands = BaseCommand.__subclasses__()
        if len(params) > 0:
            cmd_name = params[0]
            cmd_found = False
            for cmd in commands:
                if cmd.name == cmd_name or cmd_name in cmd.aliases:
                    embed = discord.Embed(
                        title="Help: " + ", ".join([cmd.name] + cmd.aliases),
                        description=cmd.help_text,
                        colour=discord.Colour.blue()
                    )
                    cmd_found = True
                    break
            if cmd_found == False:
                await ctx.channel.send("No help was found on this command.")
        else:
            embed = discord.Embed(
                title="Commands documentation",
                description="Here are all the help commands",
                colour=discord.Colour.blue()
            )
            for c in commands:
                embed.add_field(
                    name = ",".join([c.name] + c.aliases),
                    value = c.help_text,
                    inline = False
                )
            embed.set_footer(text="Made with :love:")

        await ctx.send(embed = embed)
