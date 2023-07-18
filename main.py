import conformiteGrapheOntologie as rp
import genererVoisinsGraphe as g
import probabiliteReponse as pcr
import networkx as nx
import matplotlib.pyplot as plt

# Lire le graphe à partir du fichier
onto = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/ontologie_person-animal_2.graphml")
# Lire le graphe à partir du fichier
G_valide = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheValide_person-animal_2.graphml")
# Lire le graphe à partir du fichier
G_non_valide = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheNonValide_person-animal_4.graphml")





if rp.testSubClasse(onto,G_non_valide):
  print("le graphe respect l'ontologie...:)")
else :
  print("le graphe ne respect pas l'ontologie....!")

#generation des voisin 
# Lire le graphe à partir du fichier
graphe_origine = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheValide_person-animal_2.graphml")

print(" les graphes voisin ")
GvoisinRespect=[]
Gvoisin=[]
GvoisinRespect,Gvoisin = g.CreationGrapheVoisins(onto,graphe_origine)

print("nombre des graphe voisin respect lontologie ",len(GvoisinRespect))
print("nombre des graphe voisin respect pas  lontologie ",len(Gvoisin))

POR=pcr.probabliteConditinneleGrapheOrigine(GvoisinRespect,graphe_origine)
POV =pcr.probabliteConditinneleGrapheOrigine(Gvoisin,graphe_origine)
print("POV :",POV)
print("POR :",POR)