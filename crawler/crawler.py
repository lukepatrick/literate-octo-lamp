import logging


class crawler(object):
    
    def __init__(self, url):
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

        



