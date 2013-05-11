import random

a = open("sporsm.txt", "r", encoding = "utf8")
utskrift = a.readlines()
while True:
	b = random.randrange(0, len(utskrift))
	print(utskrift[b].strip())
	foo = input()