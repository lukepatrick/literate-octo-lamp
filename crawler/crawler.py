import logging
import urllib.request as urlreq
from lxml import html
import requests

class crawler(object):
    
    def __init__(self, url=""):
        self.url = url
        self.log = logging.getLogger(__name__)

    def valid_url(self, url):
        """Validate the URL

        Args:
            url

        Returns:
            Boolean
        """
        if not url:
            return False


        try:
            request = urlreq.Request(url)
            response = urlreq.urlopen(request)
            # response valid
            return True
        except:
            # The url wasn't valid
            self.log.info("URL {} not valid or no Internet Connection".format(url))
            return False

    def parse_html(self, url):
        """Get URL and parse HTML to a usable tree

        Args:
            url

        Returns:
            tree object of HTML elements
        """
        if not self.valid_url(url):
            return None
        # Get Page
        page = requests.get(url)
        # Get HTML
        tree = html.fromstring(page.content)

        #XPath query for links
        links = tree.xpath('//a/@href')
        #Xpath query for static elements images
        images = tree.xpath('//img/@src')

        return links, images