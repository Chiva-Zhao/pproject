from new.crawler.XueqiuCrawler import XueqiuCrawler
from new.dispatch.XueqiuDispather import XueqiuDispather


def main_execute():
    craw = XueqiuCrawler()
    dispather = XueqiuDispather()
    craw.craw_base()
    dispather.select_white_list()
    craw.craw_every_day()
    dispather.select_best_list()
if __name__ == '__main__':
    main_execute()