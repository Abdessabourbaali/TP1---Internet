import csv
Nom=[]
PatteInterieur=[]
PatteExterieur=[]
IP=[]

with open('RT1-TP1 - A1.csv') as csvfile:
	reader=csv.reader(csvfile)
	print (reader)
	for row in list(reader)[1:]:
		Nom.append(row[0])
		PatteInterieur.append(row[1])
		PatteExterieur.append(row[2])
		IP.append(row[3])
	
for i in range (len(Nom)):
	print ("ip route add dst-adress = "+PatteInterieur[i]+" gateway = "+PatteExterieur[i])