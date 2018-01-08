#문자열 선언
# 따옴표를 이용해 그냥 대입하면 된다.
a = "Hello World"

#대입 하는 방법에는 3가지가 더 있다.
a = 'Hello World' #작은 따옴표로 양쪽 둘러싸기
a = """Hello World""" #큰 따옴표 3개를 연속으로 써서 양쪽 둘러싸기
a = '''Hello World''' #작은 따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print(a)

#문자열에 따옾표들을 사용하고 싶을때

#문자열에 작은따옴표 (') 포함시키기
# ex) Python's favorite food is perl
print("Python's favorite food is perl") # 큰 따옴표 이용

#문자열에 큰따옴표 (") 포함시키기
# ex) "Python is very easy." he says.
print('"Python is very easy." he says.') # 작은 따옴표 이용

# \(백슬래시)를 이용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
print('Python\'s favorite food is perl')
print("\"Python is very easy.\" he says.")

# 여러줄의 문자열을 대입하고 싶을때

# 이스케이프 코드 \n 사용
print("hello \n World \n :D")

# 작은따옴표 3개를 사용
multiline='''
 Life is too short
 You need 
 python
 '''
print(multiline)

# 큰따옴표 3개를 사용
multiline="""
 Life is too short
 You need 
 python
 """
print(multiline)
