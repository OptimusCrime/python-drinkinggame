import random

lag = ['Thomas','Marthe','Stine','Ole C','Tale','Kari','Håkon','Kristian']

i = 0
lagNr = 1
linje = ""
while len(lag) > 0:
	if len(lag) == 1:
		rand = 0
	else:
		rand = random.randrange(0,len(lag)-1)
	
	if i % 2 != 0:
		print("Lag "+str(lagNr)+" er: "+linje+" og "+lag[rand])
		lagNr += 1
	else:
		linje = lag[rand]
	lag.pop(rand)
	i += 1