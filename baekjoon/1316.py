n = int(input())

def solution(n):
    strings = []
    for i in range(n):
        group_input = input()
        strings.append(group_input)
    return strings

def group_word(strings):
    seen = set()
    prev_char = ''

    for char in strings[0]:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(prev_char)
        prev_char = char

    return True

def end():
    print()