#Problem 42
#https://projecteuler.net/problem=42
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words

from words import words
from letter2val import letter2val

word_val = []
tri_word = 0

for n in range(0,len(words)):
  score = 0
  temp = list(words[n])
  for i in range(0,len(temp)):
    score += letter2val[temp[i]]
  word_val.append(score)

tri_num = [int(n*(n+1)/2) for n in range(1,21)]

for v in word_val:
  if v in tri_num:
    tri_word += 1

print(tri_word)