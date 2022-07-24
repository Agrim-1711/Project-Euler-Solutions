#Problem 31
#https://projecteuler.net/problem=31
#How many different ways can £2 be made using any number of coins

arget = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1] + [0]*target

for coin in coins:
    # print(coin)
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]
    # print(ways)

print (f"Ways to make £{int(target/100)} =", ways[target])