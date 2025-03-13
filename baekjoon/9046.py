from collections import Counter

T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    text = input().replace(" ", "")  # 공백 제거
    counter = Counter(text)  # 문자 빈도수 계산
    most_common = counter.most_common()  # 빈도수 내림차순 정렬

    max_freq = most_common[0][1]  # 최빈 문자 빈도수
    max_chars = [char for char, freq in most_common if freq == max_freq]  # 최빈 문자 리스트

    print(max_chars[0] if len(max_chars) == 1 else "?")  # 최빈 문자가 하나면 출력, 여러 개면 '?'
