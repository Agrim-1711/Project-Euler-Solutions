#Problem 23
#https://projecteuler.net/problem=23
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers

def sum_factors(f):
  
  temp1 = pow(f,1/2)
  temp2 = int(temp1)
  factors = []
  
  if temp1 == temp2:
    for d in range(2,temp2):
      if f % d == 0:
        factors.append(d)
        factors.append(f//d)
    factors.append(temp2)
  
  else:
    for d in range(2,temp2+1):
      if f % d == 0:
        factors.append(d)
        factors.append(f//d)

  if f != 1:
    factors.append(1)
  
  sum = 0
  
  for factor in factors:
    sum = sum + factor

  #print(f,factors,sum)
  return sum

numbers = []
abundant = []
for n in range(1,28124):
  numbers.append(n)
  if n < sum_factors(n):
    abundant.append(n)

#print(numbers)
print(len(abundant))

#Create a dictionary to store our numbers
my_dictionary = dict.fromkeys(numbers,"false")
print(len(my_dictionary))

updated = 0

for p in range(0,len(abundant)):
  for q in range(0,len(abundant)):
    sum = abundant[p] + abundant[q]
    if sum in my_dictionary:
      my_dictionary[sum] = "true"
      updated += 1
print(updated)

from collections import Counter
count = Counter(my_dictionary.values())
print(count)

sum = 0
found = 0
for key, value in my_dictionary.items():
  if value == "false":
    found += 1
    sum += key
print(found)
print(sum)