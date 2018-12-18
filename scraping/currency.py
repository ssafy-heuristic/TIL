import requests
from bs4 import BeautifulSoup
#import bs4.BeautifulSoup
#from bs4 import BeautifulSoup as bus
# req = requests.get('https://finance.naver.com/sise/').text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# print(kospi.text)

# req = requests.get('https://www.naver.com').text
# soup = BeautifulSoup(req, 'html.parser')

# for i in soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a"):
#     rank = i.select_one(".ah_r").text
#     name = i.select_one(".ah_k").text
#     print(rank + " " + name)

# url = "https://www.naver.com/"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
#     rank = tag.select_one('.ah_r').text
#     name = tag.select_one('.ah_k').text
#     print(f'{rank}는 {name} 입니다.')

req = requests.get('https://m.stock.naver.com/').text
soup = BeautifulSoup(req, 'html.parser')
ranks = soup.select('.item')
print(ranks)