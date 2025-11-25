from telegram import Update
from telegram.ext import ContextTypes
from services.user import add_first_point

async def check_subs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    groups = [
        "foydali_link_0",
    ]
    
    all_ok=True

    for group in groups:
        member = await context.bot.get_chat_member(f"@{group}", user_id)
        if member.status not in ["member", "administrator", "creator"]:
            all_ok=False

    if all_ok:
        await add_first_point(user_id)
        await query.edit_message_text("Siz barcha guruhlarga obuna bo'lgansiz! 🎉\nSizga 1 ball qo'shildi.")
    else:
        await query.edit_message_text("Iltimos, barcha guruhlarga obuna bo'ling va qayta tekshiring.")