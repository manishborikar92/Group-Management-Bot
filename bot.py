from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the /start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Hello {user.first_name}! I'm your group management bot. Use /help to see what I can do.")

# Define the /help command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Here are some commands you can use:\n/start - Start the bot\n/help - Show this help message")

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("YOUR_BOT_TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
