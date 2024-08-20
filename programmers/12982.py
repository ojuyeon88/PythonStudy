def solution(d, budget):
    d.sort() 
    total_sum = 0  
    count = 0 

    for amount in d:
        if total_sum + amount <= budget:
            total_sum += amount
            count += 1
        else:
            break  # 예산을 초과하므로 반복 종료
    
    return count