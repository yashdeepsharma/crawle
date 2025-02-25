# Crawle

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
python main.py --seed_urls <seed_urls> --max_threads <max_threads> --output_file <output_file>
```

Example:

```
python main.py --seed_urls https://example.com,https://example.org --max_threads 5 --output_file crawled_data.csv
```

The crawled data will be saved into the specified CSV file.

## Configuration

The web crawler uses a configuration file (`config.py`) to store default settings. You can modify the default settings in the `config.py` file or override them using command-line arguments.

### Default Configuration

The default configuration settings are as follows:

```python
config = {
    'seed_urls': ['https://example.com', 'https://example.org'],
    'max_threads': 5,
    'output_file': 'crawled_data.csv'
}
```

### Overriding Configuration

You can override the default configuration settings by providing command-line arguments when running the `main.py` script. The available command-line arguments are:

- `--seed_urls`: Seed URLs separated by commas
- `--max_threads`: Maximum number of threads
- `--output_file`: Output file name
