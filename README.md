# Simple Web Scraper in Python

##Project Overview

This is a basic web scraping script built in Python. It extracts and prints all the links (`<a href="...">`) from a given webpage. This project is part of my learning journey in Python, HTML, and web servers.

##Objective (Requirements)

- Input: A single URL (the page to be scraped).
- Output: All hyperlink URLs (`href` values) found on that page.
- Use standard libraries like `requests` and `BeautifulSoup`.

##Features

- Connects to the target webpage.
- Parses the HTML content using BeautifulSoup.
- Identifies and prints all anchor (`<a>`) tag links.

##Design & Structure

- `fetch_html(url)`: Fetches raw HTML content from the URL.
- `extract_links(html)`: Extracts and returns a list of links from the HTML content.
- `main()`: Entry point that takes the URL input and calls the above functions.

This modular design will make it easier to add new features like:
- Scraping multiple pages.
- Saving data to CSV or JSON.
- Filtering internal/external links.

##Technologies Used

- Python 3.x
- `requests`
- `BeautifulSoup` from `bs4`

##How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
