import argparse
from web_crawler import WebCrawler
import config

def main():
    parser = argparse.ArgumentParser(description='Web Crawler')
    parser.add_argument('--seed_urls', type=str, help='Seed URLs separated by commas')
    parser.add_argument('--max_threads', type=int, help='Maximum number of threads')
    parser.add_argument('--output_file', type=str, help='Output file name')
    args = parser.parse_args()

    seed_urls = args.seed_urls.split(',') if args.seed_urls else config.config['seed_urls']
    max_threads = args.max_threads if args.max_threads else config.config['max_threads']
    output_file = args.output_file if args.output_file else config.config['output_file']
    
    crawler = WebCrawler(seed_urls, max_threads, output_file)
    crawler.run()

if __name__ == "__main__":
    main()
