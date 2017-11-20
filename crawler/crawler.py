import logging
import urllib.request as urlreq
from urllib.parse import urlparse
import urltools
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
    
    
    def process_links(self, url):
        """Process links in an website, organize links as same domain or 3rd party
        
        Args:
            url
           
        Returns:
            list
        """

        links, images = self.parse_html(url=url)

        domain = []
        third_party = []
        # parse the input url for a base domain
        my_domain_parsed = urltools.parse(url)
        my_domain_string = my_domain_parsed.domain + "." + my_domain_parsed.tld

        for link in links:
            parsed = urltools.parse(str(link))
            domain_string = parsed.domain + "." + parsed.tld

            if domain_string == my_domain_string:
                # compare domains, assuming subdomain does not matter for 'uniqueness'
                urlstring = parsed.scheme + "://" + parsed.subdomain + "." + parsed.domain\
                            + "." + parsed.tld + parsed.path
                if not urlstring in domain:
                    domain.append(urlstring)
            elif parsed.domain == '':
                # handle relative path URL's, assume they below to base domain of input url
                path = parsed.path if parsed.path.startswith("/") else "/" + parsed.path
                urlstring = my_domain_parsed.scheme + "://" + my_domain_parsed.subdomain + "." + \
                            my_domain_parsed.domain + "." + my_domain_parsed.tld + path
                if not urlstring in domain:
                    domain.append(urlstring)
            else:
                # handle non-matching domains, assume all third-party
                subdomain = parsed.subdomain + "." if parsed.subdomain else ''
                urlstring = parsed.scheme + "://" + subdomain + parsed.domain \
                            + "." + parsed.tld + parsed.path
                if not urlstring in third_party:
                    third_party.append(urlstring)

        return domain, third_party
