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

5.  **Parsing HTML with Beautiful Soup**

    * Imported the `BeautifulSoup` library.
    * Parsed the fetched HTML content using `BeautifulSoup(html_content, 'html.parser')`.
    * Located the main feed container using `soup.find('shreddit-feed')`.
    * Used `feed.find_all('shreddit-post')` to retrieve a list of all individual post elements.
    * Iterated through the list of post elements.
    * For each post element, extracted the title using the `get('post-title')` method.
    * Extracted the relative link using the `get('permalink')` method and constructed the full URL.
    * Printed the title and link for each post found.
    * Added error handling for cases where the main feed or post elements are not found.

6.   **Integrating Reddit Scraping into Discord Bot**

    * Moved the Reddit scraping logic into the main `bot.py` file within an asynchronous function `get_reddit_posts()`.
    * Introduced the `discord.ext.tasks` to schedule periodic scraping.
    * Defined constants for the target Reddit URL, headers, and the Discord notification channel ID (with a reminder to replace the placeholder).
    * Created a `@tasks.loop()` that runs the `get_reddit_posts()` function at a set interval (currently 60 seconds).
    * Inside the loop, the bot retrieves the latest posts and sends them as Discord embeds to the specified channel.
    * Implemented a `before_loop` hook to ensure the task starts after the bot is ready.
    * Started the scraping task in the `on_ready()` event.
    * Basic error handling was added to the `get_reddit_posts()` function to catch request exceptions.
    * Noted the need for handling duplicate posts and potential rate limiting.

7.  **Preventing Duplicate Notifications**

    * Implemented a mechanism to prevent sending duplicate notifications using a JSON file (`sent_posts.json`) for storage.
    * Added asynchronous functions `load_sent_posts()` and `save_sent_posts()` to read and write the list of sent post links to the JSON file.
    * Modified the `scrape_reddit` task to:
    * Load the list of already sent post links at the beginning of each scrape.
    * Check if a newly scraped post's link exists in the loaded list.
    * If the link is new, send a Discord notification and add the link to the list.
    * After processing all scraped posts, save the updated list of sent links back to the JSON file.
    * Included basic error handling for the case where the JSON file doesn't exist or contains invalid JSON.

## Potential Improvements

With the basic Reddit scraping and duplicate prevention in place, the next steps could involve:
* **Adding support for more social media platforms.** This would require creating similar scraping logic for each platform.
* **Making the bot configurable.** Allowing users to specify which subreddits or social media accounts to follow through commands or a configuration file.
* **Improving the formatting of the Discord notifications** (e.g., including author, thumbnails, etc.).
* **Implementing more robust error handling and logging.**
* **Considering more efficient storage mechanisms** if the list of sent posts grows very large.