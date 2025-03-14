from collections import Counter
text = input().upper()
counter = Counter(text)

most_common = counter.most_common()
#print(most_common)

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print("?")
else:
    print(most_common[0][0])