#문자열 포맷
# print("a" + "b")
# print("a", "b")

#방법 1
print("나는 %d살입니다." % 20) # d 는 정수값만 넣을 수 있음
print("나는 %s을 좋아해요." % "파이썬") # s 는 문자열 String 값을 넣겠다
print("Apple 은 %c로 시작해요." % "A") # c는 캐릭터라서 한 글자만 받겠단
# %s 로만 쓰면 정수건 문자건 상관없이 출력 가능

print("나는 %s살입니다." % 20) # d 는 정수값만 넣을 수 있음
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 순서대로 대입

#방법 2
print("나는 {}살입니다.".format(20)) # 중괄호
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 순번에 맞게
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 순번에 맞게

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간")) # 변수 처럼 중가로 속에 있는 값을 포맷 뒤에있는 값으로 가져가다 쓴다
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20)) # 순서 상관없이

#방법 4(Python v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")