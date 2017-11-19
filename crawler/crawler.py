import logging
import urllib.request as urlreq

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
            self.log.warning("URL {} not valid or no Internet Connection".format(url))
            return False


