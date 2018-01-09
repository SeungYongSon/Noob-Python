# 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요소값을 구하지 않고
# Key를 통해 Value를 얻는다.
# 해시(Hash)처럼 대응 관계로 나타낼 수 있는 자료형이다.

# 딕셔너리의 모습
# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
#
# Key를 통해 Value를 얻는다. 이것이 딕셔너리의 특징이다.
# Value2라는 값을 찾기 위해 순차적으로 모두 검색하는 것이 아닌
# Key를 통해 Value2라는 것이 있는 곳만 펼쳐보는 것이다.

dic = {'name': 'pey', 'phone': '0113534534543', 'birth': '1118'}
a = {1: 'hi'}  # Key에 정수값을 넣을 수 있고, Value에 'hi'라는 문자열을 넣을 수 있다.
a = {'hi': 1}  # 몰론 반대로도 가능하다.
a = {'a': [1, 2, 3]}  # Value에 리스트를 넣을 수 있다. 하지만 Key로 리스트를 넣는 것은 안된다.
a = {'a': (1, 2, 3)}  # Value에 튜플을 넣을 수 있다. 리스트와 반대로 Key로 튜플을 넣을 수 있다.
a = {1.234234: "what?"}  # Key에 실수 값을 넣을 수도 있다...

# 딕셔너리 추가, 삭제

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'  # 이렇게 하면 된다. 그러면 {1: 'a'}라는 딕셔너리에 2:'b'라는 딕셔너리 쌍이 추가된다.
print(a)

a['name'] = 'pey'  # {1: 'a', 2: 'b'}라는 딕셔너리에 'name':'pey' 라는 딕셔너리 쌍이 추가된다.
print(a)

a[3] = [1, 2, 3]  # {1: 'a', 2: 'b', 'name': 'pey'}라는 딕셔너리에 3: [1, 2, 3] 라는 딕셔너리 쌍이 추가된다.
print(a)

# 딕셔너리 요소 삭제하기
del a[1]  # key(1)에 해당하는 {key : value}({1 : 'a'} 쌍이 삭제된다
print(a)

# 딕셔너리 활용
# 그렇다면 딕셔너리는 어떻게 사용힐까?

# Key를 통해 Value 얻기
dic = {'name': 'pey', 'phone': '0113534534543', 'birth': '1118'}
a = dic['phone']  # 딕셔너리 변수[key]를 통해 Value을 얻을 수 있다.
print(a)

# 딕셔너리 만들 때 주의 사항

# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정하면
# 하나를 제외한 나머지 것들은 모두 무시된다.
# 다시말해 중복되는 Key를 사용하지 말자.
a = {1: 'a', 1: 'b'}
print(a)  # 출력시 {1: 'b'}가 나오는 것을 알 수 있다.

# 딕셔너리 관련 함수

# Key 리스트 만들기 keys
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())  # 딕셔너리 a의 Key만을 모아서 dict_keys라는 객체를 리턴한다.

# Value 리스트 만들기 values
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.values())  # Values만을 모아서 dict_values라는 객체로 리턴해준다.

# Key, Value 쌍 얻기 items
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.items())  # 딕셔너리 a의 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.

# 여기서 알아야 할점은 파이션 2.7 까지는 a.keys(), a.items() a.values() 함수들은
# 객체가 아닌 리스트를 리턴한다.
# 그 이유는 리스트를 리턴하기 위해서는 메모리의 낭비가 발생하기 때문이다.
# 그래서 3.0 이후 낭비를 줄이기 위해 dict_keys, dict_values, dict_items라는 객체를 리턴한다.

# 만약 리턴값으로 리스트가 필요할 경우 list()를 사용하면 된다.
b = list(a.keys())
print(b)
b = list(a.values())
print(b)
b = list(a.items())
print(b)
# 이렇게 얻어내면 된다.

# Key: Value 쌍 모두 지우기 clear
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a)
a.clear()  # 출력 되는 것 처럼 {} 모든 쌍이 사라진다.
print(a)  # 출력 -> {}

# Keys로 Value 얻기 get
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))
# a['name'] 과 같이 같은 결과 값을 돌려받지만
# a[Key]로 존재하지 않는 키로 값을 가져오라고 하면 오류를 발생시킨다.

# 하지만 get() 을 이용하면 None을 리턴한다.
print(a.get("joke"))

# 딕셔너리 안에 찾으려는 Key 값이 없을 경우
# 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶으면 get(x, "디폴트 값")을 사용하면 편리하다.
print(a.get("joke", "404"))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 in
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print('name' in a)  # 있으면 True 반환
print('joke' in a)  # 없으면 false 반환
