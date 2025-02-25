# crawle

## Web Crawler

This repository contains a web crawler implemented using Python multi-threading. The web crawler allows users to input seed URLs as parameters and crawls the web pages to extract links.

## Features

- Multi-threaded web crawling
- User input for seed URLs
- Fetches and parses web pages
- Extracts links from web pages
- Uses langchain for crawling
- Saves crawled data into a CSV file

## Installation

To install the dependencies, run the following command:

```
poetry install
```

## Usage

To use the web crawler, run the `main.py` script and provide the seed URLs and maximum number of threads as input parameters:

```
python main.py
```

Example:

```
Enter seed URLs separated by commas: https://example.com,https://example.org
Enter the maximum number of threads: 5
```

The crawled data will be saved into a CSV file named `crawled_data.csv`.
