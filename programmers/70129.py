def solution(s):
    transformation_count = 0
    total_removed_zeros = 0 
    
    while s != "1":
        removed_zeros = s.count("0")  # 현재 문자열에서 제거할 0의 개수
        total_removed_zeros += removed_zeros  # 총 제거된 0의 개수에 추가
        s = s.replace("0", "")  # 0 제거
        s = bin(len(s))[2:]  # 현재 문자열의 길이를 이진수로 변환 (0b 제거)
        transformation_count += 1  # 변환 횟수 증가
    
    return [transformation_count, total_removed_zeros]
