num = []  # 빈 리스트 생성
bod = [1, 1, 2, 2, 2, 8]  # 정답 리스트
ans = []  # 결과 저장 리스트

# 사용자 입력 받기
for i in range(6):
    n = int(input())  # 한 개의 숫자를 입력받아 정수로 변환
    num.append(n)  # 리스트에 추가

# 정답과 비교하여 차이 계산
for i in range(6):
    ans.append(bod[i] - num[i])  # bod[i]에서 num[i]를 뺀 값을 저장

print(*ans)  # 리스트 내용을 공백으로 구분하여 출력