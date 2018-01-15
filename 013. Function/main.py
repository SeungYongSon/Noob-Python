# 함수

# 파이썬 함수의 구조
#
# def 함수명(입력 인수):
#   <수행할 문장1>
#   <수행할 문장2>
#      ....
#
def SumTwoNum(a, b):
    result = a + b
    return result

c = SumTwoNum(10, 20)
print(c)  # 값이 30 출력

# 함수의 형태

# 일반적인 함수
def sum(a, b):
    result = a + b
    return result

# 입력값이 없는 함수
def say():
    return 'Hi'

# 리턴값이 없는 함수
def sum(a, b):
    print("{0} + {1} = {2}".format(a, b, a + b))

# 입력값도 결과값도 없는 함수
def say():
    print('Hi')


# 입력 인수가 몇 개 인지 모를떄

# 문법
#
# def 함수명(*입력변수):
#   <수행할 문장1>
#   <수행할 문장2>
#      ....
#
def SumMany(*args): # 여러 정수 값을 더하는 함수.
    sum = 0
    for i in args:
        sum = sum + i
    return sum


result = SumMany(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 여러 값을 넣어도 문제가 없다.
print(result)  # 1 ~ 10 까지 더했기 때문에 55가 출력된다.


# 함수의 리턴값은 언제나 하나다.
def SumAndMul(a, b):  # a, b의 더한값과 곱한값을 돌려주는 함수
    return a+b, a*b  # 리턴시 (a+b, a*b) 라는 튜플로 값을 리턴한다.


result = SumAndMul(3, 4)
print(result)

# 입력 인수 초깃값 미리 설정하기
def PreSum(a = 10, b = 30):
    return a + b

result = PreSum()  # 초깃값을 함수에서 설정했기 때문에 인수가 없어도 괜찬다.
print(result)

result = PreSum(5, 10)  # 인수 입력시 입력된 값을 통해 함수가 실행된다.
print(result)
