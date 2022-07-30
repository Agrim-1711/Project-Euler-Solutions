#Problem 39
#https://projecteuler.net/problem=39
#For which value of p ≤ 1000, is the number of solutions maximised

sol_p = []

for a in range(1,1000):
  for b in range(a,1000):
    c = pow(a**2 + b**2, 1/2)
    p = int(a+b+c)
    if c == int(c) and p <= 1000:
      # print(p,(a,b,int(c)))
      sol_p.append(p)

# print(len(sol_p))

max1 = 0

for s in sol_p:
  c = sol_p.count(s)
  print(s,c)
  max1 = max(max1,c)

print(max1)