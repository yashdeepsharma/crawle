# Example.md

This file demonstrates the usage of the web crawler in this repository.

## Demo Content

The web crawler is designed to help users gather data from multiple web pages efficiently. By using multi-threading, it can crawl multiple web pages simultaneously, significantly reducing the time required to gather data. The primary use cases for this web crawler include:

- Data collection for research purposes
- Monitoring changes on specific web pages
- Extracting links for further analysis
- Building datasets for machine learning projects
- Extracting business information from websites like Justdial

## Example Usage

To use the web crawler, run the `main.py` script and provide the seed URLs, maximum number of threads, and output file as input parameters:

```
python main.py --seed_urls <seed_urls> --max_threads <max_threads> --output_file <output_file>
```

Example:

```
python main.py --seed_urls https://example.com,https://example.org --max_threads 5 --output_file crawled_data.json
```

To extract business information from websites like Justdial, provide the business information parameters as input:

```
python main.py --seed_urls <seed_urls> --max_threads <max_threads> --output_file <output_file> --business_name <business_name> --business_address <business_address> --business_phone <business_phone>
```

Example:

```
python main.py --seed_urls https://justdial.com --max_threads 5 --output_file business_data.json --business_name "Business Name" --business_address "Business Address" --business_phone "Business Phone"
```

The crawled data will be saved into the specified JSON file.
