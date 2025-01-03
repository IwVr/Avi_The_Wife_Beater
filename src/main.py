from src.twitter_bot import reply_to_mentions, reply_to_hashtags
from src.database import init_db

def main():
    init_db()
    reply_to_mentions()
    reply_to_hashtags()

if __name__ == "__main__":
    main()