#Problem 17
#https://projecteuler.net/problem=17
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used

num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000]
word = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']
num2word = dict(zip(num,word))
#print(num2word)

#num_test = []
#word_test = []
#dict_test = dict(zip(num_test,word_test))
#print(dict_test)

total = 0

for n in range(1,1001):
  digits = str(n)

  if n <= 20:
    print(n)
    word = num2word[n]
    print(word)
    length = len(num2word[n])
    print(f"{length}\n")
    total = total + length
  
  elif n < 100:
    a = int(str(digits[0]))
    b = int(str(digits[1]))
    print(a*10,b)
    word = num2word[a*10],num2word[b]
    print(word)
    length = len(num2word[a*10]) + len(num2word[b])
    print(f"{length}\n")
    total = total + length

  elif n % 100 == 0 and n < 1000:
    a = int(str(digits[0]))
    print(a,0,0)
    word = num2word[a],num2word[100]
    print(word)
    length = len(num2word[a]) + len(num2word[100])
    print(f"{length}\n")
    total = total + length

  elif n % 100 <= 20 and n < 1000:
    a = int(str(digits[0]))
    b = n - a*100
    print(a,b)
    word = num2word[a],num2word[100],num2word[b]
    print(word)
    length = len(num2word[a]) + len(num2word[100]) + len(num2word[b]) + 3
    print(f"{length}\n")
    total = total + length

  elif n < 1000:
    a = int(str(digits[0]))
    b = int(str(digits[1]))
    c = int(str(digits[2]))
    print(a,b*10,c)
    word = num2word[a],num2word[100],num2word[b*10],num2word[c]
    print(word)
    length = len(num2word[a]) + len(num2word[100]) + len(num2word[b*10]) + len(num2word[c]) + 3
    print(f"{length}\n")
    total = total + length

  else:
    a = int(str(digits[0]))
    print(a)
    word = num2word[a],num2word[1000]
    print(word)
    length = len(num2word[a]) + len(num2word[1000])
    print(f"{length}\n")
    total = total + length

print(total)
