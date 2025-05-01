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

5.  **Parsing HTML with Beautiful Soup (Completed 4/30/25)**

    * Imported the `BeautifulSoup` library.
    * Parsed the fetched HTML content using `BeautifulSoup(html_content, 'html.parser')`.
    * Located the main feed container using `soup.find('shreddit-feed')`.
    * Used `feed.find_all('shreddit-post')` to retrieve a list of all individual post elements.
    * Iterated through the list of post elements.
    * For each post element, extracted the title using the `get('post-title')` method.
    * Extracted the relative link using the `get('permalink')` method and constructed the full URL.
    * Printed the title and link for each post found.
    * Added error handling for cases where the main feed or post elements are not found.

6.   **Integrating Reddit Scraping into Discord Bot (Completed 4/30/25)**

    * Moved the Reddit scraping logic into the main `bot.py` file within an asynchronous function `get_reddit_posts()`.
    * Introduced the `discord.ext.tasks` to schedule periodic scraping.
    * Defined constants for the target Reddit URL, headers, and the Discord notification channel ID (with a reminder to replace the placeholder).
    * Created a `@tasks.loop()` that runs the `get_reddit_posts()` function at a set interval (currently 60 seconds).
    * Inside the loop, the bot retrieves the latest posts and sends them as Discord embeds to the specified channel.
    * Implemented a `before_loop` hook to ensure the task starts after the bot is ready.
    * Started the scraping task in the `on_ready()` event.
    * Basic error handling was added to the `get_reddit_posts()` function to catch request exceptions.
    * Noted the need for handling duplicate posts and potential rate limiting.
