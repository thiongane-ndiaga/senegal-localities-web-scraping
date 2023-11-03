# senegal-localities-web-scraping
Simple web scraping application to collect all local authorities in Senegal

This app is developed in Python and uses Selenium as web scraping package

***web scraping***
*: technology that automates the retrieval of data from various web pages and transforms it into other, more usable formats (excel, csv, etc.).*

### How it works
The app open as a web page and navigate to [HCCT website](https://hcct.sn/territoires/collectivit%C3%A9s-territoriales). For each page it retrieves a departments list and local authorities for each department.
At the end you'll get an .json of results in `data/` folder.

### How to run
1. First you need to create a virtual environment and source it:

`python -m venv .venv && source .venv/bin/activate`

2. Install the requirements:

`pip install -r requirements.txt`

3. Run runner.py

`python app/runner.py`

4. See the result on the console or in `data/communes-XX.json`

# Cheers 🫡