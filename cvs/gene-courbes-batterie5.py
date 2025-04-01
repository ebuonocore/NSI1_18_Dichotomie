""" Générateur de courbes de décharge de batterie (tableaux de float)
Décharge progressive puis brutales sur 50.000 données
sur 30 fichiers nommés de enreg1.csv à enreg30.csv
Ordonnées: début des valeurs autour de 5,5V. Passage obligatoire à 4,8V
"""

from random import * # importation de randint(limit_inf, limit_sup)
import matplotlib.pyplot as plt # importation de plt.plot() et plt.show()
import os # pour l'enregistrement des données 
import csv # pour acceder aux fichier selon le format csv

# Initialisations
dec = 1000
N = 60000 #Nombre de données par jour
L = [[0 for i in range (N)] for j in range (30)]
#L = [(None)*N]*30
S1 = [4.8]*N
absc = [0]*N
Evo1 = [0]*30
for i in range (N):
    absc[i] = i
p = (1/(10*N)) # pente régulière

# Génération des données pour les 30 jours
for j in range (30):
    supS1 = True
    supS2 = True
    rd = randint(1,6)-3
    for i in range (N):
        L[j][i] = (5.5 - p * (i + 3*(j +rd)) - ((i+100*(j+rd))/ (N - dec))**(20))
        if ((supS1 == True) and (L[j][i] <= 4.8)):
            supS1 = False
            Evo1[j] = i
            L[j][i] = 4.8
            #print ('4,8 forcé en ',i)
        if ((supS2 == True) and (L[j][i] <= 4.1)):
            supS2 = False
            L[j][i] = 4.1
            #print ('4,1 forcé en ',i)
        
# Enregistrement des données au format csv
for j in range (30):
    fichier = "enreg"+str(j)+".csv"
    mon_fichier = open(fichier, "w") 
    for i in range (len(L[j])-1):
        mon_fichier.write(str(L[j][i]))
        mon_fichier.write('\n')
    mon_fichier.write(str(L[j][-1]))
    mon_fichier.close()

# Enregistrement des données pas au format csv
#for j in range (30):
#    fichier = "enreg"+str(j)+".csv"
#    mon_fichier = open(fichier, "w") 
#    for i in range (len(L[j])-1):
#        mon_fichier.write(str(L[j][i]))
#        mon_fichier.write(';')
#    mon_fichier.write(str(L[j][-1]))
#    mon_fichier.close()

# Affichage des données
absc2 = []
absc2 = [r for r in range(0,N)]
plt.ylabel("Tension")
plt.xlabel("Temps en s")
for j in range (0,30,5):
    plt.plot(absc2,L[j],"-",label='enreg'+str(j))
plt.plot(absc2,S1,"-",label='4.8V')
plt.legend()
plt.show()
    

# Affichage des données: Evolution des t1
absc1 = []
absc1 = [r for r in range(0,30)]
plt.ylabel("t1")
plt.xlabel("jours")
plt.plot(absc1,Evo1,"o",label='Evolution de t1')
plt.legend()
plt.show()
