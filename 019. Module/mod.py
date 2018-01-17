# mod 라는 모듈에 함수들을 선언했다.
def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할수 있는 것이 아님")
    else:
        result = sum(a, b)
    return result


def say_python():
    print("Hello, Python!")
