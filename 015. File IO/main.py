# 파일 입출력

# 파일 객체 = open(파일 이름, 파일 열기 모드)

# 파일 열기 모드
# r - 읽기모드: 파일을 일김나 할 때 사용
# w - 쓰기모드: 파일에 내용을 쓸 때 사용
# a - 추가모드: 파일의 마지막에 새로윤 내용을 추가 시킬 때 사용

# 파일을 쓰기모드로 열면 해당 파일이 이미 존재할 경우
# 원래 있던 내용이 모두 사라진다.
# 존재하지 않으면 새로운 파일이 생성된다.

# 아래 코드를 통해 정말 그런지 알아보도록 하자.
f = open("File\TextFile.txt", 'w')
f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("File\TextFile.txt", 'w')
for i in range(1, 11):
    data = "%d lines.\n" % i
    f.write(data)
f.close()

# 파일을 읽는 여러가지 방법

# readline()

#파일의 첫 번째 줄 읽기
f = open("File\TextFile.txt", 'r')
line = f.readline()  # 첫 번째 줄을 읽어온다.
print(line)
f.close()

# 몰론 모든 줄을 읽을 수도 있다.
f = open("File\TextFile.txt", 'r')
while True:
    line = f.readline()
    if not line: break  # 더이상 읽을 라인이 없으면 break 시켜서 무한 루프를 탈출한다.
    print(line)
f.close()

# relines() 함수
f = open("File\TextFile.txt", 'r')
lines = f.readlines()
# 파일에 쓰여진 모든 내용들을 각각의 줄을 요소로 만들고
# ['1 lines.\n', '2 lines.\n', ,..] 으로 리스트를 만들고 리턴한다.
print(lines)  # 리스트 출력
for line in lines:  # for문으로 요소들을 출력한다.
    print(line)
f.close()

# read() 함수
f = open("File\python.txt", 'r')
data = f.read()  # 파일의 내용 전체를 문자열로 리턴한다.
print(data)
f.close()

# 파일에 새로운 내용 추가하기
# 원래 있던 값을 유지하면서 새로운 값을 추가 가능하다.
f = open("File\TextFile.txt", 'a')
for i in range(11, 20):
    data = "%d lines.\n" % i
    f.write(data)
f.close()

# with문 사용하기
with open("File\python.txt", 'w') as f:  # 이러면 자동으로 close 해줘서 편하다.
    f.write("Life is too short, you need python")

