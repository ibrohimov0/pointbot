from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot.config import BOT_TOKEN

from bot.handlers.start import start
from bot.handlers.check_subs import check_subs
from bot.handlers.error import error_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_subs, pattern="check_subs"))
    app.add_error_handler(error_handler)

    print("Working...")
    app.run_polling()

if __name__ == "__main__":
    main()