# with
import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

#피클 사용하지않고 일반적인 파일을 쓰고 읽는것을 위드를 활용해서
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
#
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
