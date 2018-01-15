# 클래스 상속

# 상속(Inheritance)이란 "물려받다"라는 뜻으로, "재산을 상속받다"라고 할 때의 상속과 같은 의미이다.
# 클래스도 이런 개념이 적용할 수 있다.
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다
# 객체 간에 부모-자식 관계가 성립하는 경우(동물 - 고양이, 강아지 등)
# 상속 구조로 클래스를 설계할 수 있다

# 부모 클래스 생성
class Animal:
    def walk(self):
        print(self.__class__.__name__, 'is walking')

# 자식 클래스 생성
class Dog(Animal):
    pass

# 오버로딩
class Fox(Animal):
    def walk(self):
        super(Fox, self).walk()

# 오버라이딩
class Wolf(Animal):
    def walk(self):
        print(self.__class__.__name__, '는 걷는다.')

a = Dog()
a.walk()  # 부모 클래스에 있는 기능들을 사용 할 수 있다는 것을 알 수 있다.

b = Fox()
b.walk()  # 오버로딩 했을 때

c = Wolf()
c.walk()  # 오버라이딩 했을 때
