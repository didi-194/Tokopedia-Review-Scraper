## Tokopedia Review Scrapper

This code is designed to scrape reviews for a specific product on Tokopedia (Indonesian e-commerce website) using Selenium and BeautifulSoup libraries. It extracts the reviewer name, review content, star rating, the number of helpful votes, and any problems mentioned in the review.

### Requirements

The following libraries are required to run the code:

1. Selenium
2. BeautifulSoup
3. Pandas

Selenium is used for web scraping, BeautifulSoup is used for parsing HTML code, and Pandas is used to store the extracted data in a CSV file.

The code is written in Python 3.7+ and has been tested on Mozilla Firefox browser.

### Installation

1. Install Python 3.7+ from [Python's official website](https://www.python.org/downloads/).
2. Install the required libraries by running the following command in the terminal or command prompt:
```
pip install selenium beautifulsoup4 pandas
```
3. Download the geckodriver executable file from [Mozilla's website](https://github.com/mozilla/geckodriver/releases) and extract the file to a location on your computer.
4. Add the path to the geckodriver executable file to your system's PATH variable. This will allow the code to access the geckodriver executable from anywhere on your computer.

### Usage

1. Open the code in your preferred Python editor and replace the product link on line 19 with the link of the product whose reviews you want to extract.
2. Uncomment line 10 if you want to run the code in headless mode. Headless mode is a mode where the browser is run in the background and not displayed on the screen.
3. Run the code.
4. The extracted data will be saved in a CSV file named "Tokped_review.csv" in the same directory as the code.

### Limitations

1. The code has been tested on a specific product's review page on Tokopedia. It may not work for all products on Tokopedia.
2. The code may not work if the HTML structure of the review page is changed in the future.
