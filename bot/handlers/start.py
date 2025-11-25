from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.services.user import get_user, create_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    username = update.effective_user.username

    user = get_user(tg_id)

    if not user:
        create_user(tg_id, username)

    keyboard = [
        [
            InlineKeyboardButton("📌 Guruh 1", url="https://t.me/foydali_link_0"),
        ],
        [
            InlineKeyboardButton("✅ Tekshirish", callback_data="check_subs"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Xush kelibsiz! Siz ro‘yxatdan o‘tdingiz.\nIltimos guruhlarga obuna bo'ling hamda 1 ball yutib oling.",reply_markup=reply_markup)