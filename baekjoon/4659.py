def is_valid_password(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    has_vowel = False  # 모음 포함 여부
    vowel_count = 0  # 연속된 모음 개수
    consonant_count = 0  # 연속된 자음 개수
    prev_char = ''  # 이전 문자 저장
    
    for i, char in enumerate(password):
        # 모음 체크
        if char in vowels:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0  # 모음 -> 자음 카운트 리셋
        else:
            consonant_count += 1
            vowel_count = 0  # 자음 -> 모음 카운트 리셋
        
        # 모음 또는 자음이 3번 연속 등장하면 실패
        if vowel_count == 3 or consonant_count == 3:
            return False
        
        # 같은 글자가 연속적으로 두 번 오는지 확인
        if i > 0 and char == prev_char:
            if char not in {'e', 'o'}:
                return False
        
        prev_char = char  # 이전 문자 업데이트
    
    return has_vowel  # 모음이 하나라도 포함되어야 True


# 반복 입력 처리
while True:
    password = input().strip()
    
    if password == "end":
        break 
    
    if is_valid_password(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
