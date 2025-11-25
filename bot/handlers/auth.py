from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

authenticated_users = set()
async def auth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Iltimos: /auth <username> <password> formatida kiriting.")
        return

    username, password = args[0], args[1]

    if username == "admin" and password == "n1sn4q2f5enlom825u07q237":
        authenticated_users.add(update.effective_user.id)
        await update.message.reply_text("Siz muvaffaqiyatli autentifikatsiyadan o‘tdingiz!")
    else:
        await update.message.reply_text("Login yoki parol noto‘g‘ri!")

async def send_groups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    if tg_id not in authenticated_users:
        await update.message.reply_text("Iltimos, avval /auth orqali kiriting.")
        return

    # Guruhlar ro'yxati (keyinchalik DB dan olish mumkin)
    groups = [
        {"name": "Guruh 1", "url": "https://t.me/foydali_link_0"},
        {"name": "Guruh 2", "url": "https://t.me/foydali_link_1"},
        {"name": "Guruh 3", "url": "https://t.me/foydali_link_2"},
    ]

    keyboard = [
        [InlineKeyboardButton(f"📌 {g['name']}", url=g['url'])] for g in groups
    ]
    keyboard.append([InlineKeyboardButton("✅ Tekshirish", callback_data="check_subs")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Iltimos quyidagi guruhlarga obuna bo‘ling:",
        reply_markup=reply_markup
    )
