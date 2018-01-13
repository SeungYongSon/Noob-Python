# if문

# if문의 기본 구조
if True:
    print("True")
else:
    print("False")
# 조건문을 테스트해서 참이면 if문 바로 다음의 문장(if 블록)들을 수행
# 거짓이면 else문 다음 의 문장(else 블록)들을 수행.
# else문은 if문 없이 독립적으로 사용 불가.

# 기호 : 와 들여쓰기
# if문을 만들 때 if 조건문 앞에 :을 붙여야한다. 딱히 의미는 없고 문법이기 떄문이다.
# 그리고 바로 아래 문장부터 if문에 속하는 모든 문장에
# 들여쓰기(indentation)를 해야한다.
if True:
    print("들여쓰기1")
    print("들여쓰기2")
    print("들여쓰기3")

# 그렇다면 if문에 사용되는 조건문은 무엇일까?
# 조건문은 참과 거짓을 판단하는 문장이다.

# 자료형의 참과 거짓
# 숫자 자료형 -> 0아 아닌 숫자는 모두 참
# 문자열 자료형 -> 내용이 있으면 참
# 리스트 자료형 -> 요소가 있으면 참
# 터플 -> 요소가 있으면 참
# 딕셔너리 -> 요소가 있으면 참

# 비교 연산자

# x < y   x가 y보다 작다
# x > y   x가 y보다 크다
# x == y  x와 y가 같다
# x != y  x와 y가 같지 않다
# x >= y  x가 y보다 크거나 같다
# x <= y  x가 y보다 작거나 같다

# and , or ,  not

# x or y   x와 y 둘중에 하나만 참이면 참이다
# x and y  x와 y 모두 참이어야 참이다.
# not x    x가 거짓이면 참이다.

x = 1
y = 0
# x 는 참이고 y 는 거짓이다.

if x or y:  # y는 거짓이만 x는 참이므로 조건문은 참이된다.
    print("True")
else:
    print("False")

if x and y:  # y는 거짓이 아니므로 조건문은 거짓이 된다.
    print("True")
else:
    print("False")

if not y:  # y는 거짓이므로 조건무은 참이 된다.
    print("True")
else:
    print("False")

# 리스트, 튜플, 문자열에 X라는 요소가 있는가? 대한 조건문
#  X in S,  X not in S

# X in S -> X 가 S안에 있는가?
# X not in S -> X 가 S안에 없는가?
print(1 in [1, 2, 3])  # 1이 리스트 [1, 2, 3]에 있으므로 참
print(1 not in [1, 2, 3])  # 1이 리스트 [1, 2, 3]에 있으므로 거짓

a = ['paper', 'cellphone', 'money']
if 'money' in a:  # 리스트 a에 'money'라는 요소가 있는가?
    print("머니머니머니머니")  # 있으므로 참
else:
    print("노머니")


# 조건문에서 아무 일도 일어나지 않게 하기 pass
if 'money' in a:
    pass  # 이걸 쓰면 그냥 지나간다.
else:
    print("노머니")

# 다양한 조건을 판단하느 elif
a = ['paper', 'paper']
card = 1
if 'money' in a:  # a에 'money'가 없음
    print("머니머니머니")
elif card:  # elif로 들어감. card 가 1이라 참임. 밑에 문장 실행
    print("카드카드카드")
else:
    print("노머니")


# if문 줄여보기
a = ['paper', 'cellphone', 'money']
if 'money' in a: pass
else: print("노머니")  # 이렇게 줄이면 된다.
