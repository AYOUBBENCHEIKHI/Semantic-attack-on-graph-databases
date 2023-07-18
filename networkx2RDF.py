import networkx as nx
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.plugins.sparql import prepareQuery
import random
def covertireNetworkx2Rdf(graphe,namespace="example"):
   # Créer un graphe RDF vide
  g = Graph()
  # Créer un namespace pour les nœuds du graphe
  ns = Namespace("http://"+namespace+".org/")

  # Ajouter les nœuds du graphe à RDF
  for node in graphe.nodes:
      node_uri = URIRef(ns + node)
      g.add((node_uri, URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef(ns + "Node")))
      g.add((node_uri, URIRef(ns + "label"), Literal(node)))

  # Ajouter les arêtes du graphe à RDF
  for source, target, data in graphe.edges(data=True):
      source_uri = URIRef(ns + source)
      target_uri = URIRef(ns + target)
      edge_uri = URIRef(ns + source + "_" + target)
      g.add((edge_uri, URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef(ns + "Edge")))
      g.add((edge_uri, URIRef(ns + "source"), source_uri))
      g.add((edge_uri, URIRef(ns + "target"), target_uri))
      g.add((edge_uri, URIRef(ns + "edge_type"), Literal(data["edge_type"])))
  return g
def grapheQuery(graphe,query=""):
  # Définir un namespace
  g = covertireNetworkx2Rdf(graphe)
  ns = Namespace("http://example.org/")

  # Définir la requête SPARQL
  query = prepareQuery('''
      SELECT (COUNT(?node) AS ?count)
      WHERE {
          ?node ?p ?o .
          FILTER (?node = ex:ayoub)
      }
  ''', initNs={"ex": ns})

  # Exécuter la requête SPARQL et afficher le résultat
  reponce = 0
  for row in g.query(query):
      reponce =  int(row[0])
  return reponce

def ajouteBruit(reponse):
    listRepense = []
    for i in range (1000):
        listRepense.append(reponse + round(random.uniform(0,3), 0))
    return listRepense


"""G_valide = nx.read_graphml("C:/Users/ayoub/Desktop/stage/graphes/grapheValide_person-animal_2.graphml")
rep = grapheQuery(G_valide,query="")
liR = ajouteBruit(rep)
print(rep)
print(liR)"""