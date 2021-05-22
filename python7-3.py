# 파일 입출력
# socre_file = open("score.txt", "w", encoding="utf8") # w 쓰기 용도
# print("수학 : 0", file=socre_file)
# print("영어 : 50", file=socre_file)
# socre_file.close()

# socre_file = open("score.txt", "a", encoding="utf8") # a 이어쓰기
# socre_file.write("과학 : 80") #write 로 입력추가할땐 줄바꿈이 따로 없음
# socre_file.write("\n코딩 : 100")
# socre_file.close()

# 한번에 모든 내용
# socre_file = open("score.txt", "r", encoding="utf8") #r 리드를 뜻함 파일에 있는 내용을 읽어오는 용도
# print(socre_file.read())
# socre_file.close()

# 한줄 한줄
# socre_file = open("score.txt", "r", encoding="utf8")
# print(socre_file.readline(), end="") #줄별로 읽기, 한줄읽고 커서는 다음줄로 이동
# print(socre_file.readline())
# print(socre_file.readline())
# print(socre_file.readline())
# socre_file.close()

# print(socre_file.readline(), end="") 
# print(socre_file.readline(), end="")
# print(socre_file.readline(), end="")
# print(socre_file.readline(), end="")
# socre_file.close()

# socre_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = socre_file.readline()
#     if not line:
#         break
#     print(line) #줄바꿈없애려면 end="" 추가
# socre_file.close()

socre_file = open("score.txt", "r", encoding="utf8")
lines = socre_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

socre_file.close()