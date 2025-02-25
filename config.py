# Configuration settings for the web crawler

config = {
    'seed_urls': ['https://example.com', 'https://example.org'],
    'max_threads': 5,
    'output_file': 'crawled_data.csv',
    'business_info': {
        'name': '',
        'address': '',
        'phone_number': ''
    },
    'business_type': 'restaurant',
    'business_fields': ['name', 'address', 'phone_number']
}
