import unittest

from .context import crawler


class CrawlerTestCase(unittest.TestCase):

    def setUp(self):

        self.myCrawler = crawler.crawler.crawler()

    def tearDown(self):

        self.myCrawler = None


    def test_something(self):
        self.assertEqual(True, False)

    def test_valid_url(self):
        url = "www.google.com"

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


if __name__ == '__main__':
    unittest.main()
