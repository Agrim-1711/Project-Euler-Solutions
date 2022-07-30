#Problem 45
#https://projecteuler.net/problem=45
#Find the next triangle number that is also pentagonal and hexagonal

tri_num = [int(n*(n+1)/2) for n in range(1,100001)]
pent_num = [int(n*(3*n-1)/2) for n in range(1,100001)]
hex_num = [int(n*(2*n-1)) for n in range(1,100001)]

# print(tri_num)
# print(pent_num)
# print(hex_num)

for n in tri_num:
  if n in pent_num and n in hex_num:
    print(n)