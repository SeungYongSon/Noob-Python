# 문자열 연산 #

# 문자열 더해서 연결하기
head = "Py"
body = 'thon'
tail = ' is fun!!'

done = head + body + tail
print(done)

# 문자열 곱하기
print(body * 2)

# 문자열 곱하기 응용
print("*")
print("*" * 2)
print("*" * 3)
print("*" * 4)

# 문자열 인덱싱과 슬라이싱 #

# 인덱싱 : 가리킨다 , 슬라이싱 : 잘라낸다

# 인덱싱 Indexing
s = "Life is short, You need Python"
print(s[0])  # print -> 'L'
print(s[1])  # print -> 'i'
print(s[2])  # print -> 'f'
print(s[3])  # print -> 'e'

print(s[0], " = ", s[-0])  # s[0] 과 s[-0] 은 같다

print(s[-2])  # print -> 'o'
print(s[-5])  # print -> 'y'

# 슬라이싱 Slicing
s = "Life is too short, You need Python"
ns = s[0] + s[1] + s[2] + s[3]
print(ns)

print(s[0:4])  # print -> 'Life'
print(s[0:3])  # print -> 'Lif'
print(s[12:17])  # print -> 'short'
print(s[19:])  # print -> 'You need Python'
print(s[:])  # print -> 'Life is too short, You need Python'
print(s[19:-7])  # print -> 'You need'

# 슬라이싱 활용(문자열 나누기)
s = "Life is too short, You need Python"
a = s[:18]
b = s[18:]
print(a)
print(b)

# 문자열 관련 함수들 #

# 문자 개수 세기 count
a = "DSMCHEGO"
print(a.count('D')) # 문자열 중에 'D'의 개수를 반환

#위치 알려주기1 find
a = "Python Flask"
print(a.find('P')) # 문자열에 'P' 가 처음으로 나온 위치의 인덱스를 반환
print(a.find('M')) # 문자열에 'M'이 없어서 -1 을 반환

#위치 알려주기2 index
a = "DSM is very Fun. Join this school. um.. sorry. It's joking"
a.index('t') # find와 기능은 같지만 문자열에 원하는 문자를 찾지 못하면 오류가 발생한다.

#문자열 삽입 join
a = "!"
print(a.join("최강한화 "))  # '최강한화 ' 라는 문자열의 각각의 문자 사이에 a의 값인 '!'을 삽입

#소문자를 대문자로 바꾸기 upper
a = "asDf"
print(a.upper()) # 이미 대문자인 'D'는 아무런 변화가 없다.

#대문자를 소문자로 바꾸기 lower
a = "FAsD"
print(a.lower()) # 이미 소문자인 's'는 아무런 변화가 없다, 당연하다.

# 왼쪽 공백 지우기 lstrip
a = " DSM "
print(a)
print(a.lstrip())  # 왼쪽 공백이 지워진 것을 알 수 있다. lstrip에서 l은 left를 뜻한다.

#오른쪽 공백 지우기 rstrip
a = " DSM "
print(a)
print(a.rstrip())  # 오른쪽 공백이 지워진 것을 알 수 있다. 마찬가지로 rstrip 에서 r은 right를 뜻한다.

#양쪽 공백 지우기 strip
a = " DSM "
print(a)
print(a.strip())  # 양쪽 공백이 지워진 것을 알 수 있다.

#문자열 바꾸기 replace
a = "Life is very suck!!!"
print(a.replace("suck", "fun"))  # replace(바뀔 문자열, 바꿀 문자열) 바뀔 문자열을 바꿀 문자열로 치환해 준다.

# 문자열 나누기 split
a = "Life is too short"
print(a.split()) # spilt에 아무런 값을 넣지 않으면 공백(스페이스, 탭, 엔터등)을 기준으로 문자열을 나눈다.
a = "최!강!한!화!"
print(a.split('!')) # 이처럼 값을 넣으면 값을 기준으로 문자열을 나눈다.
