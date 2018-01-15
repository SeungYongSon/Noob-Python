# 클래스

# 클래스는 객체를 찍어내기 위한 틀이라고 생각하면 된다.
# 클래스를 인스턴스화하면 객체가 나온다.


class Profile:
    user_count = 0  # 클래스 변수, 클래스가 만들어질때 생긴다.

    def __init__(self, name, pw, image, content):  # 생성자
        # 객체만이 가지는 필드를 가리키는 self 키워드가 있음. this 와 거의 동일
        self.name = name
        self.pw = pw
        self.image = image
        self.content = content
        # 위에 4개의 변수가 인스턴스 변수, 인스턴스시 만들어진다.
        Profile.user_count += 1  # 클래스 변수한테 접근가능하다.

    # 소멸자
    # del로 인해 소멸할 객체는 이 메소드를 call하며 소멸함
    def __del__(self):
        Profile.user_count -= 1

    def print_profile(self):
        print("*" * 25)
        print("name : {0}".format(self.name))
        print("image : {0}".format(self.image))
        print("content : {0}".format(self.content))
        print("*" * 25)

    def change_profile(self, pw, name, image, content):
        if self.pw == pw:
            self.name = name
            self.image = image
            self.content = content
            return True
        else:
            return False


# 인스터스화 해서 객체 생성
user1 = Profile('python12312312', 'ppap13123213', "img2", "I LIke Python")
user2 = Profile('파이션112312312', 'funcamera12312', "img3", "I LIke C#")

print("User count: %d" % Profile.user_count)

print(user1.print_profile())

print(user1.change_profile('ppap13123213', '파이션12345', 'img44', 'I Like JAVA'))
print(user1.print_profile())

print(user1.change_profile('aapa12312312', '파이션시러', 'img666', 'I Like C++'))
print(user1.print_profile())

del user1
print("User count: %d" % Profile.user_count)  # 이걸 통해 user1이 삭제되었다는 것을 알 수 있다.
