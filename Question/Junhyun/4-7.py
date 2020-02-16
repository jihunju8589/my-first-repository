# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

# Life is too short
# you need java


# ※ replace 함수를 사용해 보자.

f = open("junhyun_text.txt", 'r')
text = f.read()
f.close()
    
f1 = open("junhyun_text.txt", 'w')
text = text.replace("java", "python")
f1.write(text)
f1.close()