import discord
import asyncio
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class aClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        await self.change_presence(status=discord.Status.dnd, activity=discord.Game('e resolvendo ticket'))
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1234971398511001711))
            self.synced = True
        print(f'Logado como {self.user}')

client = aClient()
tree = app_commands.CommandTree(client)

class TicketView(discord.ui.View):
    def __init__(self, creator_info: dict, message: discord.Message):
        super().__init__(timeout=None)
        self.creator_info = creator_info
        self.message = message # Message information

    @discord.ui.button(label="Não Resolvido", style=discord.ButtonStyle.danger, custom_id="not_resolved")
    async def not_resolved_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        # Change the button style to indicate that the ticket is unresolved
        self.children[0].style = discord.ButtonStyle.success
        self.children[0].label = "Resolvido"
        self.children[0].disabled = True

        # Update the view to disable the button
        await interaction.message.edit(view=self)

message_creators = {}

@tree.command(guild=discord.Object(id=1234971398511001711), name='ticket', description='Abrir um ticket de suporte')
@app_commands.describe(ticket='Descrição do problema', produto='Produto relacionado', compra='ID da compra', email='Email associado', motivo='Motivo do ticket')
async def ticket(interaction: discord.Interaction, ticket: str, produto: str, compra: str, email: str, motivo: str):
    user = interaction.user
    embed = discord.Embed(title="Ticket de Suporte", color=0xFFA500)
    embed.add_field(name="Ticket",value=ticket, inline=False)
    embed.add_field(name="Produto", value=produto, inline=False)
    embed.add_field(name="ID da Compra", value=compra, inline=False)
    embed.add_field(name="Email", value=email, inline=False)
    embed.add_field(name="Motivo", value=motivo, inline=False)
    embed.description = f'O moderador {user.mention} criou uma nova solicitação'
    embed.set_footer(text="Clique no botão abaixo para marcar o ticket como resolvido.")

    # Directly passes creator information to TicketView
    view = TicketView(creator_info={
        "user_id": user.id,
    }, message=None)
    
    message = await interaction.response.send_message(embed=embed, view=view)
    message_creators[message.id] = {
        "user_id": user.id,
        "message_content": embed.description
    }
async def main():
    token = "YOUR_TOKEN" # Change your token bot
    await client.start(token)

if __name__ == "__main__":
    asyncio.run(main())
