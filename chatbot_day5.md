flask flash messages





```
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```





## API 사용 연습

#### LOTTO 스크래핑

```python
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

```



#### LOTTO API 활용

- https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837

```python

import random
import requests
import json
from pprint import pprint

# 0. random 으로 로또번호를 생성

# 1. api 를 통해 당첨 번호를 가져온다.

# 2. 0번과 1번을 비교하여 나의 등수를 알려준다.

# 1. url 요청 보내서 정보를 가져옵니다. - json 으로 받는다. (딕셔너리로 접근 가능)

# 2. api 의 당첨번호와 보너스 번호를 저장하고.

# 3. 뽑은게 몇등인지 하는거 뽑으세요 끝.

# 당첨번호 조회
turn = 800
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(turn)
res = requests.get(url)
lotto = res.json()

nums = set()
for i in range(1, 7):
    drwtNo = "drwtNo" + str(i)
    nums.add(lotto[drwtNo])
bns = lotto["bnusNo"]
print(f"{turn}회차 당첨번호는 ")
for i in nums:
    print(str(i), end=' ')
print(f"+ {bns}")

#반복문 돌리기1
cnt = 0
hit = 0
while hit < 6:
    now = set(random.sample(range(1, 46), 6))
    hit = len((nums & now))
    if hit == 6:
        print("1등 당첨")
    elif hit == 5:
        if bns in now:
            print ("2등 당첨 " + str(cnt) + "만에 당첨")
        else: 
            print ("3등 당첨 " + str(cnt) + "만에 당첨")
    elif hit == 4:
        print("4등 당첨")
    elif hit == 3:
        print("5등 당첨")
    cnt += 1
print(f"{cnt} 만에 성공!")
```

---

## TELEGRAM

- 텔레그램 설치
- 봇 생성
- 키값 받기 : 777222444:AAEKtOPP60HfTRmKSfk8tuPuVVBfjekZXEo (가짜)

- https://api.telegram.org/bot777222444:AAEKtOPP60HfTRmKSfk8tuPuVVBfjekZXEo/getUpdates

- chat ID : 757457227



#### TELEGRAM 코드 

```python
import requests
import os
from pprint import pprint

token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
update = requests.get(url).json()
pprint(update)
chat_id = update["result"][0]["message"]["from"]["id"]
# print(chat_id)
# chat_id = 757457227
# chat_id = 737903255
msg = "GOGO"
method_name = "sendmessage"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"

print(msg_url)
print(requests.get(msg_url))
```



#### 환경변수 설정

`code ~/.bash_profile`

- .bash_profile

```
export TELEGRAM_BOT_TOKEN='777222444:AAEKtOPP60HfTRmKSfk8tuPuVVBfjekZXEo'
```

`source ~/.bash_profile`



#### KOSPI 추출

```python
import requests
from bs4 import BeautifulSoup
import os
from pprint import pprint

#chat_id 추출
token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
update = requests.get(url).json()
chat_id = update["result"][0]["message"]["from"]["id"]

#kospi 추출
req = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now")

#msg 전송
msg = f"현재 코스피 지수는 {kospi.text} 입니다."
method_name = "sendmessage"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"
print(msg_url)
print(requests.get(msg_url))
```



## 배포

#### 배포 준비

- 바탕화면에 telegram 폴더 생성 후 이동(다른 git repository와 겹치지 않도록)

- `echo "python-3.6.7" >> runtime.txt`

- `cat runtime.txt`

- `python -m pip install --upgrade pip`
- `pip freeze > requirements.txt`
- `git init`
- `git add .`

- `git status` : 새 파일이 3개가 나와야함
- `git commit -m "heroku setting"`



#### 헤로쿠 설치 및 실행

- https://devcenter.heroku.com/articles/heroku-cli
- vscode 종료 후 재실행
- `heroku login`
- 그냥 Enter 치면 사이트가 나오고 Log in 클릭하면 로그인 되고 터미널에 메일이 뜸
- `heroku create heuristic-telegram-bot` : create 이후에 프로젝트 네임은 겹치면 안됨

- `git push heroku master`

- done 되면 다시 heroku 페이지로 이동

- 프로젝트 클릭 -> settings -> Config Vars에 Key는  TELEGRAM_BOT_TOKEN

- Resource -> Add-ons -> Heroku Scheduler 추가

- Heroku Scheduler -> Add new job 클릭
- $`python telegram.py`
- FREQUENCY : Every 10 minutes 설정 후 Save

- 다시 프로젝트 페이지 -> More -> Run Console -> heroku run 에 python telegram.py

- 여기까지 실행하면 10 분 마다 자동으로 실행



#### 서버 중지

- 프로젝트 페이지 -> Overview -> Heroku Scheduler 클릭 -> Edit or Remove