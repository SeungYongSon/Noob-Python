# 패키지

# 패키지(Packages)는 도트(.)를 이용하여
# 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있다.
# 패키지 내의 모듈은 패키지. 모듈 : A.B 형식으로 관리된다. 자료구조의 Tree로 생각하면 편하다
# 예를 들어 모듈명이 A.B인 경우 A는 패키지명이 되고 B는 A 패키지의 B 모듈이 된다.

# 패키지 내의 모듈 import
import pack.bye

# 도트 연산을 통해 사용가능하다.
pack.bye.say_bye()

# from ~ import 사용으로 접근 줄이기
from pack import bye
bye.say_bye()

# 패키지 내 모듈의 함수만 import
from pack.hello import say_hello
say_hello()

# 와일드 카드 import
from pack.hello import *
say_hello()
say_hi()

#__init__.py 의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 패키지에 포함된 디렉터리에 __init__.py가 없다면 패키지로 인식이 안된다.
# (3.3 버전부터 __init__.py가 없어도 패키지로 인식되긴 한다.)

# __init__.py 의 all의 용도

# 특정 디렉터리의 모듈을 *를 이용하여 import할 때에는
# 해당 디렉터리의 __init__.py 파일에
# __all__이라는 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.
# __init__.py 의 내용을 확인해 보자.

# 패키지 내의 모든 모듈 import
from pack import *
# 패키지 내의 모든 모듈을 import한다고 쳤을 때(from 패키지 import 모듈)
# __init__.py에 __all__ 변수가 설정되어 있지 않으면 모듈 접근 시 NameError가 발생한다.
hello.say_hello()
bye.say_bye()
hello.say_hi()
