# 모듈

# 모듈은 함수나 변수 또는 클래스 들을 모아 놓은 파일이다.
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할수 있게끔 만들어진
# 파이썬 파일이라고도 할 수 있다.

# import
# 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에
# 있는 모듈만 불러올 수 있다.
import mod  # import를 통해 현재 디렉터리에 있는 mod.py를 불러온다.

print(mod.safe_sum(10, 30))  # mod 에있는 safe_num() 함수를 사용할 수 있다.

# from import
# from 모듈이름 import 모듈함수 또는 클래스
# 이걸 사용하면 모듈이름을 붙이지 않고 바로 해당 모듈의 함수, 클래스를 사용 가능하다.
from mod import safe_sum, sum  # , 콤마를 통해 여러개의 함수, 클래스를 불러올수 있다.
print(safe_sum(20, 30))
print(sum(20, 40))

# 여기서 좀더 나아가서 와일드카드 import가 가능하다
# 다시말해 모듈에 있는 모든 함수, 클래스를 불러올 수 있다.
from mod import *
say_python()
