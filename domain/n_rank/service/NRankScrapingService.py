from concurrent.futures import ThreadPoolExecutor
import random
import time
import requests
import json
from bs4 import BeautifulSoup


class NRankScripingService(object):
    def __init__(self, query):
        self.url = 'https://search.shopping.naver.com/search/all'
        self.frm = 'NVSCPRO'
        self.origQuery = query
        self.productSet = 'total'
        self.pagingSize = '80'
        self.query = query
        self.sort = 'rel'
        self.viewType = 'list'
        # self.pagingIndex = '1'

    def scrapingFirst(self, pagingStartIndex: int, pagingEndIndex: int):
        proxy = '13.124.217.238:3128'

        result = []

        for i in range(pagingStartIndex, pagingEndIndex+1):
            sleepTime = random.uniform(0.5, 2)
            # sleepTime = random.random(0.5, 2)
            params = {
                'frm': self.frm,
                'origQuery': self.origQuery,
                'pagingIndex': i,
                'pagingSize': self.pagingSize,
                'productSet': self.productSet,
                'query': self.query,
                'sort': self.sort,
                'viewType': self.viewType
            }

            try:
                res = requests.get(
                    url=self.url,
                    params=params,
                    proxies={'http': proxy, 'https': proxy},
                    timeout=10
                )
                if res.status_code == 200:
                    soup = BeautifulSoup(res.text, "html.parser")

                    stringData = soup.select_one('#__NEXT_DATA__').contents[0]

                    shoppingDataJsonObj = json.loads(stringData)
                    shoppingList = shoppingDataJsonObj['props']['pageProps']['initialState']['products']['list']

                    result.extend(shoppingList)
                else:
                    print('scrapingFirst failed status code not 200.')
                    raise Exception('failed')
            except:
                print('scrapingFirst failed exception')
                raise Exception('failed')

            time.sleep(sleepTime)

        return result

    def scrapingSecond(self, argData):
        proxy = argData['proxy']
        pagingStartIndex = argData['pagingStartIndex']
        pagingEndIndex = argData['pagingEndIndex']

        result = []

        for i in range(pagingStartIndex, pagingEndIndex+1):
            sleepTime = random.uniform(0.5, 2)
            params = {
                'frm': self.frm,
                'origQuery': self.origQuery,
                'pagingIndex': i,
                'pagingSize': self.pagingSize,
                'productSet': self.productSet,
                'query': self.query,
                'sort': self.sort,
                'viewType': self.viewType
            }

            try:
                res = requests.get(
                    url=self.url,
                    params=params,
                    proxies={'http': proxy, 'https': proxy},
                    timeout=10
                )
                if res.status_code == 200:
                    soup = BeautifulSoup(res.text, "html.parser")

                    stringData = soup.select_one('#__NEXT_DATA__').contents[0]

                    shoppingDataJsonObj = json.loads(stringData)
                    shoppingList = shoppingDataJsonObj['props']['pageProps']['initialState']['products']['list']

                    result.extend(shoppingList)
                else:
                    print('scrapingFirst failed status code not 200.')
                    raise Exception('failed')
            except:
                print('scrapingFirst failed exception')
                raise Exception('failed')

            time.sleep(sleepTime)

        return result

    def scrapingWithThread(self):
        allocated = [
            {
                'proxy':'13.124.217.238:3128',
                'pagingStartIndex':1,
                'pagingEndIndex':3
            },
            {
                'proxy':'13.124.217.238:3128',
                'pagingStartIndex':4,
                'pagingEndIndex':6
            },
            {
                'proxy':'13.124.217.238:3128',
                'pagingStartIndex':7,
                'pagingEndIndex':9
            }
        ]

        scheduler = []
        results = []
        with ThreadPoolExecutor() as executor:
            for i in executor.map(self.scrapingSecond, allocated):
                scheduler.append(i)

            for index, result in enumerate(scheduler):
                results.extend(result)

        return results
        # return None
