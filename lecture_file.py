#!/usr/bin/python3
# coding: utf-8 


#Ouverture et traitement du fichier labyrinth.txt

N = 15
FichierLabyrinth = open('labyrinth.txt', 'r') # instanciation de l'objet Fichier 
lignes, colonnes = 15, 15

liste = [ 0 for i  in range(0)]

# On crée une liste vide
index = 0
i=0
j=0
for i in range(N):
	for j in range(N):
		lab = FichierLabyrinth.read()
		lab = lab.replace('\n','') 
		
		while index < len(lab):
			if index =='\n':
				j+=1
			if index !='\n':
				char = lab[index]
				
				#Les 3 instructions suivantes sont correctes pour l'ajout d'un élément dans une liste
				#t.append(x)
				#t = t + [x]
				#t += [x]
				liste.append(char)
				index +=1
for i, elt in enumerate(liste): #"i" est l'index de ma liste et "elt" correspond au contenu à cet index (soit les caractères o ou w)
	print("À l'indice {} se trouve {}.".format(i, elt))
#test: print liste
liste2 =[]
nb_lin = 15
nb_col = len(liste) // nb_lin
mat = [[''] * nb_col for i in range(nb_lin)]
for pos, elt in enumerate(liste):
    i = pos // nb_lin
    j = pos % nb_lin 
    mat[i][j] = elt
    myTuple = (i, j)
    print ( myTuple, mat[i][j])
    liste2 += [myTuple, mat[i][j]]

print liste2
#print (liste2[2]) 

#test : print mat [0][0]
FichierLabyrinth.close()
