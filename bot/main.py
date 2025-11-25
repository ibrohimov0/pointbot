from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.config import BOT_TOKEN
from bot.handlers.start_handler import start
from bot.handlers.invite_handler import invite_handler
from bot.handlers.new_member_handler import new_member
from bot.handlers.error_handler import error_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, invite_handler))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))

    app.add_error_handler(error_handler)

    print("Bot ishlayapti...")
    app.run_polling()

if __name__ == "__main__":
    main()