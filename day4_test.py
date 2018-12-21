# #Q1
# score = {
#     "국어":87,
#     "영어":92,
#     "수학":40
# }
# sum_value = 0
# for i in score:
#     sum_value += score[i]
# avg = sum_value/len(score)
# print(avg)
# print(sum(score.values()) / len(score))

# #Q2
# scores = {
#     "철수": {
#         "국어": 80,
#         "영어": 90,
#         "수학": 100
#     }, 
#     "영희": {
#         "국어": 70,
#         "영어": 60,
#         "수학": 50
#     }   
# }

# each_total = 0
# for name in score:
#     each_total += sum(score[name].values()) / len(scores[name])
# print(each_total / len(scores))

# Q3
# score = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# # 도시 중 최근 3일 가장 추웠던 곳과 가장 더웠던 곳
# for key, value in score.items():
#     print(key, value)

cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 9],
    "부산": [2, -2, 9]
}

max_city = ""
min_city = ""
max_num = -float("inf")
min_num = float("inf")
for name, temp in cities.items():
    if max(temp) > max_num:
        max_num = max(temp)
        max_city = name
    if  min_num > min(temp):
        min_num = min(temp)
        min_city = name
print("최고로 더웠던 도시 " + max_city + ", 추웠던 도시 " + min_city)