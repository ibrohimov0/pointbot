from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from bot.services.user import get_user, create_user, add_point

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    username = update.effective_user.username
    args = context.args

    if args:
        referrer_id = int(args[0])
        add_point(referrer_id)

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

    reply_keyboard = [["Ballarni ko'rish", "Link yaratish"]]
    reply_markup_input = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Sizga yordamchi tugmalar:",
        reply_markup=reply_markup_input
    )