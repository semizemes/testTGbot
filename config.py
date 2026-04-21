# ============================================================
#  config.py  —  Bot sozlamalari (faqat shu faylni o'zgartiring)
# ============================================================

# 1. @BotFather dan olgan token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# 2. Majburiy kanallar
#    id  →  bot admin bo'lishi kerak bo'lgan kanal ID
#    Kanal ID ni qanday topish: pastdagi README ga qarang
REQUIRED_CHANNELS = [
    {
        "id": -1001234567890,          # <-- kanal ID (manfiy son)
        "link": "https://t.me/+WcdtRNyDSlE2MTkx",
        "name": "Kanal 1",
    },
    {
        "id": -1009876543210,          # <-- kanal ID
        "link": "https://t.me/Dilbarkhon_Mansurovna",
        "name": "Dilbarkhon Mansurovna",
    },
    {
        "id": -1001122334455,          # <-- kanal ID
        "link": "https://t.me/+b0_CsM93ckljMTA6",
        "name": "Kanal 3",
    },
]

# 3. Oxirida yuboriladigan kanal linki
FINAL_CHANNEL_LINK = "https://t.me/Welcome_toHell_z"

# 4. Nechta do'st taklif qilish kerak
REFERRAL_REQUIRED = 3

# 5. SQLite fayl nomi
DB_FILE = "bot.db"
