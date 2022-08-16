#Problem 38
#https://projecteuler.net/problem=38
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1

digits = set(str('123456789'))
largest = 0

for a in range(1,10000):
  for b in range(2,10):
    num_list = []
    for n in range(1,b+1):
      num_list.append(str(a*n))
    num = ''.join(num_list)
    if set(num) == digits and len(num) == 9:
      print(num)
      largest = max(largest,int(num))

print(f"The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1 is: /n {largest}!!!")
