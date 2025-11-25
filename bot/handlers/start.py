from telegram import Update
from telegram.ext import ContextTypes
from bot.services.user import get_user, create_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    username = update.effective_user.username

    user = get_user(tg_id)

    if not user:
        create_user(tg_id, username)
        await update.message.reply_text(
            "Xush kelibsiz! Siz ro‘yxatdan o‘tdingiz.\nInvite link yuboring."
        )
    else:
        await update.message.reply_text("Invite link yuborishingiz mumkin.")