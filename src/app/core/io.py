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
    data ={
        "edges": graph.edges() if graph.edges()!=None else [],
        "nodes": graph.nodes() if graph.nodes()!=None else [] 
    }
    print(data)
    with open(filepath, "w") as f:
        json.dump(data, f)


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
    with open(filepath, "r") as f:
        data = json.load(f)
    g=Graph()
    for i in data["nodes"]:
        g.add_node(i)
    for i in data["edges"]:
        g.add_edge(i[0],i[1])
    return g


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
    # TODO: implémenter
    pass


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
    # TODO: implémenter
    # Validation requise :
    # 1. Vérifier que "nodes" et "edges" existent
    # 2. Créer un graphe vide
    # 3. Ajouter tous les nœuds
    # 4. Pour chaque arête :
    #    - Vérifier format (liste/tuple de 2 éléments)
    #    - Vérifier que a et b existent dans nodes
    #    - Ajouter l'arête
    # 5. Gérer les exceptions proprement
    pass
