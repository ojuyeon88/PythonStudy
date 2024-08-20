def solution(n):
    x = 1
    while n >= x :
        if n % x != 1 :
            x =  x + 1
        elif n % x == 1 : 
            break

    return x