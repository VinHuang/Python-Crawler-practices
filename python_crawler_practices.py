import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

url = 'http://www.twse.com.tw/ch/trading/fund/BFI82U/BFI82U.php?download=&queryDWM=by_issueD&qdate={0}&query_yearW=2016&query_week=20161212&query_yearM=2016&query_monthM=12'

def getTradeValue(dt):
    res = requests.get(url.format(dt))
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text)
    for tr in soup.select('table tr')[2:]:
        td = tr.select('td')
        print td[0].text, td[1].text, td[2].text, td[3].text

today = date.today()
for i in range(1, 10):
    today = today + timedelta(days = -1)
    dayary = str(today).split('-')
    dt = '%2F'.join([str(int(dayary[0]) - 1911), dayary[1], dayary[2]])
    getTradeValue(dt)