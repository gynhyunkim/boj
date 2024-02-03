from sys import stdin
from collections import Counter

strs = stdin.readline().strip('\n').upper()
word_count = Counter(strs)
sorted_word_count = sorted(word_count.items(), key = lambda x:x[1], reverse = True)
#print(sorted_word_count)
if len(sorted_word_count) > 1 and sorted_word_count[0][1] == sorted_word_count[1][1]:
    print("?")
else:
    print(sorted_word_count[0][0])
