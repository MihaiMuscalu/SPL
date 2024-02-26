import random
N1= random.randrange(10,30)
sum =0
while N1 != 15 and N1 != 25:
    sum += N1
    N1 = random.randrange(10,30)

print(sum)