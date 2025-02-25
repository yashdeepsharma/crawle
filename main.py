from web_crawler import WebCrawler

def main():
    seed_urls = input("Enter seed URLs separated by commas: ").split(',')
    max_threads = int(input("Enter the maximum number of threads: "))
    
    crawler = WebCrawler(seed_urls, max_threads)
    crawler.run()

if __name__ == "__main__":
    main()
