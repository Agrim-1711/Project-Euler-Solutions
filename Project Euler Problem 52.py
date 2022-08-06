#Problem 52
#https://projecteuler.net/problem=52
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits

for n in range(1,1000000):
  a = str(n)
  b = str(2*n)
  c = str(3*n)
  d = str(4*n)
  e = str(5*n)
  f = str(6*n)
  if len(a) == len(b) == len(c) == len(d) == len(e) == len(f) and set(list(a)) == set(list(b)) == set(list(c)) == set(list(d)) == set(list(e)) == set(list(f)):
    print(a,b,c,d,e,f)
    break