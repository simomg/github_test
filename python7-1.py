# 표준 입출력
# import sys
# #print("Python", "Java", sep=",", end="?") #end 의미는 이 문장의 끝부분을 물음표로 바꿔달라
# #print("무엇이 더 재밌을까요?")
# print("Python", "Java", file=sys.stdout) #표준 출력으로 문장이 찍히는것
# print("Python", "Java", file=sys.stderr) #표준 에러로 처리

#시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #키인 서브젝트 밸류 스코어 튜플로 쌍으로보냄
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust왼쪽으로 정렬을 하는데 총 8칸의 공간을 확보한 상태에서 왼쪽으로 정렬
#     #오른쪽 정렬을 하는데 총 4칸의 공간을 확보

#대기 순번표
#001, 002, 003
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") # 사용자 입력을 통해서 값을 받게되면 문자열형태로 저장 
answer = 10 # 
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")