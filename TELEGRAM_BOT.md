# Telegram Support Bot - Setup Guide

## Overview
NERMAN.AI loyihasiga webhook orqali ishlaydigan Telegram support bot integratsiya qilindi. Bot Render.com Free plan bilan ishlaydi va polling o'rniga webhook ishlatadi.

## Environment Variable Sozlash

### Local Development
PowerShell orqali:
```powershell
$env:BOT_TOKEN="8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA"
```

Yoki `.env` faylga qo'shing:
```
BOT_TOKEN=8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA
```

### Render.com Deployment
1. Render.com dashboard'ingizga kiring
2. Service settings → Environment
3. Yangi environment variable qo'shing:
   - **Key**: `BOT_TOKEN`
   - **Value**: `8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA`

## Webhook URL O'rnatish

### Local Development (ngrok bilan)
```bash
# 1. ngrok tunnel ochish
ngrok http 8000

# 2. Webhook o'rnatish (ngrok URL'ni ishlating)
curl -X POST "https://api.telegram.org/bot8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA/setWebhook?url=https://your-ngrok-url.ngrok.io/webhook/"

# 3. Webhook statusini tekshirish
curl "https://api.telegram.org/bot8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA/getWebhookInfo"
```

### Production (Render.com)
```bash
# Webhook o'rnatish (production URL bilan)
curl -X POST "https://api.telegram.org/bot8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA/setWebhook?url=https://your-app.onrender.com/webhook/"

# Webhook statusini tekshirish
curl "https://api.telegram.org/bot8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA/getWebhookInfo"
```

## Bot Funksiyalari

### `/start` Komandasi
Foydalanuvchi bot bilan birinchi marta muloqot qilganda:
```
Assalomu alaykum! 👋

Men NERMAN.AI support boti.
Sizga qanday yordam bera olaman?
```

### Oddiy Xabarlar
Foydalanuvchi oddiy xabar yuborganda:
```
Sizning xabaringiz qabul qilindi: [xabar matni]

Tez orada support jamoamiz siz bilan bog'lanadi.
```

## Testing

### 1. Local Test
```powershell
# Environment variable o'rnatish
$env:BOT_TOKEN="8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA"

# Server ishga tushirish
python manage.py runserver
```

### 2. ngrok bilan Webhook Test
```bash
# ngrok tunnel
ngrok http 8000

# Webhook o'rnatish
curl -X POST "https://api.telegram.org/bot8484894535:AAGE2gQ3ujvnKxzK7Jhn0QK5rvl5c4xCIaA/setWebhook?url=https://abc123.ngrok.io/webhook/"
```

### 3. Telegram'da Test
1. Bot'ga `/start` komandasi yuboring
2. Oddiy xabar yuboring (masalan: "Yordam kerak")
3. Bot javob berishini tekshiring

## Troubleshooting

### ⚠️ Bot javob bermayapti
1. **BOT_TOKEN tekshirish:**
   ```bash
   echo $env:BOT_TOKEN  # Windows
   echo $BOT_TOKEN      # Linux/Mac
   ```

2. **Webhook status tekshirish:**
   ```bash
   curl "https://api.telegram.org/bot<BOT_TOKEN>/getWebhookInfo"
   ```

3. **Server loglarini tekshirish:**
   ```bash
   # Render.com'da
   Logs tab'ini oching va xatolarni o'qing
   ```

### ⚠️ CSRF Error
Webhook endpoint `/webhook/` CSRF'dan ozod qilingan (`@csrf_exempt`). Agar CSRF xatosi bo'lsa, URL routing'ni tekshiring - webhook URL `i18n_patterns`'dan **tashqarida** bo'lishi kerak.

### ⚠️ Module import error
```bash
# Dependencies o'rnatish
pip install -r requirements.txt

# Specific package
pip install python-telegram-bot>=20.0
```

### ⚠️ Webhook URL noto'g'ri
Webhook URL'da quyidagilar bo'lishi kerak:
- HTTPS (HTTP emas!)
- Public URL (localhost emas, ngrok yoki production URL)
- `/webhook/` endpoint

## Technical Details

### Files Structure
```
support_bot/
├── __init__.py          # Django app identifier
├── apps.py              # App configuration
├── bot.py               # Bot instance management
├── views.py             # Webhook handler
├── urls.py              # URL routing
└── admin.py             # Admin configuration
```

### URL Endpoints
- **Webhook**: `https://your-domain.com/webhook/`
- **Method**: POST only
- **Content-Type**: application/json

### Security
- ✓ CSRF exempt for webhook (Telegram serverlaridan keladi)
- ✓ BOT_TOKEN environment variable'da (code'da emas)
- ✓ Error handling va logging
- ✓ JSON validation

## Next Steps

1. ✅ BOT_TOKEN environment variable o'rnatish
2. ✅ Dependencies install qilish
3. ✅ Server ishga tushirish
4. ⚠️ Webhook URL o'rnatish (yuqoridagi komandalar)
5. ⚠️ Telegram'da test qilish

## Support

Muammolar yuzaga kelsa:
1. Render.com logs'ini tekshiring
2. `getWebhookInfo` API orqali webhook statusini tekshiring
3. BOT_TOKEN to'g'riligini tasdiqlang
