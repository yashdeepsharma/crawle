import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue
import json
from langchain import LangChain
import config

class WebCrawler:
    def __init__(self, seed_urls, max_threads=10, output_file='crawled_data.json', business_name='', business_address='', business_phone=''):
        self.seed_urls = seed_urls
        self.max_threads = max_threads
        self.output_file = output_file
        self.business_name = business_name
        self.business_address = business_address
        self.business_phone = business_phone
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
                business_info = self.extract_business_info(content)
                self.crawled_data.append({'url': url, 'content': content, **business_info})
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

    def extract_business_info(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        business_info = {
            'business_name': '',
            'business_address': '',
            'business_phone': ''
        }
        if self.business_name:
            business_info['business_name'] = soup.find(text=self.business_name)
        if self.business_address:
            business_info['business_address'] = soup.find(text=self.business_address)
        if self.business_phone:
            business_info['business_phone'] = soup.find(text=self.business_phone)
        return business_info

    def save_to_json(self):
        with open(self.output_file, 'w') as output_file:
            json.dump(self.crawled_data, output_file, indent=4)

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
        
        self.save_to_json()
