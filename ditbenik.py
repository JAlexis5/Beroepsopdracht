import time
import datetime
import os
import sys

nu = datetime.datetime.now()
Jelani = ("Jelani")
jelani = ("jelani")

print("Hello You!, ik ben Jelani.")
time.sleep(1.5)

print("Wie ben jij? (Voer je naam in en druk op Enter.)")
naam = input()

print("Aan het scannen...")
time.sleep(2)

print("Welkom! Jouw naam is" , naam + "!")
if naam == Jelani:
    time.sleep(2)
    print("Alhoewel ik een vermoeden heb dat je lult laat ik je wel inloggen, 1 seconde...")
    time.sleep(2.5)
if naam == jelani:
    time.sleep(2)
    print("Alhoewel ik een vermoeden heb dat je lult laat ik je wel inloggen, 1 seconde...")
    time.sleep(2.5)

print("Login Time:")
print(nu)
time.sleep(1)

print("Wil je dit programma herstarten of doorgaan naar de vragen? D om door te gaan, H om te herstarten.") 
antwoord = input()
if antwoord == ("h") or ("H"):
    os.execl(sys.executable, sys.executable, *sys.argv)
elif antwoord == ("d") or ("D"):
    print("Dan gaan we door!")
    
    
