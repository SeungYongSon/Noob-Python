# while 문

# while문 기본 구조
#
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#          ....
#
# 조건문이 거짓이 될때까지 계속 반복한다.

# 밑에 주석처리된 while문은 조건문이 계속 참이기 때문에 무한 루프가 된다.
# while True:
#    print("True")

# while문 강제로 빠져나오기 break
while True:
    print("True")
    break  # 아무리 무한루프로라도 강제로 나올 수 있다.


# 조건에 맞지 않는 경우 맨 처음으로 돌아가기 continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0 : continue  # a가 짝수일때 맨 처음 조건문으로 돌아간다.
    print(a)  # 결국 1~10 까지의 홀수만 출력 된다.
