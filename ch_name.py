# 파일명 바꾸기
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG", "SSAFY"))