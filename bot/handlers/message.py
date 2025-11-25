from telegram import Update
from telegram.ext import ContextTypes
from bot.services.user import get_user

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user_id = update.message.from_user.id
        text = update.message.text
    elif update.callback_query:
        user_id = update.callback_query.from_user.id
        text = update.callback_query.data
        await update.callback_query.answer()
    else:
        return

    if text == "Ballarni ko'rish":
        user = get_user(user_id)
        points = user.get("points", 0) if user else 0
        first_point = user.get("firstPoint", False) if user else False
        await update.effective_message.reply_text(f"Sizning ballaringiz: {points+ (1 if first_point else 0)}")
    elif text == "Link yaratish":
        await update.effective_message.reply_text("Siz Tugma B ni bosdingiz!")
