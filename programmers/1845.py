def solution(nums):
    types = len(set(nums))
    maxi = len(nums) // 2
    
    return min(types, maxi)