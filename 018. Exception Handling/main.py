# 예외 처리

# 오류 예외 처리 기법

# try , except 문

#
# try:
#   ...
# except[발생오류[as 오류 메시지 변수]]:
#   ...
#

# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
# 하지만 try 블록에서 아무 오류가 없으면
# except 블록은 수행되지 않는다.

# except [발생 오류 [as 오류 메시지 변수]]:

# try, except 만 쓰기
# 오류 종류에 상관없이 오류가 발생하기만 하면
# except 블록문을 수행
try:
    4/0
except:
    print("에러!!!")

# 발생 오류만 포함한 except문
# 오류가 발생했을 때 except문에 미리 정해 놓은
# 오류 이름과 일치할때 만 except문을 수행
try:
    4 / 0
except ZeroDivisionError:
    print("에러!!!")

# 발생 오류와 오류 메세지 변수까지 포함한 except문
# 위 except 코드에서 오류 메세지의 내용까지 알고 싶을 때
# 사용하는 방법이다.
try:
    4 / 0
except ZeroDivisionError as e:
    print("에러!!! -> ", e)


# try ... else

# else절은 예외가 발생하지 않은 경우에 실행된다.
# 반드시 except절 바로 다음에 위치해야 한다.

try:  # python.txt 파일이 없으므로 except 블록이 수행됨
    f = open('python.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()

try:  # test.txt 파일이 있으므로 else 블록이 수행됨
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()
000
# try ... finally

# finally문은 try문 수행 도중 예외 발생 여부에 상관 없이 항상 수행된다.
# 보통 리소스를 close 해햐 할 경우에 많이 사용된다.
try:
    f = open('python.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
finally:
    f.close()

# 여러개의 오류처리하기

#
# try:
#     ...
# except 발생 오류1:
#     ...
# except 발생 오류2:
#     ...
#

# 이 코드는 인데싱 오류가 먼저 발생하기 때문에
# 4/0으로 발생되는 ZeroDivisionError는 발생하지 않는다.
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:  # 함께 오류 처리가 가능하다.
    print(e)

# 오류 피하기

# pass 를 통해 피할 수 있다.
try:
    f = open("python.txt", 'r')
except FileNotFoundError:
    pass


# 오류 만들기

# 예외처리를 하기 위해서 오류를 만들어서 사용할 수도 있다.
class MyError(Exception):
    def __str__(self):
        return "JAVA라니..."


def say_py(py):
    if py == 'JAVA':
        raise MyError()
    print(py)

try:
    say_py("PYTHON")
    say_py("JAVA")
except MyError as e:
    print("에러! -> ", e)
