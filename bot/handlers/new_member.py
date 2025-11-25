from telegram import Update
from telegram.ext import ContextTypes
from bot.services.invite_service import find_invite_owner, increase_invite_usage
from bot.services.user_service import add_point

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.new_chat_members and msg.invite_link:
        link = msg.invite_link.invite_link

        owner_id = find_invite_owner(link)

        if owner_id:
            add_point(owner_id)
            increase_invite_usage(link)

            try:
                await context.bot.send_message(
                    owner_id, "🎉 Sizning link orqali yangi odam qo‘shildi! +1 point"
                )
            except:
                pass