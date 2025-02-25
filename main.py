import argparse
from web_crawler import WebCrawler
import config

def main():
    parser = argparse.ArgumentParser(description='Web Crawler')
    parser.add_argument('--seed_urls', type=str, help='Seed URLs separated by commas')
    parser.add_argument('--max_threads', type=int, help='Maximum number of threads')
    parser.add_argument('--output_file', type=str, help='Output file name')
    parser.add_argument('--business_name', type=str, help='Business name to extract')
    parser.add_argument('--business_address', type=str, help='Business address to extract')
    parser.add_argument('--business_phone', type=str, help='Business phone number to extract')
    args = parser.parse_args()

    seed_urls = args.seed_urls.split(',') if args.seed_urls else config.config['seed_urls']
    max_threads = args.max_threads if args.max_threads else config.config['max_threads']
    output_file = args.output_file if args.output_file else config.config['output_file']
    business_name = args.business_name if args.business_name else config.config['business_info']['name']
    business_address = args.business_address if args.business_address else config.config['business_info']['address']
    business_phone = args.business_phone if args.business_phone else config.config['business_info']['phone_number']
    
    crawler = WebCrawler(seed_urls, max_threads, output_file, business_name, business_address, business_phone)
    crawler.run()

if __name__ == "__main__":
    main()
