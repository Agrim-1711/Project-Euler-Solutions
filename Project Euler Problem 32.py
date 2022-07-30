#Problem 32
#https://projecteuler.net/problem=32
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital

digits = {'1','2','3','4','5','6','7','8','9'}
products = []
sum = 0

for a in range(10,100):
  for b in range(100,1000):
    c = a*b
    x = str(a)
    y = str(b)
    z = str(c)
    if set(x+y+z) == digits and len(x+y+z) == 9 and c not in products:
      print(x,y,z)
      products.append(c)
      sum += c

for a in range(1,10):
  for b in range(1000,10000):
    c = a*b
    x = str(a)
    y = str(b)
    z = str(c)
    if set(x+y+z) == digits and len(x+y+z) == 9 and c not in products:
      print(x,y,z)
      products.append(c)
      sum += c

print(products)
print(len(products))
print(sum)