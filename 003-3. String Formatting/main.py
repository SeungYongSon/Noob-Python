# 포매팅 Formatting

# 문자열 포매팅

# 숫자 바로 대입
print('I have %d pen' % 3)

# 문자열 바로 대입
print('I Like %s' % "train")

# 값을 나타내는 변수로 대입
a = 123
print("%d" %a)

# 2개 이상 값들 대입
a = 789
print('Counting. %d %s %d' %(123, '456', a))

# 포맷 코드
# %s  문자열
# %c : 문자 1개
# %d : 정수
# %f : 실수
# %o : 8진수
# %x : 16진수
# %% : 문자 '%' 자체

# %d 와 %을 같이 쓸때는 %%을 쓴다.
print("%d%%" % 9999)

# 정렬 과 공백
print("%10s" % "hi")  # %10s 10번 공백하고 문자열 hi 대입
print('%-10sjane' % 'hi')  # %-10s 왼쪽 정렬후 문자열 hi 대입

# 소수점 표현
print('%0.4f' % 3.1415926535897932384626)  # 소수점 4자리까지만 표시

# 고급? 문자열 포패팅?

# {0} .format() 이용
# 바로 값 대입
print("I have {0} pen".format(3))
print("I have a {0}".format("apple"))

# 값 있는 변수 대입
a = "apple"
print("I have a {0}".format(a))

# 2개 이상의 값 넣기
number = 3
apple = 'apples'

#  {0}, {1}과 같은 인덱스 항목들이 format 함수의 입력값들로 순서에 맞게 바뀐다.
print("I have {0} {1}".format(number, apple))
# {0}은 format 함수의 첫 번째 입력값인 number로 바뀌고
# {1}은 format 함수의 두 번째 입력값인 apple로 바뀐다.


# 이름과 .format() 이용
print("I slept {hour} hours. so I was sick for {day} days.".format(hour=72, day=3))

# 정렬(기호가 귀엽다)
print("{0:<10}".format('hi'))  # 왼쪽 정렬  :<
print("{0:>10}".format('hi'))  # 오른쪽 정렬 :>
print("{0:^10}".format('hi'))  # 가운데 정렬 :^

# 공백 채우기
print("{0:!>10}".format('hi'))  # 왼쪽 공백  :!>
print("{0:!<10}".format("hi"))  # 오른쪽 공백  :!<
print("{0:=^10}".format("hi"))  # 양쪽 공백  =^

# 소수점 표현
y = 3.1415926535897932384626
print("{0:0.4f}".format(y)) # 소수점 4자리 까지 표현
print("{0:10.4f}".format(y)) # 공백 10번 넣고 소수점 4자리 까지 표현

# { 또는 } 문자 표현하기
print("{{ YESSSSS!!!!!! }}".format()) # 포매팅이 아닌 { } 을 사용하고 싶으면 {{}} 이렇게 2번 쓰자
