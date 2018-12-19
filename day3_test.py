# Q
'''
N = int(input("번호를 입력하세요: "))
for i in range(1,N+1):
    print(i)
'''

# Q
'''
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
'''  

# Q
'''
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
'''

# ssafy의 semester1의 기간을 출력하세요

# ssafy dictionary 안에 들어 있는 '대전'을 출력하세요

# daejeon의 매니저의 이름을 출력하세요.

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
