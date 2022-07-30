#Problem 33
#https://projecteuler.net/problem=33
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator

product = 1

for a in range(10,100):
  for b in range(10,100):
    if b > a and a % 11 != 0 and b % 11 != 0 and '0' not in (str(a)+str(b)):
      # print(a,b)
      x = str(a)
      y = str(b)
      if (x[1]==y[0] and int(x[0]) / int(y[1]) == a/b) or (x[0]==y[1] and int(x[1]) / int(y[0]) == a/b):
        product = product * (a/b)
        print(a,b)

print(product)