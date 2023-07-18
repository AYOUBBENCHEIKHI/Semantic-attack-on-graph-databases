import networkx as nx
import matplotlib.pyplot as plt
import conformiteGrapheOntologie as rp

def CreationGrapheVoisins(graphesOntologie,grapheDonnee):
  GvoisinRespect = []
  Gvoisin = []
  # Obtenir tous les graphes voisins possibles
  for edge in grapheDonnee.edges():
      #copie le graphe origine  dans G_copy
      G_copy = grapheDonnee.copy()
      ed_type = grapheDonnee.edges[edge]["edge_type"]
      nodeS = edge[0]
      nodeE = edge[1]
      # suprime l'arete actuale
      G_copy.remove_edge(nodeS,nodeE)
      #ajouter le graphe voisin dans la liste des graphes G_Copys
      if rp.testSubClasse(graphesOntologie,G_copy):
        GvoisinRespect.append(G_copy)
      else :
        Gvoisin.append(G_copy)
      for node in G_copy.nodes():
        #copie le graphe G_copy  dans G2_copy
        G2_copy = G_copy.copy()
        if  node != nodeE :
          #ajouter une arete dans le graphe pour respect dis(G1,G2)=1
          G2_copy.add_edge(nodeS,node,edge_type = ed_type)
          #ajouter le graphe voisin dans la liste des graphes G_Copys
          if rp.testSubClasse(graphesOntologie,G2_copy):
            GvoisinRespect.append(G2_copy)
          else :
            Gvoisin.append(G2_copy)
  return GvoisinRespect,Gvoisin



# Lire le graphe à partir du fichier
onto = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/ontologie_person-animal_2.graphml")
# Lire le graphe à partir du fichier
graphe_origine = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheValide_person-animal_2.graphml")



print(" les graphes voisin ")
GvoisinRespect=[]
Gvoisin=[]
GvoisinRespect,Gvoisin = CreationGrapheVoisins(onto,graphe_origine)

print("nombre des graphe voisin respect lontologie ",len(GvoisinRespect))
print("nombre des graphe voisin respect pas  lontologie ",len(Gvoisin))