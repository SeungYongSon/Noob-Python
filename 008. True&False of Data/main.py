# 자료형에 참과 거짓이 있다.
# 이건 매우 중요한 특징이고 매우 자주 쓰인다.

# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓이 된다.
# 반대로 비여있지 않으면 참이 된다.

# 숫자에서는 그 값이 0일 때 거짓이 된다.

# None 이라는 것도 지금은 거짓을 뜻한다는 것만 알고 있자.

# 밑에는 참과 거짓이 쓰이는 부분이다.
a = [1, 2, 3, 4]
while a:
    print(a.pop())

# while 문은 조건문이 참일때 까지만 반복 수행된다.
# a가 pop()통해 비워지기 전까지 참 이다.
# 비워지면 거짓이 되기 때문에 while문을 탈출하게 된다.

# if 문에 있는 조건문에 비여있는 리스트가 있다.
# 비워있기 때문에 거짓이다. 그레서 else 문이 실행되고 "False"가 출력된다.
if []:
    print("True")
else:
    print("False")

# if 문에 있는 조건문에 값이있는 리스트가 있다.
# 비여있지 않기때문에 참이다. 그대로 실행되서 "True"가 출력된다.
if [1, 2, 3]:
    print("True")
else:
    print("False")
