def stampaDizionario(diz):
    for key,value in dizionario.items():
        print("la chiave è ... "+key)
        print("il valore è ... "+str(value))

def totaleOre(dict):
    somma = 0 
    for key,value in dizionario.items():
        somma = somma + value
    return(somma)

def modifica(diz,prof,ore):
    if prof in diz:
        diz[prof]=ore

dizionario = {"Rossi":18, "Bianchi":16, "Venarucci":6}
#inserire un elemento nel dizionario
dizionario["Viola"]=14
print(dizionario)
#modificare un coppia chiave valore
dizionario["Bianchi"]=18
print(dizionario)
#iterare sul dizionario
for key,value in dizionario.items():
    print("la chiave è ... "+key)
    print("il valore è ... "+str(value))

#calcolare il totale delle ore del dizionario
somma = 0 
for key,value in dizionario.items():
    somma = somma + value

print("la somma delle ore è " + str(somma))

#numero degli insegnanti con cattedra piena
c=0
for key,value in dizionario.items():
    if value == 18:
        c+=1

print(c)
    
stampaDizionario(dizionario)
modifica(dizionario, "Rossi", 6)
print(dizionario)
#scrivere una funzione che modifica le ore 
    
