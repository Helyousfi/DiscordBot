import discord
from discord.ext import commands

# Define the bot's command prefix
bot = commands.Bot(command_prefix='!')

# Replace with your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

# A dictionary containing product details
products = {
    "product1": {
        "name": "Product 1",
        "price": "$10.00",
        "link": "https://example.com/product1",
        "description": "Description of Product 1"
    },
    "product2": {
        "name": "Product 2",
        "price": "$20.00",
        "link": "https://example.com/product2",
        "description": "Description of Product 2"
    },
    # Add more products as needed
}

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is ready and online!')

@bot.command()
async def buy(ctx, product_name: str):
    # Check if the product exists in the dictionary
    product = products.get(product_name.lower())
    if product:
        # Construct the message
        message = (
            f"**{product['name']}**\n"
            f"Price: {product['price']}\n"
            f"{product['description']}\n"
            f"[Buy Now]({product['link']})"
        )
        # Send the user a private message with the product details
        await ctx.author.send(message)
        await ctx.send(f"{ctx.author.mention}, I've sent you a private message with the details!")
    else:
        await ctx.send(f"{ctx.author.mention}, sorry, I couldn't find that product!")

# Run the bot
bot.run(TOKEN)
