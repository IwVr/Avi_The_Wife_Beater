import unittest
from unittest.mock import patch, MagicMock
from src.twitter_bot import get_variation, reply_to_mentions, reply_to_hashtags
from src.database import save_reply, has_replied, init_db
import tweepy
import re

class TestTwitterBot(unittest.TestCase):

    def setUp(self):
        # Initialize the database for testing
        init_db()

    def test_get_variation(self):
        # Test that get_variation returns a string
        variation = get_variation()
        self.assertIsInstance(variation, str)
        self.assertTrue(len(variation) > 0)

    @patch('src.twitter_bot.api')
    def test_reply_to_mentions(self, mock_api):
        # Mock mentions_timeline to return a list of mock tweets
        mock_tweet = MagicMock()
        mock_tweet.id_str = '12345'
        mock_tweet.user.screen_name = 'test_user'
        mock_tweet.user.followers_count = 100
        mock_tweet.user.verified = False
        mock_tweet.full_text = 'Test mention full text'
        mock_tweet.lang = 'en'
        mock_tweet.created_at = MagicMock()
        mock_tweet.created_at.strftime.return_value = '2023-10-01 12:00:00'
        mock_api.mentions_timeline.return_value = [mock_tweet]

        # Mock has_replied to return False
        with patch('src.twitter_bot.has_replied', return_value=False):
            reply_to_mentions()

        # Check that update_status was called
        mock_api.update_status.assert_called_once()

    @patch('src.twitter_bot.tweepy.Cursor')
    @patch('src.twitter_bot.api')
    def test_reply_to_hashtags(self, mock_api, mock_cursor):
        # Create a mock tweet
        mock_tweet = MagicMock()
        mock_tweet.id_str = '67890'
        mock_tweet.user.screen_name = 'test_user_hashtag'
        mock_tweet.user.followers_count = 250
        mock_tweet.user.verified = True
        mock_tweet.full_text = 'Test hashtag full text'
        mock_tweet.lang = 'en'
        mock_tweet.created_at = MagicMock()
        mock_tweet.created_at.strftime.return_value = '2023-10-02 15:30:00'

        # Create a mock cursor instance
        mock_cursor_instance = MagicMock()
        mock_cursor_instance.items.return_value = iter([mock_tweet])
        mock_cursor.return_value = mock_cursor_instance

        # Mock has_replied to return False
        with patch('src.twitter_bot.has_replied', return_value=False):
            reply_to_hashtags()

        # Check that update_status was called
        mock_api.update_status.assert_called_once()

    def test_save_reply(self):
        # Test saving a reply to the database
        save_reply(
            tweet_id='12345',
            user='test_user',
            user_followers_count=100,
            user_verified=False,
            text='Test text',
            number_of_characters=15,
            lang='en',
            created_at='2023-10-01 12:00:00',
            reply='Test reply'
        )
        self.assertTrue(has_replied('12345'))

    def test_has_replied_false(self):
        # Test has_replied returns False for non-existent tweet_id
        self.assertFalse(has_replied('non_existent_id'))

    @patch('src.twitter_bot.api')
    def test_reply_to_mentions_no_new_mentions(self, mock_api):
        # Mock mentions_timeline to return empty list
        mock_api.mentions_timeline.return_value = []

        with patch('src.twitter_bot.has_replied', return_value=True):
            reply_to_mentions()

        # update_status should not be called
        mock_api.update_status.assert_not_called()

    @patch('src.twitter_bot.api')
    def test_reply_to_hashtags_exception(self, mock_api):
        # Simulate TweepyException when searching tweets
        mock_api.search_tweets.side_effect = tweepy.TweepyException("API Error")

        with patch('src.twitter_bot.has_replied', return_value=False):
            with self.assertLogs('src.twitter_bot', level='ERROR') as log:
                reply_to_hashtags()
                self.assertIn("ERROR:src.twitter_bot:Error processing hashtag", log.output[0])

    @patch('src.twitter_bot.api')
    def test_reply_to_mentions_multiple_mentions(self, mock_api):
        # Mock multiple mentions
        mock_tweet1 = MagicMock()
        mock_tweet1.id_str = '11111'
        mock_tweet1.user.screen_name = 'user1'
        mock_tweet1.user.followers_count = 150
        mock_tweet1.user.verified = False
        mock_tweet1.full_text = 'First mention'
        mock_tweet1.lang = 'en'
        mock_tweet1.created_at = MagicMock()
        mock_tweet1.created_at.strftime.return_value = '2023-10-03 10:00:00'

        mock_tweet2 = MagicMock()
        mock_tweet2.id_str = '22222'
        mock_tweet2.user.screen_name = 'user2'
        mock_tweet2.user.followers_count = 200
        mock_tweet2.user.verified = True
        mock_tweet2.full_text = 'Second mention'
        mock_tweet2.lang = 'en'
        mock_tweet2.created_at = MagicMock()
        mock_tweet2.created_at.strftime.return_value = '2023-10-03 11:00:00'

        mock_api.mentions_timeline.return_value = [mock_tweet1, mock_tweet2]

        with patch('src.twitter_bot.has_replied', side_effect=[False, False]):
            reply_to_mentions()

        # update_status should be called twice
        self.assertEqual(mock_api.update_status.call_count, 2)

    @patch('src.twitter_bot.api')
    def test_reply_to_hashtags_no_new_tweets(self, mock_api):
        # Mock hashtags to return no new tweets
        mock_cursor_instance = MagicMock()
        mock_cursor_instance.items.return_value = iter([])
        mock_api.search_tweets.return_value = mock_cursor_instance

        with patch('src.twitter_bot.has_replied', return_value=False):
            reply_to_hashtags()

        # update_status should not be called
        mock_api.update_status.assert_not_called()

    def tearDown(self):
        # Clean up the database after tests
        import os
        if os.path.exists('tweets.db'):
            os.remove('tweets.db')

if __name__ == '__main__':
    unittest.main()