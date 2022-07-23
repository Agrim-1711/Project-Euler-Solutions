#Problem 48
#https://projecteuler.net/problem=48
#Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰

series = 0
for n in range(1,1001):
  series += pow(n,n)

#print(series)

digits = list(str(series))
#print(digits)

for m in range(len(digits)-10,len(digits)):
  print(digits[m])