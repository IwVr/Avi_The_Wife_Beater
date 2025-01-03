# Avi_The_Wife_Beater Twitter Bot


## Description

This Twitter bot automatically replies to tweets mentioning Avi Yemini or using specific hashtags with information about his domestic violence charges.
Twitter Bot that responds to any of Avi Yemenis tweets or mentions that informs people of his Domestic Violence Charge


## Features

- Replies to mentions of @OzraeliAvi
- Replies to tweets with specific hashtags
- Stores replies in a SQLite database
- Ensures no duplicate replies
- Provides varied responses

## Setup

1. Clone the repository.
2. Create a virtual environment: `python -m venv avi_env`
3. Activate the virtual environment: `source avi_env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your Twitter API keys to `src/config.py`.
6. Run the bot: `python src/main.py`

## License

This project is licensed under the MIT License.