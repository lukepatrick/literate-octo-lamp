
import sys
import crawler


class web_index(object):

    def __init__(self):
        self.my_crawler = crawler.crawler.crawler()

def main(argv):
    if argv is None:
        argv = sys.argv
    crw = web_index()

    if argv[0]:
        crw.my_crawler.get_all_links(url=argv[0])
    else:
        print("nop")

if __name__ == "__main__":
    if sys.argv[1:]:
        main(sys.argv[1:])
    else:
        print("Full URL expected "
              "Example: \n $ python web_index.py http://www.google.com")

