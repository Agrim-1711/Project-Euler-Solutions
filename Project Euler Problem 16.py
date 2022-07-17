#Problem 16
#https://projecteuler.net/problem=16
#What is the sum of the digits of the number 2¹⁰⁰⁰?

num = pow(2,1000)
print(num)
sum = 0

for digit in str(num):
  sum = sum + int(digit)
  print(f"The running sum is {sum}!")

print(f"The total sum of the digits is {sum}!")