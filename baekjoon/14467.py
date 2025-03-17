import sys

def count_cow_crossings(observations):
    cow_positions = {}  # 각 소의 마지막 위치를 저장할 딕셔너리
    crossing_count = 0
    
    for cow_id, position in observations:
        if cow_id in cow_positions:
            if cow_positions[cow_id] != position:  # 위치가 바뀌었으면 길을 건넘
                crossing_count += 1
        
        cow_positions[cow_id] = position  # 현재 위치 저장
    
    return crossing_count

def main():
    n = int(sys.stdin.readline().strip())
    observations = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
    result = count_cow_crossings(observations)
    print(result)

if __name__ == "__main__":
    main()