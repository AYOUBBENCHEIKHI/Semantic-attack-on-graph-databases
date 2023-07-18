import random
import networkx2RDF as n2r
import numpy as np
#Methode choisi une reponce aleatoire
def reponce(graphe,requet = ""):
  """#ctte Str representer les reponce possible par la reque
  Str = "A B C D"
  letters_list = Str.split()
  # Choisir une lettre aléatoire dans la liste
  random_letter = random.choice(letters_list)
  # Afficher la lettre aléatoire choisie"""
  reponse = n2r.grapheQuery(graphe)
  reponses= n2r.ajouteBruit(reponse)
  return reponses

#calculer la probaliter de chaque reponce parapport a 1000 fois
def ReponceMemeRequet(graphe,requet = ""):
  liste_reponce = []
  for i in range(1000):
    # on appele methode reponce pour donnée la reponce pour la meme requet
    pb = reponce(graphe,requet)
    liste_reponce.append(pb)
  return liste_reponce


#clacule la probabiliter de chaque reponce dans le,meme graphes
def probabiliteReponce(graphe,reponces):
  # Créer des dictionnaires pour stocker le nombre d'occurrences de chaque reponce
  probabiliteReponce = {}
  counts = {}
  somme = len(reponces)
  # Compter le nombre d'occurrences de chaque reponce dans la liste
  for item in reponces:
      if item in counts:
          counts[item] += 1
      else:
          counts[item] = 1
  # calculer la pb  le nombre d'occurrences de chaque reponce
  for key, value in counts.items():
    prb = (value/somme)
    probabiliteReponce[key] = prb
  return probabiliteReponce,counts

def probabliteGrapheOrigine(listGrapheVoisin,GrapheOrigine):
  reponcesOR = reponce(GrapheOrigine,requet = "")
  probabliteGrapheOrigine,count = probabiliteReponce(GrapheOrigine,reponcesOR)
  probabliteGrapheVoisins = []
  for i in range(len(listGrapheVoisin)):
    reponces = reponce(listGrapheVoisin[i],requet = "")
    pbR,_ = probabiliteReponce(listGrapheVoisin[i],reponces)
    probabliteGrapheVoisins.append(pbR)
  return probabliteGrapheOrigine,probabliteGrapheVoisins,count

def probabliteConditinneleGrapheOrigine(listGrapheVoisin,GrapheOrigine):
  #PO : probabilite de graphe origine, PV :probabilite de graphe Voisines
  PO,PV,count =probabliteGrapheOrigine(listGrapheVoisin,GrapheOrigine)
  prC = {}
  someK={}
  print(count)
  print(PV)
  #for k,v in count.items():
  for dic in PV:
    for k,v in (count.items()) and (dic.items()) :
      if k == 
      someK[k]=  dic[k]
  #prC[k] = PO[k]/someK[k]
  print("****************",someK)
  """SrepA = 0
  SrepB = 0
  SrepC = 0
  SrepD = 0
  for dic in PV:
    SrepA = SrepA + dic["A"]
    SrepB = SrepB + dic["B"]
    SrepC = SrepC + dic["C"]
    SrepD = SrepD + dic["D"]
  prC["A"] = PO["A"] /SrepA
  prC["B"] = PO["B"] /SrepB
  prC["C"] = PO["C"] /SrepC
  prC["D"] = PO["D"] /SrepD"""
  return prC