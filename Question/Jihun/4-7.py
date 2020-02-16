# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

# Life is too short
# you need java


# ※ replace 함수를 사용해 보자.
f1 = open("jihun_test.txt", 'r')
text=f1.read()
f1.close()

f2 = open("jihun_test.txt", 'w')
replaceAll=text.replace("java", "python")
f2.write(replaceAll)
f2.close()

