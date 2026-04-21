# ============================================================
#  database.py  —  SQLite bilan ishlash
# ============================================================

import sqlite3
from config import DB_FILE


def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Jadvallarni yaratish (agar mavjud bo'lmasa)."""
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                user_id     INTEGER PRIMARY KEY,
                username    TEXT,
                full_name   TEXT,
                referred_by INTEGER,          -- kim taklif qildi
                joined_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                rewarded    INTEGER DEFAULT 0  -- final link yuborildimi
            );

            CREATE TABLE IF NOT EXISTS referrals (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id INTEGER NOT NULL,  -- taklif qilgan
                referred_id INTEGER NOT NULL,  -- taklif qilingan
                joined_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(referred_id)
            );
        """)


# ── Foydalanuvchi operatsiyalari ──────────────────────────────

def get_user(user_id: int):
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()


def add_user(user_id: int, username: str, full_name: str, referred_by: int = None):
    """Yangi foydalanuvchi qo'shish. Agar mavjud bo'lsa — o'tkazib yuborish."""
    with get_conn() as conn:
        conn.execute(
            """
            INSERT OR IGNORE INTO users (user_id, username, full_name, referred_by)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, username, full_name, referred_by),
        )


# ── Referral operatsiyalari ───────────────────────────────────

def add_referral(referrer_id: int, referred_id: int):
    """Referral yozuvini qo'shish."""
    with get_conn() as conn:
        try:
            conn.execute(
                "INSERT OR IGNORE INTO referrals (referrer_id, referred_id) VALUES (?, ?)",
                (referrer_id, referred_id),
            )
        except sqlite3.IntegrityError:
            pass


def count_referrals(user_id: int) -> int:
    """Foydalanuvchining taklif qilgan do'stlari soni."""
    with get_conn() as conn:
        row = conn.execute(
            "SELECT COUNT(*) as cnt FROM referrals WHERE referrer_id = ?",
            (user_id,),
        ).fetchone()
        return row["cnt"] if row else 0


def is_rewarded(user_id: int) -> bool:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT rewarded FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()
        return bool(row and row["rewarded"])


def mark_rewarded(user_id: int):
    with get_conn() as conn:
        conn.execute(
            "UPDATE users SET rewarded = 1 WHERE user_id = ?", (user_id,)
        )
