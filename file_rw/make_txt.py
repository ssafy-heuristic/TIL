# f = open("test1.txt", "w", encoding='utf-8')
# for i in range(5):
#     data = f'{i+1}번째 줄입니다. \t'
#     f.write(data)
# f.close()

# with open("test1.txt", "w", encoding='utf-8') as f:
#     for i in range(5):
#         data = f'{i+1}번째 줄입니다! \t'
#         f.write(data)

with open("new.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

