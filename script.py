import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Function to get a random quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = f'"{data[0]["q"]}" - {data[0]["a"]}'
    return quote

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Type /quote to get a motivational quote!")

# /quote command handler
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_quote())

# Main function to start the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token("7624300048:AAEG01YrQ2nwvDSD3gCDtskvepD8mEyJqGg").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))

    print("Bot is running...")
    app.run_polling()
