# Avi The Wife Beater Twitter Bot

## Description

This Twitter bot automatically replies to tweets mentioning specific keywords or hashtags related to Avi Yemini with informative messages. It aims to raise awareness by providing consistent and factual information in response to relevant tweets.

## Features

- **Automated Replies to Mentions**: Replies to tweets that mention the bot or specific keywords.
- **Automated Replies to Hashtags**: Monitors and replies to tweets containing certain hashtags.
- **Database Storage**: Stores replied tweets in a SQLite database to prevent duplicate replies.
- **Randomized Responses**: Provides varied responses to avoid repetition.
- **Rate Limiting**: Handles Twitter API rate limits gracefully.
- **Error Logging**: Logs errors and exceptions for troubleshooting.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Twitter API Setup](#twitter-api-setup)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Running Tests](#running-tests)
- [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
- [Potential Pitfalls](#potential-pitfalls)
- [References](#references)
- [License](#license)

## Prerequisites

Before setting up the bot, ensure that you have the following installed on your system:

- **Python 3.7 or higher**: The bot is developed using Python 3.
- **Virtual Environment Tool**: Such as `venv` or `virtualenv` to manage dependencies.
- **Git**: For cloning the repository.
- **SQLite**: Included with Python's standard library for database management.

## Installation

Follow these steps to install and set up the bot:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/IwVr/Avi_The_Wife_Beater
   cd Avi_The_Wife_Beater
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv avi_env
   ```

3. **Activate the Virtual Environment**:

   - On **Unix or MacOS**:

     ```bash
     source avi_env/bin/activate
     ```

   - On **Windows**:

     ```batch
     avi_env\Scripts\activate
     ```

4. **Upgrade `pip`** (Optional but recommended):

   ```bash
   pip install --upgrade pip
   ```

5. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   **Note**: Ensure that the `requirements.txt` file includes all necessary packages. For this bot, the main dependency is:

   - `tweepy`: Python library for accessing the Twitter API.

## Twitter API Setup

To interact with the Twitter API, you need to create a developer account and obtain API keys.

1. **Apply for a Twitter Developer Account**:

   - Visit [Twitter Developer Platform](https://developer.twitter.com/) and apply for a developer account.
   - Follow the instructions to get your account approved.

2. **Create a New App**:

   - Once approved, navigate to the [Developer Portal](https://developer.twitter.com/en/portal/dashboard).
   - Click on **"Create App"** and provide the necessary details.

3. **Generate API Keys and Tokens**:

   - After creating the app, navigate to the **"Keys and Tokens"** section.
   - Generate and copy the following credentials:

     - **API Key** (Consumer Key)
     - **API Secret Key** (Consumer Secret)
     - **Access Token**
     - **Access Token Secret**

   **Important**: Keep these credentials secure and do not share them publicly.

4. **Apply for Elevated Access** (If necessary):

   - Depending on your bot's functionality, you might need elevated access to use certain endpoints.
   - Ensure that your app permissions are set appropriately (read and write access).

## Configuration

Set up your configuration file to include your Twitter API credentials.

1. **Create a Configuration File**:

   - Navigate to the `src` directory:

     ```bash
     cd src
     ```

   - Create a new file named `config.py`:

     ```bash
     touch config.py
     ```

2. **Add Your API Credentials**:

   ```python:src/config.py
   # Twitter API credentials
   consumer_key = 'YOUR_CONSUMER_KEY'
   consumer_secret = 'YOUR_CONSUMER_SECRET'
   access_token = 'YOUR_ACCESS_TOKEN'
   access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
   ```

   **Note**: Replace `'YOUR_CONSUMER_KEY'` and other placeholders with your actual API keys and tokens.

3. **Secure Your Credentials**:

   - Add `config.py` to your `.gitignore` file to prevent it from being committed to version control.

     ```gitignore
     # src/.gitignore
     config.py
     ```

## Running the Bot

With everything set up, you can now run the bot.

1. **Initialize the Database**:

   - The bot uses a SQLite database to store replies.
   - The database is initialized automatically when you run the bot.

2. **Run the Bot**:

   - From the project's root directory:

     ```bash
     python src/main.py
     ```

   - The bot will start scanning for mentions and hashtags and reply accordingly.

3. **Monitor the Bot**:

   - The bot uses the `logging` module to output information.
   - Monitor the console output for any logs or error messages.

## Running Tests

Ensure your bot is functioning correctly by running unit tests.

1. **Install Testing Dependencies** (if not already in `requirements.txt`):

   ```bash
   pip install unittest
   ```

2. **Run the Tests**:

   - From the project's root directory:

     ```bash
     python -m unittest discover -s tests
     ```

     - Alternatively, if your tests are in `src`:

       ```bash
       python -m unittest discover -s src
       ```

   - The tests will run, and you'll see output indicating which tests passed or failed.

## Common Issues and Troubleshooting

### 1. Authentication Errors

**Problem**: Receiving authentication errors when attempting to access the Twitter API.

**Solution**:

- Verify that your API keys and tokens in `config.py` are correct.
- Ensure that your app has the necessary permissions (read and write access).
- Check that your system's clock is accurate, as time discrepancies can cause authentication failures.

**References**:

- [Twitter API Authentication](https://developer.twitter.com/en/docs/authentication/overview)

### 2. Rate Limit Exceeded

**Problem**: Hitting Twitter API rate limits, leading to `429 Too Many Requests` errors.

**Solution**:

- Utilize `wait_on_rate_limit=True` when initializing the Tweepy API to automatically handle rate limits.

  ```python
  api = tweepy.API(auth, wait_on_rate_limit=True)
  ```

- Implement backoff strategies if needed.
- Limit the number of requests or adjust the frequency of your bot's operations.

**References**:

- [Twitter API Rate Limits](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits)
- [Tweepy Rate Limit Handling](https://docs.tweepy.org/en/stable/faq.html#handling-the-rate-limit-using-cursors)

### 3. Duplicate Replies

**Problem**: The bot replies multiple times to the same tweet.

**Solution**:

- Ensure the `has_replied` function correctly checks the database for existing replies.
- Verify that the tweet IDs are stored and retrieved accurately.
- Check the database initialization and connection.

### 4. Errors When Running Tests

**Problem**: Tests fail or produce errors.

**Solution**:

- Make sure the database is correctly initialized during tests.
- Mock external dependencies like the Twitter API using `unittest.mock`.
- Ensure that the test environment is isolated and does not affect production data.

### 5. Module Not Found Errors

**Problem**: Python cannot find certain modules or packages.

**Solution**:

- Ensure all dependencies are installed in your virtual environment.
- Activate the virtual environment before running the bot or tests.
- Verify the `PYTHONPATH` and ensure it's set correctly.

### 6. Permission Issues on Windows

**Problem**: Scripts like `activate` or `pip` do not run correctly on Windows.

**Solution**:

- Use the correct command for activating virtual environments on Windows:

  ```batch
  avi_env\Scripts\activate
  ```

- Run your command prompt or PowerShell as an administrator if necessary.

## Potential Pitfalls

### 1. Exceeding Twitter Terms of Service

- **Issue**: Automated bots must comply with Twitter's policies.
- **Recommendation**:

  - Review Twitter's [Automation Rules](https://help.twitter.com/en/rules-and-policies/twitter-automation).
  - Avoid aggressive replying or spamming behaviors.
  - Ensure that your bot does not violate any terms that could lead to suspension.

### 2. Handling Exceptions

- **Issue**: Unhandled exceptions can crash the bot.
- **Recommendation**:

  - Implement comprehensive exception handling using `try-except` blocks.
  - Log exceptions for later analysis.
  - Consider using a monitoring service or setting up alerts.

### 3. Keeping API Keys Secure

- **Issue**: Exposing API keys can lead to security vulnerabilities.
- **Recommendation**:

  - Never commit `config.py` or any files containing sensitive information to version control.
  - Use environment variables or a configuration management tool for production environments.
  - Regularly rotate your API keys and tokens.

### 4. Rate Limit Handling

- **Issue**: Not properly handling rate limits can cause the bot to stop functioning.
- **Recommendation**:

  - Use Tweepy's built-in rate limit handler.
  - Monitor your app's rate limit usage in the Twitter Developer Portal.
  - Implement exponential backoff strategies when retrying requests.

### 5. Unicode and Encoding Errors

- **Issue**: Tweets with special characters may cause encoding errors.
- **Recommendation**:

  - Ensure your code handles Unicode characters properly.
  - Use `tweet_mode='extended'` to get the full text of tweets.

### 6. Database Locking

- **Issue**: Concurrent database access can lead to locking issues.
- **Recommendation**:

  - Use proper transaction management with SQLite.
  - Consider using a more robust database system for production environments.

## References

- **Twitter API Documentation**:

  - [Twitter Developer Platform](https://developer.twitter.com/)
  - [Twitter API v2 Reference](https://developer.twitter.com/en/docs/twitter-api)
  - [Authentication Guide](https://developer.twitter.com/en/docs/authentication/overview)

- **Tweepy Documentation**:

  - [Tweepy Documentation](https://docs.tweepy.org/en/stable/)
  - [Getting Started with Tweepy](https://docs.tweepy.org/en/stable/getting_started.html)
  - [Cursor Usage](https://docs.tweepy.org/en/stable/cursor_tutorial.html)

- **Python Resources**:

  - [Python's `unittest` Framework](https://docs.python.org/3/library/unittest.html)
  - [SQLite3 Module Documentation](https://docs.python.org/3/library/sqlite3.html)

- **Helpful Guides**:

  - [How to Set Up a Twitter Bot with Python](https://realpython.com/twitter-bot-python-tweepy/)
  - [Common Python Pitfalls](https://docs.python-guide.org/writing/gotchas/)
  - [Best Practices for Virtual Environments](https://docs.python.org/3/library/venv.html)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Disclaimer*: This bot is intended for educational purposes. Please ensure that you comply with all relevant laws, terms of service, and ethical guidelines when deploying automated systems on social media platforms.