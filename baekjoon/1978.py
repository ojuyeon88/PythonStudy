import math  # 제곱근을 구하기 위해 필요

def is_prime(num):
    if num < 2:  
        return False
    if num in (2, 3):  
        return True
    if num % 2 == 0:
        return False
    
    for i in range(5, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

T = int(input())  # 테스트 횟수 입력
prime_count = 0  # 소수 개수 카운트

for _ in range(T):
    num = int(input())  # 숫자 입력
    if is_prime(num):  # 소수인지 판별
        prime_count += 1

print(prime_count) 