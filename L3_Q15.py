import random


f = open('D:/DORA/mashup/python/file.txt','r')
line = f.read().splitlines()
r = random.choice(line)
print(r)