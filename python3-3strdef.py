#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 첫번쨰 문자가 대문자인지 확인해주는
print(len(python)) # 문자 길이 확인
print(python.replace("Python", "Java")) # Python 을 찾아서 Java로 변경

index = python.index("n") #문자가 어느 위치에 있는지 확인 가능 n
print(index)
index = python.index("n", index + 1) # n을 찾은 5위치에서 하나를 더한 6위치에 부터 또 n 이 나오는 위치를 찾는
print(index)

print(python.find("n")) # index와 같은 기능
print(python.find("Java")) # 내가 원하는 값이 이변수에 포함하지 않을경우 -1을 반환
#print(python.index("Java")) # 내가 원하는 값이 이변수에 포함하지 않을경우 오류를 내버리고 종료시켜버림
print("hi") # 결과값 index일경우 오류, find일경우 -1

print(python.count("n")) # python 이란 변수에서 n 이 몇번 등장하는지 계산해줌