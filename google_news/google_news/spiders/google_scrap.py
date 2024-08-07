from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime, timedelta

class GoogleScrapSpider(CrawlSpider):
    # crawling
    name = 'google_scrap'
    allowed_domains = ['news.google.com']

    # Define the keywords to search for
    keywords = ['baja', 'steel', 'metalurgi']

    # Calculate the date and time one hour ago from now
    now = datetime.now()
    one_hour_ago = now - timedelta(hours=1)
    
    # Define the formatted date string
    formatted_date = one_hour_ago.strftime('%Y-%m-%dT%H:%M:%S')

    # Define the base URL for search
    base_url = 'https://news.google.com/search'

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # Create the start URLs using class-level variables
        cls.start_urls = cls.build_start_urls()
        return super(GoogleScrapSpider, cls).from_crawler(crawler, *args, **kwargs)

    @classmethod
    def build_start_urls(cls):
        """Build and return the start URLs."""
        return [f"{cls.base_url}?q={keyword}+after:{cls.formatted_date}" for keyword in cls.keywords]

    rules = (
        Rule(LinkExtractor(allow='search'), callback='parse_google_news', follow = True),
    )

    def parse_google_news(self, response):
        """Parse the Google News search results page."""
        scrape_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        for article in response.css('article'):
            yield {
                'title': article.css('h3 a::text').get(),
                'link': response.urljoin(article.css('h3 a::attr(href)').get()),
                'source': article.css('div > div > a::text').get(),
                'time': article.css('time::attr(datetime)').get(), 
                'scrape_time': scrape_time  # Add the timestamp here
            }
        
        # Follow next page links (if any)
        next_page = response.css('a[aria-label="Next page"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_google_news)
