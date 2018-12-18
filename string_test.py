# python 과거
#'일은 영어로 %s,  이는 영어로 %s' % ('one', 'two')

# pyformat
#'{} {}'.format('one', 'two')
'''
name = '파이리'
e_name = 'Lizard Baby'
print("안녕하세요. {}입니다. My name is {}".format(name, e_name))
print("안녕하세요. {1}입니다. My name is {0}".format(name, e_name))
print("안녕하세요. {1}입니다. My name is {1}".format(name, e_name))

# f-string python 3.6
name = '꼬부기'
e_name = 'Turtle Baby'
print(f'안녕하세요. {name}입니다. My name is {e_name}')
'''

import random

numbers = list(range(0,46))
lotto = random.sample(numbers, 7)
slotto = lotto[:6]
slotto.sort()
print("오늘의 행운 번호는 {}, {}, {}, {}, {}, {} 입니다.\n2등 보너스 번호는 {} 입니다.".format(slotto[0],slotto[1],slotto[2],slotto[3],slotto[4],slotto[5],lotto[6]))

name = "홍길동"
print("안녕하세요. " + name + "입니다.")



