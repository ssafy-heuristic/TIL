# 1
# 다음 리스트의 요소들을 한줄로 출력하시오(for 문 사용.)
# numbers = [2, 3, 6, 11, 8]
numbers = [2, 3, 6, 11, 8]
s = ""
'''
for i in numbers:
    print(i)
    s = s + str(i) + " "
print(s)
'''
for i in numbers:
    print(i, end=" ")
print()
# 2
# 주어진 리스트의 요소들 중에서 자연수가 홀수인지
# 짝수인지 판별하여 각각의 리스트로 출력하여라.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []

for i in numbers:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)