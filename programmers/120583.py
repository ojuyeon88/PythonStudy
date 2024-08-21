# def solution(array, n):
#     answer = 0
#     for i in array :
#         if i == n :
#             answer = answer + 1
#     return answer

def solution(array, n):
    return array.count(n)