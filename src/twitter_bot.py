import tweepy
from src.config import consumer_key, consumer_secret, access_token, access_token_secret
from src.database i mport save_reply, has_replied
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_variation():
    variations = [
        "Avi Yemini is a convicted domestic abuser. He assaulted his ex-wife with a chopping board, sent abusive texts, and terrorized her. She said, ‘I was a vessel for his hatred.’ Don’t let him rewrite history. Details: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Reminder: Avi Yemini is a convicted wife beater. He threw a chopping board at his ex-wife, called her vile names in texts, and terrorized her. She described it as ‘years of fear.’ Sources: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Avi Yemini is a domestic abuser who hit his ex-wife with a chopping board, leaving her injured. He harassed her for years with vile texts. She said, ‘I was nothing but a vessel for his hatred.’ Sources: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Don’t forget: Avi Yemini is a convicted abuser. He attacked his ex-wife, sent her disgusting texts for over a year, and left her terrorized. She said, ‘He didn’t care when I was hurt.’ Sources: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Avi Yemini’s violent past is clear: he assaulted his ex-wife with a chopping board, called her a ‘P.O.S.’ in vile texts, and terrorized her for years. He’s a domestic abuser. Details: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Fact: Avi Yemini is a convicted domestic abuser. He hit his ex-wife, sent her vile, abusive texts, and ignored her injuries. His ex-wife said, ‘He terrorized me for years.’ Don’t let him hide. Details: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Avi Yemini admitted to assaulting his ex-wife with a chopping board and sending abusive texts for over a year. She described years of terror, saying, ‘I was just a vessel for his hatred.’ Yemini is a domestic abuser. Sources: tinyurl.com/avi-smh, tinyurl.com/AY-wiki.",
        "Avi Yemini’s ex-wife said, ‘He terrorized me for years, treating me as a vessel for his hatred.’ Yemini assaulted her with a chopping board and harassed her with vile texts. He is a convicted domestic abuser. Sources: tinyurl.com/avi-smh, tinyurl.com/AY-wiki.",
        "Avi Yemini: convicted for hitting his ex-wife with a chopping board and abusing her via text for years. She said, ‘He terrorized me.’ He is a domestic abuser hiding behind outrage. Details: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot.",
        "Avi Yemini assaulted his ex-wife with a chopping board, harassed her with disgusting texts, and terrorized her during their marriage. He is a convicted wife beater. Don’t let him escape accountability. Details: tinyurl.com/avi-smh, tinyurl.com/AY-wiki, tinyurl.com/avidiot."
    ]
    return random.choice(variations)

def reply_to_mentions():
    mentions = api.mentions_timeline()
    for mention in mentions:
        if not has_replied(mention.id_str):
            reply_text = get_variation()
            api.update_status(status=reply_text, in_reply_to_status_id=mention.id_str)
            save_reply(mention.id_str, mention.user.screen_name, mention.text, reply_text)

def reply_to_hashtags():
    hashtags = ["#aviyemini", "#griftingmidget", "#wifebeater", "#RebelNews"]
    for hashtag in hashtags:
        try:
            for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, tweet_mode='extended', result_type='recent').items(10):
                if not has_replied(tweet.id_str):
                    reply_text = get_variation()
                    api.update_status(status=reply_text, in_reply_to_status_id=tweet.id_str)
                    save_reply(tweet.id_str, tweet.user.screen_name, tweet.full_text, reply_text)
        except tweepy.TweepyException as e:
            logger.error(f"Error processing hashtag {hashtag}: {e}")