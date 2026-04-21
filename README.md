# 🤖 Telegram Referral Bot — To'liq Qo'llanma

## 📁 Fayl tuzilmasi

```
telegram_bot/
├── bot.py           ← asosiy mantiq
├── database.py      ← SQLite operatsiyalari
├── config.py        ← SOZLAMALAR (shu faylni to'ldiring)
├── requirements.txt ← kutubxonalar
└── bot.db           ← avtomatik yaratiladi
```

---

## ⚙️ 1-QADAM: Bot Token olish

1. Telegramda **@BotFather** ga yozing
2. `/newbot` → botga nom bering → username bering
3. Token oling: `123456789:ABCdef...`
4. `config.py` da `BOT_TOKEN` ga yozing

---

## 📢 2-QADAM: Kanal ID larini topish

Bot kanallar a'zoligini tekshirishi uchun:

### Har bir kanalga botni admin qiling:
1. Kanal sozlamalari → Adminlar → Bot qo'shing
2. **"A'zolarni boshqarish"** huquqini bering

### Kanal ID ni aniqlash:

**Usul 1 — @userinfobot orqali:**
1. Kanalga `@userinfobot` ni forward qiling
2. U kanal ID ni ko'rsatadi (masalan: `-1001234567890`)

**Usul 2 — Oddiy usul:**
1. Botni ishga tushiring
2. Kanalga istalgan xabar yuboring
3. `https://api.telegram.org/bot<TOKEN>/getUpdates` ga browser orqali kiring
4. `chat.id` ni toping

### config.py ga yozing:
```python
REQUIRED_CHANNELS = [
    {
        "id": -1001234567890,   # ← shu yerga
        "link": "https://t.me/+WcdtRNyDSlE2MTkx",
        "name": "Kanal 1",
    },
    ...
]
```

> ⚠️ **Muhim:** Private kanallarda ham bot admin bo'lishi **shart**!

---

## 💻 3-QADAM: O'rnatish va ishga tushirish

### Python o'rnatish (agar yo'q bo'lsa):
Python 3.10+ kerak → https://python.org/downloads

### Kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

### Botni ishga tushirish:
```bash
python bot.py
```

---

## 🔄 Bot oqimi (Flow)

```
User /start bosadi
        │
        ▼
3 ta kanalga a'zo?
   │           │
  YO'Q        HA
   │           │
   ▼           ▼
Kanallar   Referral havolasi
ko'rsatiladi  yuboriladi
   │
   ▼
"Tekshirish" tugmasi
   │
   ▼ (agar hammasi ✅)
Referral havolasi yuboriladi
        │
        ▼
Har bir do'st /start?start=refXXX bosadi
        │
        ▼
Taklif qilganga: "Do'stingiz qo'shildi (N/3)" xabari
        │
        ▼ (3 ta to'ldi)
Final kanal linki yuboriladi 🎁
```

---

## 🛑 Server (VPS) da 24/7 ishlatish

### systemd service (Linux):
```bash
sudo nano /etc/systemd/system/mybot.service
```

```ini
[Unit]
Description=Telegram Referral Bot
After=network.target

[Service]
User=root
WorkingDirectory=/home/ubuntu/telegram_bot
ExecStart=/usr/bin/python3 /home/ubuntu/telegram_bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable mybot
sudo systemctl start mybot
sudo systemctl status mybot
```

---

## 🐞 Tez-tez uchraydigan xatolar

| Xato | Sabab | Yechim |
|------|-------|--------|
| `ChatMember not found` | Bot kanal admini emas | Botni admin qiling |
| `Forbidden: bot was blocked` | Foydalanuvchi botni bloklagan | O'tkazib yuborish (try/except bor) |
| `Invalid token` | Token noto'g'ri | @BotFather dan qayta oling |
| `0 referral` | Bot private kanalga admin emas | Har 3 ta kanalga admin qiling |

---

## 📋 Buyruqlar

| Buyruq | Vazifasi |
|--------|----------|
| `/start` | Botni boshlash / a'zolikni tekshirish |
| `/referral` | Havolani qayta ko'rish |
