# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) #대괄호로 가져올떄는 오류
print(cabinet.get(5)) #get이용시 none이라고 하고 계속 이어감
print(cabinet.get(5, "사용 가능")) # 5라는 값을 가져올려고 시도하고 없으면 "사용가능"값을 준다
print("hi")

print(3 in cabinet) # True 캐비넷에 있을 경우
print(5 in cabinet) # False 캐비넷에 없을 경우

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새로운 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호" #캐비넷에 "C-20" 이란 키를 만들고 "조세호"라는 값을 넣겠다 / "C-20"이란 키가 사용 즁이면 값이 업데이트되는것
print(cabinet)

#간 손님
del cabinet["A-3"] # 키 값 삭제
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 함께 출력하려면
print(cabinet.items())

# 목욕탕 마감
cabinet.clear()
print(cabinet)