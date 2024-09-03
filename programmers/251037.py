def solution(bandage, health, attacks):
    t, x, y = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    max_health = health
    current_health = health
    last_attack_time = 0  # 마지막 공격 시간
    bandage_time = 0  # 연속 성공 시간
    
    for attack_time, damage in attacks:
        # 시간 경과에 따른 회복 처리
        time_passed = attack_time - last_attack_time
        if bandage_time + time_passed >= t:
            # 붕대 감기 성공
            current_health += min(bandage_time * x + time_passed * x + y, max_health - current_health)
            bandage_time = 0  # 성공 후 초기화
        else:
            # 연속 붕대 감기 도중 공격 받음
            current_health += min(time_passed * x, max_health - current_health)
            bandage_time += time_passed  # 경과된 시간만큼 연속 시간 증가
        
        # 공격에 의한 체력 감소
        current_health -= damage
        if current_health <= 0:
            return -1  # 캐릭터 사망
        
        # 공격 이후 연속 성공 시간 초기화
        bandage_time = 0
        last_attack_time = attack_time
    
    return current_health

# 테스트 실행
bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bandage, health, attacks))  # 예상 출력: 5

# 2024.09.03