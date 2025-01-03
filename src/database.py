import sqlite3

def init_db():
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS replies (
            id INTEGER PRIMARY KEY,
            tweet_id TEXT,
            user TEXT,
            user_followers_count INTEGER,
            user_verified BOOLEAN,
            text TEXT,
            number_of_characters INTEGER,
            lang TEXT,
            created_at TEXT,
            reply TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_reply(tweet_id, user, user_followers_count, user_verified, text, number_of_characters, lang, created_at, reply):
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO replies (
            tweet_id, user, user_followers_count, user_verified, text, 
            number_of_characters, lang, created_at, reply
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (tweet_id, user, user_followers_count, user_verified, text, number_of_characters, lang, created_at, reply))
    conn.commit()
    conn.close()

def has_replied(tweet_id):
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM replies WHERE tweet_id = ?", (tweet_id,))
    result = c.fetchone()
    conn.close()
    return result is not None