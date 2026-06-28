import discord
from discord.ext import commands
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='help', description='View useful information about the bot.')
    async def help(self, interaction: discord.Interaction):
        overview = (
            "Etherial is a competitive PvP utility bot for Etheria Restart, created to help players\n"
            "master the arena through optimized builds, matchup analysis, counter recommendations,\n"
            "and meta-focused insights. Build for serious competitors and unions looking to gain\n"
            "every possible advantage!"
        )
        
        commands = (
            "/help - View useful information about the bot.",
            "/build - View build recommendations for the selected animus.",
            "/team - View team recommendations for the selected animus.",
            "/counter - View counters for the selected animus.",
            "/compare - View a comparison of two selected animus.",
            "/speedtune - View speed tuning recommendations for the selected team.",
            "/draft - View ban recommendations for the selected enemy draft picks."
        )

        contact = (
            "Please contact bl4ckh4wkttv.gaming@gmail.com for additional support.\n"
            "Feel free to also provide suggestions/feedback about the bot in general,\n"
            "or to suggest edits to inaccurate information to better the experience."
        )
        
        embed = discord.Embed(title='Etherial Support', description=overview)
        
        if self.bot.user:
            embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        
        embed.add_field(name='Commands', value=commands)
        embed.add_field(name='Contact', value=contact)
        
        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    await bot.add_cog(HelpCog(bot))