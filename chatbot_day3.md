## 챗봇 3일차

#### 파이썬 익히기

- N 이 주어졌을 때 1부터 N까지 출력하기

```python
N = int(input("번호를 입력하세요: "))
for i in range(1,N+1):
    print(i)
```

- 투자 종목을 입력 받아서 투자 경고 종목에 있으면 "투자 경고 종목입니다" 없으면 "투자 경고 종목이 아닙니다" 를 출력

```python
warn_invenstment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f"경고 종목 리스트: {warn_invenstment_list}")
item = input('투자종목이 무엇입니까?: ')

if item.lower() in warn_invenstment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# 별도    
if item.lower() not in warn_invenstment_list:
    print("투자 경고 종목이 아닙니다")
else:
    print("투자 경고 종목입니다")
```

- colors에서 0, 4, 5 번째 항목만 제거한 새 리스트 만들기

```python
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
# Answer 1
new_colors1 = colors[1:4]
# Answer 2
new_colors2 = []
nolist = [0,4,5]
for i in range(len(colors)):
    if i not in nolist:
        new_colors2.append(colors[i])
print(new_colors1)
print(new_colors2)
```

- 주어진 딕셔너리에서 다음을 출력하라
  - ssafy의 semester1의 기간
  - ssafy dictionary 안에 들어 있는 '대전'
  - daejeon의 매니저의 이름

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}
print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])
```

## HTML 기초

- TIL 폴더에 web_basic 폴더 생성
- index.html 파일 생성 및 열기

----

- html 형식의 파일이라는 것을 정의

```html
<!DOCTYPE html>
```

- HTML : Hyper Text Markup Language
  - HTML은 태그를 이용해서 문서 내용을 구분
- html 태그

  - html 문서는 html 태그 안에서 작업이 이루어짐(cf. 단축기 html:5 입력 후 Enter)

```html
<!DOCTYPE html>
<html lang="en">
</html>
```

- head 태그
  - head 태그는 문서 전체에 대한 설정을 하는 부분

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
</head>
</html>
```

- body 태그
  - body 태그는 문서의 내용을 정의하는 부분

 ```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
</head>
<body>
	안녕하세요
</body>
</html>
 ```

- h1태그, p태그,  br태그
  - h1태그는 Markdown 에서 처럼 미리 정의된 폰트의 글자를 출력(h2, h3...)
  - p태그는 paragraph, 단락을 묶어주는 태그
  - br태그는 줄바꿈 태그
  - hr태그는 horizen, 수평선을 그어주는 태그

```html
	<h1>Hello HTML</h1>
    <p>안녕하세요</p>
    <p>안녕하세요</p>
	안녕하세요<br>안녕하세요
	<hr>
```

- img 태그
  - img 태그를 이용해서 웹 페이지에 이미지 파일을 불러올 수 있음
  - img 입력 후 Tab 키를 입력하면 `<img src="" alt="">`로 자동 완성
    - img 태그 안에 있는 src, alt 같은 것들은 img 태그의 '속성', 대입한 값은 '속성 값'
  - src에는 이미지의 경로를 입력, alt는 이미지 파일이 없을 때 표시할 문자열 입력

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
</head>
<body>
    <h1>Hello HTML</h1>
    <p>안녕하세요</p>
    <p>안녕하세요</p>
    <img src="https://post-phinf.pstatic.net/MjAxODAxMTVfMjQ4/MDAxNTE2MDA3Mjk1NTc0.trofpy35cywF7usTPQLpNa2TDwglm2QLXlB8YRCtcXkg.ntDPMI3ayEXTFisVKzX1_e1PWyi0TESajPzU1PfoEdcg.PNG/07_%EB%A9%94%EA%B0%80%EB%A6%AC%EC%9E%90%EB%AA%BD-%ED%94%BC%EC%B9%B4%EC%B8%84final2.png?type=w1200" alt="피카츄">
</body>
</html>
```

- 선택자 정의 - id 속성과 class 속성
  - p태그에 id는 uniq, class는 saffy와 daejeon 2개(공백은 여러 클래스를 정의할 때 구분자)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
</head>
<body>
    <h1>Hello HTML</h1>
    <p>안녕하세요</p>
    <p>안녕하세요</p>
    <p id="uniq" class="ssafy daejeon"></p>
</body>
</html>


```

- 주석 처리

```html
<body>
    <h1>Hello HTML</h1>
    <p>안녕하세요</p>
    <p>안녕하세요</p>
    <!-- 이미지 태그 -->
    <img src="https://post-phinf.pstatic.net/MjAxODAxMTVfMjQ4/MDAxNTE2MDA3Mjk1NTc0.trofpy35cywF7usTPQLpNa2TDwglm2QLXlB8YRCtcXkg.ntDPMI3ayEXTFisVKzX1_e1PWyi0TESajPzU1PfoEdcg.PNG/07_%EB%A9%94%EA%B0%80%EB%A6%AC%EC%9E%90%EB%AA%BD-%ED%94%BC%EC%B9%B4%EC%B8%84final2.png?type=w1200" alt="피카츄">
    <p id="uniq" class="ssafy daejeon"></p>
</body>
```

---

## CSS 기초

- css : Cascading Style Sheets, html 문서를 디자인 하기 위한 문법

#### 3가지 사용방법

- Inline Style

- Internal Style( = embedding 방법)
- Linking Style

- cf. http://www.colors.commutercreative.com/grid/ 문자열로 색을 선택할 때 참고할 수 있는 사이트

---

#####  css 주석

```css
    <style>
        /* h1 { color: red;} */
    </style>
```

#####  embeded 방법

```css
<head>
    <meta charset="UTF-8">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
    <!-- 1. embedding style-->
    <style>
        /* h1 { color: red;} */
    </style>
</head>
```

##### inline 방법

```css
<body>
    <h1>Hello HTML</h1>
    <!-- 2. inline styling -->
    <p style="color: violet">안녕하세요</p>
    <p>안녕하세요</p>
</body>
```

##### linking 방법

- 새로 css 파일 생성 - style.css

```css
p {
    background-color: red
}
/* class 적용 */
p.third {
    background-color: aquamarine
}
/* id 적용 */
p#good{
    background-color: yellow
}
```

- 적용할 html 파일 head에 css 적용 

```html
<head>
    <meta charset="UTF-8">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
    <!-- 3. linking style-->	
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello HTML</h1>
    <!-- 2. inline styling -->
    <p style="color: violet">안녕하세요</p>
    <p class="third">안녕하세요</p>
    <p id="good">Good</p>
</body>
```

##### Selector 자세히

- 선택자 우선순위 : id > 태그 > class

---

- style.css

```css
/* universial Selector */
* {
    color: blue;
}

body{
    background: white;
}

#lunch {
    color: red;
}

#dinner{
    font-weight: bold;
}

.container{
    font-size: 20px;
}

.text-center{
    text-align: center;
}

.text-red{
    color: red;
}

.text-blue{
    color: blue;
}

.text-large {
    font-size: 200%;
}

div p {
    color: green;
}

div > p {
    color: hotpink;
}

/* p + span {
    background-color: blueviolet;
} */

p ~ span {
    background-color: brown;
}

```

- index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Heuristic's Story</title>
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello HTML</h1>
    <!-- 2. inline styling -->
    <p style="color: violet">안녕하세요</p>
    <div class="container">
        <p class="third">안녕하세요</p>
        <p id="lunch">점심 돈까스</p>
        <span>paragraph1</span>
        <span>
            paragraph2
            <p>paragraph3</p>
        </span>
    </div>
    <p id="dinner">저녁 뭐먹지??</p>
    <hr>
    <p class="text-center">Center</p>
    <p class="text-large text-red">Large Red</p>
    <p class="text-center text-large text-blue">Center Large Blue</p>
</body>
</html>


```

- 참고용 사이트
  - https://www.w3schools.com/

---



## Flask

- http://flask.pocoo.org/
- micro framework : 가볍고 기능이 적음

---

- gmail에서 받은 메일 확인 -> support@c9.io

- link 클릭, username 설정
- 이것저것 설정하고 만들기, gmail은 github과 동일한 것이 좋음

- Join Team

- 다시 gmail에 온 메일 확인 -> 비밀번호 설정
- create workspace -> flask-basic, public, blank

- c9 접근 주소는 [c9.io/login](c9.io/login)



#### 파이썬 환경 설정

- `sudo apt-get update`: 우분투 전체 업데이트

- pyenv 검색, https://github.com/pyenv/pyenv : 파이썬 버전 관리 프로그램
- 메뉴얼 대로 c9에 설치
  - 1,2,3,4 실행
  - 우분투는 `~/.bash_profile` 대신 `~/.bashrc`

- `pyenv install 3.6.7`: 파이썬 공식 홈페이지를 통해 설치
- `pyenv global 3.6.7` : 버전을 3.6.7로 변경
- `pyenv rehash` : 버전 적용
- `python -V` : python 버전 확인

- `pip install -U pip` : pip 업데이트
- `pip -V` : pip 버전 확인



#### flask 설치

- `pip install flask`  : flask 설치

- `mkdir flask-start`  : 테스트 용 폴더 생성 및 이동
- `touch hello.py`  : 파일 생성
- flask 홈페이지에서 Flask is Fun 소스 코드를 복사 후 저장

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

- `export FLASK_APP=hello.py` : 시작할 때 적용할 앱을 설정 (딱 한번만 설정)
- `flask run --host=0.0.0.0 --port=8080` : flask로 서버 실행
- 내용 변경 후 적용하기 위해서는 서버를 재실행 -> ctrl+c로 종료 후 다시 실행 명령어 입력



- 공식 홈페이지에서 read the documentation -> Quick Start -> Routing

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "index"
    
@app.route("/hello")
def hello():
    return "hello"
```

- 로컬이 아니라서 다른 사람의 주소로도 접속이 가능



- html 출력

``` python
from flask import Flask
app = Flask(__name__)

@app.route("/html_tag")
def html_tag():
    return "<h1>html_tag</h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1> multi lines </h1>
    <ul>
        <li> one </li>
        <li> two </li>
        <li> three </li>
    </ul>
    """

```



- render template

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/html_render")
def html_render():
    return render_template("index.html")
```

-> render_template의 기본 경로는 같은 위치의 templates 폴더를 찾아서 파일을 검색 후 실행



- variable routing

  - templates에 hello.html 파일 생성

  ```python
  <h1>Hello!, {{ your_name }} </h1>
  ```

  - hello.py 수정 -> parameter를 받아서 넘김

  ```python
  from flask import Flask, render_template
  app = Flask(__name__)
  
  @app.route("/html_name/<string:name>")
  def html_name(name):
      return render_template("hello.html", your_name = name)
  ```

- 응용 : 받은 값의 세제곱 출력하기

  - math.html

  ```python
  <h1>{{ num }} 의 세제곱은  </h1>
  <h2>{{ result }} 입니다. </h2>
  ```

  - hello.py

  ```python
  from flask import Flask, render_template
  
  @app.route("/math/<int:num>")
  def math(num):
      result = num**3
      return render_template("math.html", num = num, result = result)
  ```

- 응용 : 식사 메뉴 뽑기
  - dinner.html

  ```html
  <h1> 오늘의 저녁 메뉴는 {{ pick }} 이다! </h1>
  <img src="{{ url }}" alt="{{ pick }}" height="300" width="400"></img>
  ```

  - hello.py

  ```python
  from flask import Flask, render_template
  import random
  
  @app.route("/dinner")
  def dinner():
      list = ["초밥", "탕수육", "삼겹살", "돼지국밥"]
      dict = {
          "초밥" : "http://image.edaily.co.kr/images/Photo/files/NP/S/2014/09/PS14090300271.jpg",
          "탕수육" : "https://t1.daumcdn.net/cfile/tistory/257B403B534201F811",
          "삼겹살" : "https://i.ytimg.com/vi/ulVYYoXX6c8/hqdefault.jpg",
          "돼지국밥" : "http://cityfood.co.kr/file2/h_0111/55454/photo/235952ad.jpg"
      }
      pick = random.choice(list)
      url = dict[pick]
      return render_template("dinner.html", pick=pick, url=url)
  ```

  ---



## Font Awesome 활용하기

- https://ssafy-heuristic.github.io/ : resume page에 접속해서 skills 확인
- skills에 있는 아이콘 목록은 `fab fa-`로 시작하는 class를 갖는다
- https://fontawesome.com/ 에서 원하는 아이콘을 찾아서 fa-이후를 변경하면 원하는 아이콘으로 변경 가능
- resume 폴더에 index.html에서 원하는 icon이 나오도록 수정



#### 수정 후 commit

- resume 폴더로 이동
- `git add .`
- `git status`
- `git commit -m "font-awesome test"`

- `git push`



#### font awesome 사이즈 변경

- resume.min.css 에서 일괄적으로 아이콘 크기 변경

```css
li > i.fab{
  font-size: 80px;
}
```

