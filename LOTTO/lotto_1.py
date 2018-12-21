from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800, 838), 8)

for i in numbers:
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
    # url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={i}"
    page = requests.get(url).text
    page = BeautifulSoup(page, "html.parser")
    nums = page.select('.ball_645')
    bonus = nums[6]
    nums = nums[:6]
    print(str(i) + " 회차 당첨번호")
    for i in nums:
        print(i.text, end=' ')
    print("+ " + bonus.text)
    print()
