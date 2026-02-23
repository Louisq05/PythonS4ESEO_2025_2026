"""
Module core.io
--------------
Import/Export de graphes au format JSON.

Palier E.
"""

import json
from pathlib import Path
from .graph import Graph


# ============================================================================
# PALIER E : Import/Export
# ============================================================================

def save_graph(graph: Graph, filepath: str | Path) -> None:
    """
    Sauvegarde un graphe au format JSON.
    
    Format JSON:
    {
        "nodes": ["A", "B", "C"],
        "edges": [["A", "B"], ["B", "C"]]
    }
    
    Args:
        graph: Le graphe à sauvegarder
        filepath: Chemin du fichier de sortie
    
    Raises:
        IOError: Si l'écriture échoue
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> save_graph(g, "my_graph.json")
    """
    data=graph_to_dict(graph)       #Transforme le graph en dictionnaire
    with open(filepath, "w") as f:  #Créer un fichier json 
        json.dump(data, f)          #Ajout du dictionnaire au graph


def load_graph(filepath: str | Path) -> Graph:
    """
    Charge un graphe depuis un fichier JSON.
    
    Format JSON attendu:
    {
        "nodes": ["A", "B", "C"],
        "edges": [["A", "B"], ["B", "C"]]
    }
    
    Args:
        filepath: Chemin du fichier à charger
    
    Returns:
        Le graphe chargé
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si le format JSON est invalide
        KeyError: Si les clés "nodes" ou "edges" sont absentes
    
    Exemple:
        >>> g = load_graph("my_graph.json")
        >>> g.has_node("A")
        True
    """
    with open(filepath, "r") as f:  #Ouverture du fichier json
        data = json.load(f)         #Lecture et récupération des données
    return dict_to_graph(data)      #renvoie les données en graph avec la fonction dict_to_graph


def graph_to_dict(graph: Graph) -> dict:
    """
    Convertit un graphe en dictionnaire (utile pour serialization).
    
    Args:
        graph: Le graphe à convertir
    
    Returns:
        Dictionnaire avec clés "nodes" et "edges"
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> graph_to_dict(g)
        {'nodes': ['A', 'B'], 'edges': [['A', 'B']]}
    """
    return {
        "edges": graph.edges() if graph.edges()!=None else [], 
        "nodes": graph.nodes() if graph.nodes()!=None else [] 
    } #Ajout des noeuds et arrêtes
    


def dict_to_graph(data: dict) -> Graph:
    """
    Crée un graphe depuis un dictionnaire.
    
    Args:
        data: Dictionnaire avec clés "nodes" et "edges"
              - "nodes": liste de chaînes ["A", "B", "C"]
              - "edges": liste de paires [["A", "B"], ["B", "C"]]
                         (ou tuples : [("A", "B"), ("B", "C")])
    
    Returns:
        Le graphe créé
    
    Raises:
        KeyError: Si les clés requises sont absentes
        ValueError: Si le format est invalide (ex: arête invalide)
    
    Validation:
        - Clés "nodes" et "edges" doivent exister
        - "nodes" : liste de chaînes
        - "edges" : liste de paires [a, b] ou (a, b)
        - Chaque arête doit référencer des nœuds existants
    
    Exemple:
        >>> data = {'nodes': ['A', 'B'], 'edges': [['A', 'B']]}
        >>> g = dict_to_graph(data)
        >>> g.has_edge("A", "B")
        True
    """
    g=Graph()                   #Initialisation d'un graph vide
    for i in data["nodes"]:     #Parcours les noeuds contenu dans le Json
        g.add_node(i)           #Ajout des noeuds au graph
    for i in data["edges"]:     #Parcours les arrêtes contenu dans le Json
        g.add_edge(i[0],i[1])   #Ajout des graphes au graph
    return g                    #Renvoie le graph
