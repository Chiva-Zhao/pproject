import ICrawler
from new.mysql.XueqiuDao import XueqiuDao
import re


class XueqiuCrawler(ICrawler):
    def __init__(self):
        self.dao = XueqiuDao()

    def craw_base(self):
        list1 = ['https://xueqiu.com/today#/cn', 'https://xueqiu.com/today#/hk',
                 'https://xueqiu.com/today#/financial_management'
            , 'https://xueqiu.com/today#/us']
        for wsss in list1:
            self.brower.get(wsss)
            for i in range(3):
                self.brower.execute_script("window.scrollBy(0," + str(i * 1000 + 2000) + ")")
                self.time.sleep(3)
                if i == 2:
                    data = self.brower.page_source
                    soup = self.BeautifulSoup(data, "html.parser")
                    list1 = soup.find_all('div', class_='home__timeline__item')
                    for list2 in list1:
                        title = list2.find('h3').get_text()
                        uid = list2.find('a', class_='user-name')['href']
                        url = list2.find('a').attrs['href']
                        author = list2.find('a', class_='user-name').get_text()
                        wirte_time = list2.find('span', class_='timestamp').get_text()
                        read = list2.find('div', class_='read').get_text()
                        category = list2.find('span', class_='category').get_text()
                        self.brower.get('https://xueqiu.com/2701143866/90963519' + url)
                        data = self.brower.page_source
                        soup = self.BeautifulSoup(data, "html.parser")
                        priasexml = soup.find_all('div', class_="meta-btns single-meta-btn")
                        today = self.date.today()
                        for num in priasexml:
                            rows = num.find_all("em", class_='em_number')
                            try:
                                priase = rows[0].get_text()
                                forword = rows[1].get_text()
                                comment = rows[2].get_text()
                            except:
                                priase = ''
                                forword = ''
                                comment = ''
                            if priase == '' or forword == '' or comment == '':
                                continue
                            # print(a1)
                            print(uid, author, title, wirte_time, read, category, url, priase, forword, comment)
                            self.dao.insert_base(uid, author, title, wirte_time, read, category, url, priase,
                                                 forword, comment)
        self.time.sleep(3)
        self.brower.close()

    def craw_every_day(self):

        white_list = self.dao.query_author_white()
        black_list = self.dao.query_author_black()
        final_list = white_list & black_list
        # TODO 去除负面清单

        wzss = 'https://xueqiu.com'
        for user in final_list:
            self.brower.get(wzss + user.uid)
            data = self.brower.page_source
            soup = self.BeautifulSoup(data, "lxml")
            list1 = soup.find_all('div', class_='status_bd')
            today = self.date.today()
            url = ''
            title = ''
            write_time = ''
            priase = ''
            forword = ''
            comment = ''
            try:
                list2 = list1[0].find_all('li')
            except:
                list2 = ''
            if list2 == '':
                continue
            # list1 = soup.find_all('ul',class_='status-List')
            for list3 in list2:
                try:
                    wzs = list3.find('h4')
                    url = wzs.find('a').attrs['href']
                    # print(wz)
                    title = wzs.get_text()
                    print(title)
                    write_time = list3.find('a', class_='time').get_text()
                    priase = list3.find('a', class_='like').get_text()
                    forword = list3.find('a', class_='repost second').get_text()
                    comment = list3.find('a', class_='statusComment last').get_text()
                except:
                    url = ''
                    title = ''
                    write_time = ''
                    priase = ''
                    forword = ''
                    comment = ''
                if title == '' or write_time == '' or priase == '' or forword == '' or comment == '' or url == '':
                    continue
                # print(times,title,wz)
                # zan = list3.find('a',class_='like').get_text()
                if write_time[-1] == '前':
                    times = today
                elif write_time[0] == '今':
                    times = today
                else:
                    times = write_time
                if len(priase) == 1:
                    priase = 0
                elif len(priase) != 1:
                    d = int(re.sub("\D", "", priase))
                    priase = d
                else:
                    print('wu')
                if len(forword) == 2:
                    forword = 0
                elif len(forword) != 2:
                    b = int(re.sub("\D", "", forword))
                    forword = b
                else:
                    print('wu')
                # zhuanfas = int(re.sub("\D", "", zhuanfa))
                # pinglun = list3.find('a',class_='statusComment last').get_text()
                if len(comment) == 2:
                    comment = 0
                elif len(comment) != 2:
                    c = int(re.sub("\D", "", comment))
                    comment = c
                else:
                    print('wu')
                print(times, title, url)
                self.dao.insert_day_articles(title, user.author, write_time, url, priase, forword, comment)
