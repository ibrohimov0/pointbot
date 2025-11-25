from telegram import Update
from telegram.ext import ContextTypes
from bot.services.invite import save_invite
from bot.services.utils import extract_invite_link

async def invite_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    link = extract_invite_link(text)

    if link:
        tg_id = update.effective_user.id
        save_invite(tg_id, link)
        await update.message.reply_text("Invite saqlandi!")