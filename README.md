# Scrape-and-clean-PB

## Project Description

This Python project is designed to scrape Powerball results from the web and perform a descriptive analysis on the obtained data. The scraper utilizes BeautifulSoup to fetch the HTML elements containing the dates and winning numbers. The project leverages two Python files to automate the data extraction and processing workflow. The extracted data is then cleaned and formatted for further analysis using Pandas and excel to create a basic relational database using MS Access.

## Project Structure

The project consists of two Python files:

scraper_and_cleaner_pb/
├── scraper.py
├── scraper_cleaner.py


## Installation

The project requires the following Python libraries:

* BeautifulSoup4
* Pandas

## Usage

1. Run `scraper.py` to scrape the Powerball results and generate an initial Excel file.
2. Run `scraper_cleaner.py` twice with the following arguments:
    1. First run: you need to pass "data" as an argument into pd.DataFrame() and rename the outputted excel file accordingly, to output powerball numbers (This creates an Excel file containing the cleaned Powerball numbers)
    2. Second run: you will need to pass "dates" as an argument into pd.DataFrame() to generate the dates of all the draws. 


## Contributions

We welcome contributions to improve this project. Feel free to fork the repository and submit pull requests with your enhancements.

## Future Improvements

1. Improve code maintainability and conciseness by further breaking down the code into subsets and create functions that only perform one objective. This applied to both python files.

2. Improve scraper_cleaner.py to allow the program to output both dates and powerball values side by side in an excel document. 

3. Implement error handling: The project currently lacks robust error handling mechanisms to deal with potential issues during scraping or cleaning. Using try-except mechanisms would be a great place to start


## Softwares and Libraries

* VS Code (v1.82.2)
* Python (v3.12.2)
* BeautifulSoup4 (v4.12.3)
* Pandas (v2.2.2)
* MS Excel 
* MS Access
