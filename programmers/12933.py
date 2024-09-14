def solution(n):
    string_n = str(n)
    sorted_string = ''.join(sorted(string_n, reverse=True))
    return int(sorted_string)