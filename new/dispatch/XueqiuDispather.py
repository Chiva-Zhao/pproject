from new.mysql.XueqiuDao import XueqiuDao
import pandas as pd


class XueqiuDispather:
    def __init__(self):
        self.dao = XueqiuDao
        pass

    def select_white_list(self):
        list_white = self.dao.query_author_white()
        list_black = self.dao.query_author_black()
        list_base = self.dao.query_base()
        if list(list_white) is None:
            df = pd.DataFrame(list_base)
            df['sum'] = 1 / 5 * df['priase'] + 2 / 5 * df['forword'] + 2 / 5 * df['comment']
            mean1 = df['sum'].groupby(df['author'], df['uid']).mean()
            # mean2= df.groupby('name').mean()
            mean3 = mean1.sort_index(by='sum')
            dflen = len(mean3)
            mean4 = mean3.iloc[dflen - 320:dflen, :]
            authors = list(mean4.index)
            uids = list(mean4['uid'])
            for author, uid in zip(authors, uids):
                self.dao.insert_author_white(uid, author)
        else:
            df = pd.DataFrame(list_base)
            df['sum'] = 1 / 5 * df['priase'] + 2 / 5 * df['forword'] + 2 / 5 * df['comment']
            mean1 = df['sum'].groupby(df['author'], df['uid']).mean()
            mean_evg = int(mean1.mean())
            mean3 = df.groupby('author').mean()
            mean4 = mean3[mean3['sum'] > 1.5 * mean_evg]
            mean5 = mean4['sum']
            xzname = list(mean5.index)
            setngname = set(list_black)
            setxzname = set(xzname)
            exrta_list = list(setngname & setxzname)
            mean6 = mean5.drop(exrta_list)
            mean7 = mean6.dropna()
            newxzname = list(mean7.index)
            setnewlist = set(newxzname)
            setlist3 = set(list_white)
            weknewlist = list(setnewlist & setlist3)
            mean7.drop(weknewlist)
            final_list = list(mean7.index)
            self.dao.insert_author_white()
            # TODO uid author

    def select_best_list(self):
        list_article = self.dao.query_day_articles()
        self.dao.insert_best_articles()

        df = pd.DataFrame(list_article)
        df['sum'] = 1 / 5 * df['priase'] + 2 / 5 * df['forword'] + 2 / 5 * df['comment']
        # mean2= df.groupby('name').mean()
        mean3 = df.sort_index(by='sum')
        dflen = len(mean3)
        mean4 = mean3.iloc[dflen - 50:dflen, :]
        urls = list(mean4['url'])
        authors = list(mean4['author'])
        titles = list(mean4['title'])
        for author, url, title in zip(authors, urls, titles):
            self.dao.insert_best_articles(title, author, url)
