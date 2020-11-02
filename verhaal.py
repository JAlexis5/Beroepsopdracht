import time
import os

#15 keuzes 9 eindes / 21 keuzes 4 eindes

print("Door de Ogen van Fadi")
time.sleep(1)
print("Verhaal door Jelani Alexis, gecodeerd door Jelani Alexis")
time.sleep(1)

while True:
	startcheck = input("Typ START om te beginnen of QUIT om te sluiten: ")
	if startcheck.lower() == "start":
		print('START')
		time.sleep(1)
		break
	elif startcheck.lower() == "quit":
		print('Tot ziens')
		raise SystemExit
	else:
		print("Geldige invoer leveren s.v.p.")

print("Je wordt wakker op een normale dag in Syrië. Het is in het oosten onrustig, maar bij jou is er nog niks aan de hand.")
time.sleep(1)
print("Je bent net klaar met ontbijten. Opeens hoor je het luchtalarm, maar het is niet de dag waarop ze getest worden.")
time.sleep(1)
#keuze 1
print("Je hoort in de verte een hele luide knal. Een paar minuten later nog een, en dan nog een. Wat doe je?")
print("(a) Blijf zitten")
print("(b) Ren weg")

while True:
	choice1check = input()
	if choice1check.lower() == "a":
		print("Je blijft zitten en hoopt op het beste resultaat.")
		time.sleep(2)
		print("Jammer genoeg landde de eerstvolgende bom 2 huizen verderop.")
		time.sleep(1)
		print("Game over.")
		print("Einde 1: Het Snelle Einde")
		raise SystemExit
	elif choice1check.lower() == "b":
		print("Je rent zo snel mogelijk naar je auto en rijdt zo snel mogelijk weg.")
		time.sleep(1)
		break
	else:
		print("Geldige invoer leveren s.v.p.")

#keuze 2
print("Je ontkomt de bommen net aan. Wat doe je?")
print("(a) Je gaat naar een andere stad")
print("(b) Je wacht een tijdje en gaat terug naar huis")

while True:
	choice2check = input()
	if choice2check.lower() == "a":
		print("Je gaat naar een andere stad toe.")
		time.sleep(1)
		break
	elif choice2check.lower() == "b":
		print("Je wacht even en komt terug naar je stad. Je huis staat er niet meer.")
		time.sleep(1)
		break
	else:
		print("Geldige invoer leveren s.v.p.")

os.system('CLS')
print("Je besluit je vriend op te bellen en hem te vertellen wat er is gebeurd.")
time.sleep(1)
print("Hij laat je overnachten in zijn gastkamer.")
time.sleep(1)
print("De volgende dag word je wakker en hoor je hetzelfde als gisteren gebeuren.")
time.sleep(1)
print("Het is niet meer veilig in Syrië. Je gaat vluchten.")
time.sleep(1)

#keuze 3
print("Je hebt 2 keuzes, je kan vluchten met de auto, of je kan met de hulp van een smokkelaar ontsnappen.")
print("(a) Ontsnappen met de auto")
print("(b) Mensensmokkelaar om hulp vragen")

while True:
	choice3check = input()
	if choice3check.lower() == "a":
		auto = True
		print("Je gaat met de auto vluchten.")
		break
	elif choice3check.lower() == "b":
		auto = False
		print("Je vraagt een mensensmokkelaar om hulp.")
		break
	else:
		print("Geldige invoer s.v.p.")

#keuze 4
print("Naar welk land ga je vluchten?")
print("(a) Turkije")
print("(b) Nederland")

while True:
	choice4check = input()
	if choice4check.lower() == "a":
		turkije = True
		print("Je gaat naar Turkije vluchten.")
		break
	elif choice4check.lower() == "b":
		turkije = False
		print("Je gaat naar Nederland vluchten.")
		break
	else:
		print("Geldige invoer s.v.p.")

#tak 1
if auto == True and turkije == True:
	print("Je rijdt een stuk naar de Turkse grens. Welke route ga je nemen om er te komen?")
	print("(a) Kortere maar gevaarlijkere route")
	print("(b) Langere stukken veiligere route")
	while True:
		choice5check = input()
		if choice5check.lower() == "a":
			print("Je neemt de korte, gevaarlijkere route.")
			time.sleep(1)
			print("Helaas word je gevonden door Assad's aanhangers.")
			print("Game over.")
			print("Einde 2: Haastige spoed is zelden goed")
			raise SystemExit
		elif choice5check.lower() == "b":
			print("Je neemt de langere maar veiligere route, en je komt zonder problemen aan bij de Turkse grens.")
			print("")