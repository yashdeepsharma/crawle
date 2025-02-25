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

## Detailed Description

The web crawler is designed to help users gather data from multiple web pages efficiently. By using multi-threading, it can crawl multiple web pages simultaneously, significantly reducing the time required to gather data. The primary use cases for this web crawler include:

- Data collection for research purposes
- Monitoring changes on specific web pages
- Extracting links for further analysis
- Building datasets for machine learning projects

## Contributing

We welcome contributions to improve the web crawler. If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Submit a pull request with a detailed description of your changes

## Reporting Issues or Requesting Features

If you encounter any issues or have feature requests, please open an issue on the GitHub repository. Provide as much detail as possible to help us understand and address your concerns.

## Code Quality

To ensure code quality, we use `pylint` for static code analysis. You can run `pylint` to check the code quality by using the following command:

```
pylint <module_or_script_name>
```

For example, to check the code quality of `main.py`, run:

```
pylint main.py
```

Make sure to address any issues reported by `pylint` to maintain high code quality standards.
