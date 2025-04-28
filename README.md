# Social Media Discord Bot

This project aims to create a Discord bot that scrapes new posts from various social media platforms and sends real-time notifications to a designated Discord channel.

## Setup (as of [Current Date])

1.  **Discord Bot Setup:**
    * Created a new application on the Discord Developer Portal.
    * Created a bot user for the application.
    * Obtained the bot token (kept securely).
    * Invited the bot to the target Discord server.

2.  **Python Environment Setup:**
    * Installed Python (version [Your Python Version]).
    * Verified `pip` is installed (version [Your Pip Version]).
    * Created a project directory: `social_media_discord_bot`.
    * Created and activated a virtual environment named `venv`.
    * Installed the `discord.py` library.

3.  **Writing the Basic Discord Bot Structure and Connecting to Discord**

    * Created a main Python file named `bot.py`.
    * Implemented basic code to connect to the Discord API using the bot token.
    * Defined bot intents.
    * Implemented an `on_ready` event to print connection information to the console.
    * Added a simple `!ping` command for testing.
    * The bot can now be run using `python bot.py` and should appear online in the Discord server.

## Next Steps

The next step will involve researching and choosing the first social media platform we want to scrape and exploring the necessary web scraping libraries.