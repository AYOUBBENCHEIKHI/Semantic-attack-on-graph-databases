import networkx as nx
import matplotlib.pyplot as plt

#methode pour test les relation de sub classe
def testSubClasse(graphesOntologie,grapheDonnee):
  #liste pour prend tous les existe dans le graphes
  list_nodes = []
  # liste prend les types de chaque nodes ?prend la méme index
  list_types = []
  #list des nodes mere
  list_Mere =[]
  #liste des nodes fille
  list_fille = []
  #liste prend des vlaure vraie ou faux
  valide = []
  #extraire les sub classe de lontologie
  for edge in graphesOntologie.edges():
      edge_type = graphesOntologie.edges[edge]["edge_type"]
      if edge_type == "subClasse":
        list_Mere.append(edge[0])
        list_fille.append(edge[1])

  #extraire les node de graphes avec leur types
  for edge in grapheDonnee.edges() :
    edge_type = grapheDonnee.edges[edge]["edge_type"]
    if edge_type == "hasType":
        list_nodes.append(edge[0])
        list_types.append(edge[1])

  # le test de sub classe
  for i in range(len(list_nodes)):
    for j in range(len(list_Mere)):
      #test si un types de liste des types existe dans la liste des filles
      if list_types[i] ==  list_fille[j] :
          # prend la mere de cette nodes filles et prend le nodes des cet types et teste si elya une relation avec eux
          if grapheDonnee.has_edge(list_Mere[j],list_nodes[i]):
            for ed in grapheDonnee.edges():
                #chercher l'edge
                if ed == (list_Mere[j],list_nodes[i]):
                  ed_type = grapheDonnee.edges[ed]["edge_type"]
                  #teste le type de edge si un subClasse
                  if ed_type == "subClasse":
                    valide.append(True)
                  else:
                    valide.append(False)
          else:
              valide.append(False)

  try:
    index = valide.index(False)
    return False
  except ValueError:
    return True
  #return valide


def testDomainRange(graphesOntologie,grapheDonnee):
  #liste des triplets de ontologie
  domains_ranges_relation_onto = []
  #liste des triplets de graphe
  domains_ranges_relation_graphe = []
  #liste pour prend tous les existe dans le graphes
  nodes = []
  # liste prend les types de chaque nodes prend la méme index
  types =[]
  #liste prend des vlaure vraie ou faux
  valide = []
  #extraire les relation  de lontologie
  for edge in graphesOntologie.edges():
      edge_type = graphesOntologie.edges[edge]["edge_type"]
      if edge_type != "subClasse":
        chain = edge[0] +":"+edge[1]+":"+edge_type
        domains_ranges_relation_onto.append(chain)
  #faire le test sur les données
  for edge in grapheDonnee.edges() :
    edge_type = grapheDonnee.edges[edge]["edge_type"]
    if edge_type != "hasType" and edge_type != "subClasse":
      chi = edge[0] +":"+edge[1]+":"+edge_type
      domains_ranges_relation_graphe.append(chi)
    if edge_type == "hasType":
        nodes.append(edge[0])
        types.append(edge[1])
  for i in range(len(domains_ranges_relation_graphe)):
    for j in range(len(domains_ranges_relation_onto)):
      dg,rag,rg = domains_ranges_relation_graphe[i].split(":")
      do,rao,ro = domains_ranges_relation_onto[j].split(":")
      # la relation de l'ontologie si la meme relation dans le graphe
      if (rg == ro) :
        indexDomaineG = nodes.index(dg)
        indexRangeG = nodes.index(rag)
        typeDomaineG = types[indexDomaineG]
        typeRangeG = types[indexRangeG]
        # si la domzine de lontologie et la meme parrapport a domain dans le graphes
        if typeDomaineG == do and typeRangeG == rao:
          valide.append(True)
        else :
          valide.append(False)
  try:
    index = valide.index(False)
    return False
  except ValueError:
    return True



def testDisjoint(graphesOntologie,grapheDonnee):
  #liste des triplets de ontologie
  domains_ranges_relation_onto = []
  #liste des triplets de graphe
  domains_ranges_relation_graphe = []
  #liste pour prend tous les existe dans le graphes
  nodes = []
  # liste prend les types de chaque nodes prend la méme index
  types =[]
  #liste prend des vlaure vraie ou faux
  valide = []
  #extraire les relation  de lontologie
  for edge in graphesOntologie.edges():
      edge_type = graphesOntologie.edges[edge]["edge_type"]
      if edge_type == "Disjoint":
        chain = edge[0] +":"+edge[1]+":"+edge_type
        domains_ranges_relation_onto.append(chain)
  #faire le test sur les données
  for edge in grapheDonnee.edges() :
    edge_type = grapheDonnee.edges[edge]["edge_type"]
    if  edge_type == "Disjoint":
      chi = edge[0] +":"+edge[1]+":"+edge_type
      domains_ranges_relation_graphe.append(chi)
    if edge_type == "hasType":
        nodes.append(edge[0])
        types.append(edge[1])
  for i in range(len(domains_ranges_relation_graphe)):
    for j in range(len(domains_ranges_relation_onto)):
      dg,rag,rg = domains_ranges_relation_graphe[i].split(":")
      do,rao,ro = domains_ranges_relation_onto[j].split(":")
      indexDomaineG = types.index(do)
      indexRangeG = types.index(rao)
      nodeDomaineG = nodes[indexDomaineG]
      nodeRangeG = nodes[indexRangeG]
      if grapheDonnee.has_edge(nodeRangeG,do):
        for ed in grapheDonnee.edges():
          #chercher l'edge
          if ed == (nodeRangeG,do):
            ed_type = grapheDonnee.edges[ed]["edge_type"]
            if ed_type == "hasType":
              valide.append(False)
      valide.append(True)
  try:
    index = valide.index(False)
    return False
  except ValueError:
    return True




"""# Lire le graphe à partir du fichier
onto = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/ontologie_person-animal_2.graphml")
# Lire le graphe à partir du fichier
G_valide = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheValide_person-animal_2.graphml")
# Lire le graphe à partir du fichier
G_non_valide = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheNonValide_person-animal_4.graphml")


if testSubClasse(onto,G_non_valide):
  print("le graphe respect l'ontologie...:)")
else :
  print("le graphe ne respect pas l'ontologie....!")"""