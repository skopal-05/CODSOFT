import string
import random
 
l1= list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

length = input("Enter desired length of password  ")

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

num=int(length)

part1 = round(num * (30/100))
part2 = round(num * (20/100))

result = []

for x in range(part1):
    result.append(l1[x])
    result.append(l2[x])

for x in range(part2):
    result.append(l3[x])
    result.append(l4[x])

random.shuffle(result)

password = "".join(result)
print("Strong Password: ", password)
