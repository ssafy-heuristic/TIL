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
turn = 625
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

# #반복문 돌리기2
# cnt = 0
# hit = 0
# while True:
#     now = set(random.sample(range(1, 46), 6))
#     hit = len((nums & now))

#     if hit == 6:
#         print("1등 당첨")
#     elif hit == 5:
#         if bns in now:
#             print ("2등 당첨")
#         else: 
#             print ("3등 당첨")
#     elif hit == 4:
#         print("4등 당첨")
#     elif hit == 3:
#         print("5등 당첨")
#     if hit > 
#     cnt += 1
# print(f"{cnt} 만에 성공!")

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
            print ("2등 당첨 " + format(cnt*1000,',') + "원으로 성공")
    #     else: 
    #         print ("3등 당첨 " + str(cnt) + "만에 당첨")
    # elif hit == 4:
    #     print("4등 당첨")
    # elif hit == 3:
    #     print("5등 당첨")
    cnt += 1
print(f"{format(cnt*1000,',')} 원으로 성공!")

# # 강사님 답

# while True:
#     my_numbers = sorted(random.sample(range(1,46), 6))
#     matched = len(num & set(my_numbers))

#     if matched == 6:
#         print("1등")
#     elif matched == 5:
#         if bns in my_numbers:
#             print("2등")
#         else:
#             print("3등")
#     elif matched == 4:
#         print("4등")
#     elif matched == 3:
#         print("5등")
#     else:
#         print("꽝")










