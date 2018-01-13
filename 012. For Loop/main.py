# for문

# for문 기본구조
#
# for 변수 in 리스트(또는 튜플, 문자열):
#   수행할 문장1
#   수행할 문장2
#      ...
#

# 전형적인 for문 사용
lt = ['one', 'two', 'three']
for i in lt:
    print(i)

# 다양한 for문 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# range()
# range()는 숫자 리스트를 자동으로 만들어주는 함수다.
# 그걸 이용해 for문을 만들 수 있다.
# range(10) -> 0부터 10 미만의 숫자를 포함하는 range 객체를 만듬
# range(1, 11) -> range(시작 숫자, 끝 숫자)
# 1부터 11 미만의 숫자를 포함하는 range 객체를 만듬

# range() 사용 예시
for i in range(10):
    i += i
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        print("{0} * {1} = {2} ".format(i, j, i*j))
        print('')

# for문에 continue
lt = [90, 25, 67, 45, 80]
a = 0
for i in lt:
    a += 1
    if i < 60: continue  # 조건문이 참이면 처음 for문의 조건문으로 돌아간다.
    print("%d번 째 요소인 %d 이 60보다 크다." % (a, i))

# 리스트 안에 for문 포함하기

# 문법
# 변수 = [표현식 for 항목 in 반복가능객체 if 조건]  ->  "if 조건"은 생략 가능하다.
# r = [i * 3 for i in a]
# r = [num * 3 for num in a if num % 2 == 0]

a = [1, 2, 3, 4]
r = []
for i in a:
    r.append(i * 3)  # append()로 r 리스트에 i *3 요소를 삽입
print(r)

# 이 위에 코드를 쉽게 바꿀 수 있다.
r = []
r = [i * 3 for i in a]
print(r)

# 좀더 나아가서 if문도 넣을 수 있다.
r = []
r = [num * 3 for num in a if num % 2 == 0]
print(r)

# 좀더 나아가서 for문을 2개 이상 사용 가능하다.

# 문법
# [표현식 for 항목1 in 반복가능객체1 if 조건1
#        for 항목2 in 반복가능객체2 if 조건2
#        ...
#        for 항목n in 반복가능객체n if 조건n]
#
r = [x*y for x in range(2, 10)
     for y in range(1, 10)]
print(r)
# 구구단의 모든 결과를 리스트에 담는 코드다.
