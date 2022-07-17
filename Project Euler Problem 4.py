#Problem 4
#https://projecteuler.net/problem=4
#Find the largest palindrome made from the product of two 3-digit numbers

answer = 0

for p in range(100,1000):
  for q in range(100,1000):
    d = list(str(p*q))
    l = len(d)
    palindrome = True
    for i in range(0,(l//2)):
      if d[i] != d[l-i-1]:
        palindrome = False
        break
    if palindrome:
      answer = max(answer,p*q)

print(f"{answer} is the answer!")