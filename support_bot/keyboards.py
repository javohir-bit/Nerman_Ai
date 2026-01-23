from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_category_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🛠 Platforma", callback_data='cat_platform'),
            InlineKeyboardButton("🎬 Video", callback_data='cat_video'),
        ],
        [
            InlineKeyboardButton("🤖 AI", callback_data='cat_ai'),
            InlineKeyboardButton("🔐 Akkaunt", callback_data='cat_account'),
        ],
        [
            InlineKeyboardButton("💳 To'lov", callback_data='cat_payment'),
            InlineKeyboardButton("🧪 Boshqa", callback_data='cat_other'),
        ],
        [
            InlineKeyboardButton("📝 Support'ga yozish", url='https://t.me/Nerman_bot'),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_support_keyboard():
    keyboard = [
        [InlineKeyboardButton("📝 Support'ga yozish", url='https://t.me/Nerman_bot')],
        [InlineKeyboardButton("◀️ Ortga", callback_data='back_to_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)
