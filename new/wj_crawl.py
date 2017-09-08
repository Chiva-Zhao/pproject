from new.crawler.XueqiuCrawler import XueqiuCrawler
from new.dispatch.XueqiuDispather import XueqiuDispather


def main_executeweeks():
    craw = XueqiuCrawler()
    craw.craw_base()
    dispather.select_white_list()
    craw.craw_every_day()
    dispather.select_best_list()


def main_executeday():
    dispather = XueqiuDispather()
    craw.craw_base()
    dispather.select_white_list()
    craw.craw_every_day()
    dispather.select_best_list()


def runTaskweek(func, day=0, hour=0, min=0, second=0):
    # Init time
    now = datetime.now()
    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
    print("now:", strnow)

    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period
    strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next run:", strnext_time)
    while True:
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(strnext_time):
            print("start work: %s" % iter_now_time)
            main_executeweek()
            print("task done.")
            iter_time = iter_now + period
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print("next_iter: %s" % strnext_time)
            # Continue next iteration
            continue


def runTaskday(func, day=0, hour=0, min=0, second=0):
    # Init time
    now = datetime.now()
    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
    print("now:", strnow)

    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period
    strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next run:", strnext_time)
    while True:
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(strnext_time):
            print("start work: %s" % iter_now_time)
            main_executeday()
            print("task done.")
            iter_time = iter_now + period
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print("next_iter: %s" % strnext_time)
            # Continue next iteration
            continue
if __name__ == '__main__':
    runTask(main_executeweek, day=5, hour=0, min=1)
    runTask(main_execute, day=1, hour=0, min=1)
