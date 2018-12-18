# 챗봇 day2

#### 자료 게시

- github.com/djpy2

#### 테마 변경

- 왼쪽에서 가장 아래에 클릭해서  theme 검색하면 테마를 바꿀 수 있음

#### 파일 만들기

touch string_test.py

#### 코드 실행

code string_test.py 

- vscode에서 파일을 실행해줌
- sublime 은 subl, atom은 atom 으로 실행

#### 화면 비우기

- ctrl + L or clear 입력

## String 포맷 연습

####  기존에 사용하던 방식

```python
#python 과거
'일은 영어로 %s,  이는 영어로 %s' % ('one', 'two')

#pyformat
'{} {}'.format('one', 'two')
```

#### 예제

```python
name = '파이리'
e_name = 'Lizard Baby'
print("안녕하세요. {}입니다. My name is {}".format(name, e_name))
print("안녕하세요. {1}입니다. My name is {0}".format(name, e_name))
print("안녕하세요. {1}입니다. My name is {1}".format(name, e_name))
```

#### f-string 예시

- python 3.6 부터 사용 가능

```python
# f-string python 3.6
name = '꼬부기'
e_name = 'Turtle Baby'
print(f'안녕하세요. {name}입니다. My name is {e_name}')
```

#### 로또 실습

```python
import random

numbers = list(range(0,46))
lotto = random.sample(numbers, 7)
slotto = lotto[:6]
slotto.sort()
print("오늘의 행운 번호는 {}, {}, {}, {}, {}, {} 입니다.\n2등 보너스 번호는 {} 입니다.".format(slotto[0],slotto[1],slotto[2],slotto[3],slotto[4],slotto[5],lotto[6]))
```

#### 문자열 연산

```python
name = "홍길동"
print("안녕하세요. " + name + "입니다.")
```

## 파일명 바꾸기 실습

#### github에서 실습 코드 복사

- zzu.li/dummy 접속

- TIL 폴더 생성 및 이동
- zzu.li/dummy의 코드를 복사할 파일 생성 - 이름은 dummy_test.py

- 파일에 코드 복사 후 실행 <- touch로 500개의 파일을 생성하는 코드

- 파일 명을 바꾸기 위한 파일 생성 - 이름은 ch_name.py

#### 파일명 바꾸기

import os

1) os.chdir(r'폴더주소')

- 해당 폴더 주소로 이동, 윈도우만 r을 붙임

2) os.listdir('폴더주소')

- 지정된 디렉토리 전체 파일 목록 얻기

3)os.rename('현재 파일명', '바꿀 파일명')

```python
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG " + filename)
```

만약 SAMSUNG을 SAFFY로 대체 하고 싶다면

```python
# 파일명 바꾸기
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG", "SSAFY"))
```



## 파일 읽고 쓰기 

- TIL 안에 폴더 생성 - 폴더명은 file_rw
- 파일 생성하는 파이썬 파일 생성 - touch make_txt.py

#### 파일 쓰기

- 파일을 없으면 생성해서 열고 문자열 저장 후 닫기

```python
f = open("new.txt", "w")
f.write("Hello !!!")
f.close()
```

cf. with 구문

```python
with open("new.txt", "w") as f:
    f.write("Hello !!!")
```

- 다시 하면 w 옵션이기 때문에 내용이 덮어짐
- 추가하려면 a 옵션 사용

#### 파일 읽기

```python
f = open("new.txt", "r")
data = f.read()
print(data)
f.close()
```

- with 구문

```python
with open("new.txt", "r") as f:
    data = f.read()
    print(data)
```



#### 여러 줄 쓰기

```python
f = open("new.txt", "w", encoding='utf-8')
for i in range(5):
    data = f'{i+1}번째 줄입니다.\n'
    f.write(data)
f.close()
```

- with 구문

``` python
with open("new.txt", "w", encoding='utf-8') as f:
    for i in range(5):
        data = f'{i+1}번째 줄입니다!\n'
        f.write(data)
```

- writelines 함수

```python
menu = ["일본카레\n","인도카레\n","오뚜기카레\n"]
f = open("menu.txt", "w", encoding='utf-8')
f.writelines(menu)
f.close()
```

- writelines 함수 with 구문

```python
menu = ["일본카레\n","인도카레\n","오뚜기카레\n"]
with open("menu.txt", "w", encoding='utf-8') as f:
    f.writelines(menu)
```

#### 실습

- 여러 줄 출력을 tab으로 구분

```python
f = open("test1.txt", "w", encoding='utf-8')
for i in range(5):
    data = f'{i+1}번째 줄입니다. \t'
    f.write(data)
f.close()
```

- 여러 줄 출력을 tab으로 구분 - with 구문

```python
with open("test1.txt", "w", encoding='utf-8') as f:
    for i in range(5):
        data = f'{i+1}번째 줄입니다! \t'
        f.write(data)
```

#### 잠깐 복습 - 지금까지 내용 git 으로 push 하기 

- git status       : add 되지 않은 파일들을 확인할 수 있음
- git add .         : 현재 디렉토리의 내용을 모두 add, add하고 있는 디렉토리 위치 확인 할 것
- git commit -m "day2 commit_01"   : add 된 내용 commit

cf. 데스크탑도 git의 관리 장소로 설정된 경우 그곳으로 가서 

ls -al로 .git을 찾아서 삭제, 이후에 다중 git을 사용하게 되면 이 방법이 안될 수 있음

- git log		: git 로그를 확인할 수 있음

#### 파일 읽기 추가

`readline()` : 한 줄로 읽어서 리턴

`readlines()` : 파일 전체를 읽어 list 로 리턴

- 실습용 파일 생성

``` python
with open("new.txt", "w", encoding='utf-8') as f:
    for i in range(1, 11):
        data = f"{i}번째 줄입니다. \n"
        f.write(data)
```

- readline으로 한 줄 읽기

```python
with open("new.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    print(line)
```

-> 이렇게 하면 개행이 2번 됨

- strip으로 공백 문자열 양 옆 공백 처리

```python
ssafy = "          sdweqq       "
>>> ssafy.lstrip()
'sdweqq       '
>>> ssafy.rstrip()
'          sdweqq'
>>> ssafy.strip()
'sdweqq'
```

- readlines로 여러 줄 읽기

```python
with open("new.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

#### # 크롬 extension - 쉬어가기

- 유블록 오리진 : ad 블락을 더 가볍게 만듬
- 모멘텀 : 새 탭을 할 때 보이는 화면 변경

- Earth view from Google Earth
- Wappalyzer : 웹 구성 도구 확인 툴
- Octotree : github 파일 디렉토리 관리 도구
- Google Dictionary : 간단한 단어 사전

- Grammarly for Chrome : 문법 교정



## 정보 스크랩핑

#### request 연습

- `$ pip install requests` : request 모듈 설치

 1) request.get('url') : 해당 url에 get 요청 

```python
import requests

print(requests.get('https://www.naver.com'))
```

2) requests.get('url').text : 페이지 소스코드를 출력

```python
import requests

print(requests.get('https://www.naver.com').text)
```

3) requests.get('url').status_code : 상태 정보 얻기

```python
import requests

print(requests.get('https://www.naver.com').status_code)
```



#### 정보 스크랩 1단계

- beautifulsoup 준비
- `$ pip install bs4`: bs4 설치



1. 네이버 증권에서 정보 가져오기 - 코스피 지수

```python
import requests
from bs4 import BeautifulSoup
#import bs4.BeautifulSoup
#from bs4 import BeautifulSoup as bus
req = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now")
print(kospi.text)
```



2. 네이버 실시간 검색어 스크래핑

- 내 풀이

```python
import requests
from bs4 import BeautifulSoup
for i in soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a"):
    rank = i.select_one(".ah_r").text
    name = i.select_one(".ah_k").text
    print(rank + " " + name)
```

- 강사님 풀이

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name} 입니다.')
```

###  # github 이력서 호스팅 - 쉬어가기

- github에서 로그인
- username과 동일한 repository 생성
- 바탕화면에 resume 폴더 생성 후 shell 에서 resume로 이동
- `git init` : git 에서 관리 한다고 추가
- start bootstrap에서 resume 템플릿 다운 후 압축을 풀어서 웹 소스 코드를 resume에 저장
- `git commit -m "first commit"` : commit
- `git remote add origin https://github.com/ssafy-heuristic/ssafy-heuristic.github.io.git` : git repository에 연결
- `git push -u origin master` : 첫 push

- `ssafy-heuristic.github.io.git ` 로 접속하면 resume를 볼 수 있음 

