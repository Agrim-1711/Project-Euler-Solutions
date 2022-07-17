#Problem 17
#https://projecteuler.net/problem=17
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
word = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
num2word = dict(zip(num,word))
#print(dictionary)

#num_test = []
#word_test = []
#dict_test = dict(zip(num_test,word_test))
#print(dict_test)

total = 0

for n in range(1,100):
  a = n % 10
  b = n - a
  if n <= 20:
    print(n)
    word = num2word[n]
    print(word)
    length = len(num2word[n])
    print(f"{length}\n")
    total = total + length
  else:
    print(b,a)
    word = num2word[b],num2word[a]
    print(word)
    length = len(num2word[b]) + len(num2word[a])
    print(f"{length}\n")
    total = total + length

print(total)