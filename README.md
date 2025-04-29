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

4.  **Fetching Website Content (Completed 4/27/25)**

    * Created a Python script (initially for testing) to fetch the HTML content of a Reddit URL using the `requests` library.
    * Included a step to check the HTTP status code of the response to ensure the request was successful.
    * Retrieved the HTML content using `response.text`.
    * Added a basic User-Agent header to the request to mimic a web browser.
    * The script prints a success message and the first 500 characters of the HTML content to the console.

5.  **Parsing HTML with Beautiful Soup (Completed 4/28/25)**

    * Imported the `BeautifulSoup` library.
    * Parsed the fetched HTML content using `BeautifulSoup(html_content, 'html.parser')`.
    * Used CSS selectors (`soup.select()`) to target HTML elements containing post titles and links.
    * Iterated through the selected elements to extract the title text using `.get_text(strip=True)` and the link from the `href` attribute.
    * Noted that Reddit's HTML structure can be dynamic, and selectors might need adjustments.
    * Handled cases where links might be relative and prepended the base Reddit URL if necessary.
    * Added basic logic to try and pair titles with their corresponding links.
