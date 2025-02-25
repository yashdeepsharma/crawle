import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue
import csv
from langchain import LangChain

class WebCrawler:
    def __init__(self, seed_urls, max_threads=10):
        self.seed_urls = seed_urls
        self.max_threads = max_threads
        self.visited_urls = set()
        self.url_queue = Queue()
        self.crawled_data = []

    def crawl(self):
        while not self.url_queue.empty():
            url = self.url_queue.get()
            if url not in self.visited_urls:
                self.visited_urls.add(url)
                content = self.fetch_url(url)
                links = self.parse_links(content)
                self.crawled_data.append({'url': url, 'content': content})
                for link in links:
                    if link not in self.visited_urls:
                        self.url_queue.put(link)
            self.url_queue.task_done()

    def fetch_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return ""

    def parse_links(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            links.add(a_tag['href'])
        return links

    def save_to_csv(self, filename):
        keys = self.crawled_data[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.crawled_data)

    def run(self):
        for url in self.seed_urls:
            self.url_queue.put(url)
        
        threads = []
        for _ in range(self.max_threads):
            thread = threading.Thread(target=self.crawl)
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        self.save_to_csv('crawled_data.csv')
