import sys

words = [sys.stdin.readline().strip() for _ in range(5)]
max_length = max(len(word) for word in words)
result = ""

# 세로로 읽기
for i in range(max_length):
    for word in words:
        if i < len(word):  
            result += word[i]

# 결과 출력
print(result)
