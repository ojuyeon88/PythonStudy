def is_group_word(word):
    seen = set()  # 이미 본 문자들을 저장
    prev_char = ''  # 이전 문자를 저장
    
    for char in word:
        if char != prev_char:
            if char in seen:
                return False  
            seen.add(prev_char)  
        prev_char = char 
    
    return True 

def solution(n, words):
    count = 0 
    
    for word in words:
        if is_group_word(word):
            count += 1
    
    return count

# 입력 받기
n = int(input()) 
words = [input().strip() for _ in range(n)] 

# 결과 출력
print(solution(n, words))
