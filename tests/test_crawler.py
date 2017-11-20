import unittest

from .context import crawler


class CrawlerTestCase(unittest.TestCase):
    def setUp(self):
        self.myCrawler = crawler.crawler.crawler()

    def tearDown(self):
        self.myCrawler = None

    def test_valid_url(self):
        url = "http://www.google.com"

        response = None
        response = self.myCrawler.valid_url(url=url)
        self.assertIsNotNone(response)
        self.assertTrue(response)

    def test_valid_url_bad(self):
        url = "AAABBBBDDD"

        response = None
        response = self.myCrawler.valid_url(url=url)
        self.assertIsNotNone(response)
        self.assertFalse(response)

    def test_parse_html(self):
        url = "http://www.google.com"

        links = None
        images = None
        links, images = self.myCrawler.parse_html(url=url)
        self.assertIsNotNone(links)
        self.assertIsNotNone(images)
        self.assertGreater(len(links), 0)
        self.assertGreater(len(images), 0)

    def test_process_links(self):
        url = "http://buildit.wiprodigital.com/"

        domain = None
        third_party = None

        domain, third_party = self.myCrawler.process_links(url=url)
        self.assertIsNotNone(domain)
        self.assertGreater(len(domain), 0)







if __name__ == '__main__':
    unittest.main()


