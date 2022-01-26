import math

def getAdRank(query, mallName, itemList):
    adRank = 0
    commonRank = 0

    adList = []
    commonList = []

    for i in range(0, len(itemList)):
        item = itemList[i]['item']

        if 'adId' in item:
            adRank += 1
            if item['mallName'] == mallName :
                currPage = math.ceil((commonRank+1)/40)
                itemDict = {
                    'rank':adRank,
                    'type':'광고',
                    'productTitle':item['productTitle'],
                    'mallName':item['mallName'],
                    'pageIndex':currPage,
                    'imageUrl':item['imageUrl'],
                    'details':item,
                    'query': query
                }

                adList.append(itemDict)
            continue

        commonRank += 1

        if item['lowMallList'] :
            lowMallList = item['lowMallList']

            for j in range(0, len(lowMallList)):
                if(lowMallList[j]['name'] == mallName):
                    itemDict = {
                        'rank':commonRank,
                        'type':'가격비교',
                        'productTitle':item['productTitle'],
                        'mallName':mallName,
                        'pageIndex':math.ceil(commonRank/40),
                        'pageRank':commonRank % 40,
                        'imageUrl':item['imageUrl'],
                        'details':item,
                        'query': query
                    }

                    commonList.append(itemDict)
            continue

        if item['mallName'] == mallName :
            itemDict = {
                'rank':commonRank,
                'type':'일반',
                'productTitle':item['productTitle'],
                'mallName':mallName,
                'pageIndex':math.ceil(commonRank/40),
                'pageRank':commonRank % 40,
                'imageUrl':item['imageUrl'],
                'details':item,
                'query': query
            }

            commonList.append(itemDict)

    result = {
        'adList':adList,
        'commonList':commonList,
        'totalAdCount':adRank,
        'totalCommonCount':commonRank
    }

    return result
            



