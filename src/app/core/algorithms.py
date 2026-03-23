"""
Module core.algorithms
-----------------------
Implémentation des algorithmes de parcours de graphes (DFS, BFS)
et résolution de problèmes classiques.

Paliers B, C, D.
"""

from collections import deque
from .graph import Graph


# ============================================================================
# PALIER B : DFS (Depth-First Search / Parcours en profondeur)
# ============================================================================

def dfs(graph: Graph, start: str) -> list[str]:
    """
    Parcours en profondeur (DFS) à partir d'un nœud de départ.
    
    Utilise une pile (implémentée avec une liste Python).
    Visite les voisins dans l'ordre alphabétique (grâce à graph.neighbors()).
    
    Args:
        graph: Le graphe à parcourir
        start: Le nœud de départ
    
    Returns:
        Liste des nœuds visités dans l'ordre du parcours DFS
    
    Raises:
        ValueError: Si le nœud de départ n'existe pas
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("A", "C")
        >>> g.add_edge("B", "D")
        >>> dfs(g, "A")
        ['A', 'B', 'D', 'C']  # Ordre déterministe car voisins triés alphabétiquement
    
    Note:
        ⚠️ CRITIQUE : Le résultat est déterministe car Graph.neighbors() retourne 
        une liste triée alphabétiquement. Ne pas modifier cet ordre !
    
    Algorithme:
        1. Créer une pile avec le nœud de départ
        2. Créer un ensemble de nœuds visités
        3. Tant que la pile n'est pas vide:
           - Dépiler un nœud
           - Si déjà visité, continuer
           - Marquer comme visité
           - Empiler tous ses voisins non visités
    """
    pile = []                       # Création de la pile de départ
    explored = set()                # Création de l'ensemble des noeuds explorés
    result=[]                       # Création de la liste des résultats
    pile.append(start)              # Ajout du start à la pile
    while pile!=[]:                 # Tant que la pile n'est pas vide :
        i=pile.pop()                # On retire le dernier élément : pop() = FO de LIFO
        if i not in explored:       # Si le noeud n'est pas déja visité :
            explored.add(i)         # On l'ajoute dans le set des noeuds visités
            result.append(i)        # Et dans la liste des résultats
        
            for x in reversed(graph.neighbors(i)):          # On inverse la sortie neighbors pour contourner le problème de l'odre alpha
                if x not in explored:                       # Si le noeud n'a pas encore été visité :
                    pile.append(x)                          # On l'ajoute à la pile : append = LI de LIFO
    return result   


def dfs_path(graph: Graph, start: str, goal: str) -> list[str] | None:
    """
    Trouve un chemin entre deux nœuds avec DFS.
    
    Args:
        graph: Le graphe à parcourir
        start: Nœud de départ
        goal: Nœud cible
    
    Returns:
        Liste des nœuds du chemin (incluant start et goal)
        None si aucun chemin n'existe
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("B", "C")
        >>> dfs_path(g, "A", "C")
        ['A', 'B', 'C']
    
    Algorithme:
        Variante de DFS où on stocke le chemin complet dans la pile.
        Pile contient des tuples (nœud, chemin_jusqu'ici).
    """
    path=[]                          #Création de la liste décrivant le chemin
    if start==goal:                  #On regarde si le chemin est immédiat
        return [start]
    for x in dfs(graph,start) :      #Parcours la pile donné par le dfs
        path.append(x)               #Ajout de l'élement au chemin
        if x==goal:                  #Si l'élement est l'arrivée
            return path              #On s'arrete et renvoie le chemin
    return None


# ============================================================================
# PALIER C : BFS (Breadth-First Search / Parcours en largeur)
# ============================================================================

def bfs(graph: Graph, start: str) -> list[str]:
    """
    Parcours en largeur (BFS) à partir d'un nœud de départ.
    
    Utilise une file (collections.deque).
    Explore le graphe couche par couche.
    
    Args:
        graph: Le graphe à parcourir
        start: Le nœud de départ
    
    Returns:
        Liste des nœuds visités dans l'ordre du parcours BFS
    
    Raises:
        ValueError: Si le nœud de départ n'existe pas
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("A", "C")
        >>> g.add_edge("B", "D")
        >>> bfs(g, "A")
        ['A', 'B', 'C', 'D']  # Ordre par couches
    
    Algorithme:
        1. Créer une file avec le nœud de départ
        2. Créer un ensemble de nœuds visités
        3. Tant que la file n'est pas vide:
           - Défiler un nœud
           - Marquer comme visité
           - Enfiler tous ses voisins non visités
    """
    # Astuce : file = deque(), visited = set
    file = deque()                                  # Création de la file : dequeu pour implementer le FIFO
    visited = []
    result = []
    file.append(start)

    while file:
        node = file.popleft()                       # popleft = FO de FIFO
        if node not in visited:
            visited.append(node)
            result.append(node)
            for neighbor in graph.neighbors(node):  # ordre alphabétique conservé
                if neighbor not in visited:
                    file.append(neighbor)           # append = FI de FIFO
    return visited

def bfs_path(graph: Graph, start: str, goal: str) -> list[str] | None:
    """
    Trouve le PLUS COURT chemin entre deux nœuds avec BFS.
    
    Args:
        graph: Le graphe à parcourir
        start: Nœud de départ
        goal: Nœud cible
    
    Returns:
        Liste des nœuds du plus court chemin (incluant start et goal)
        None si aucun chemin n'existe
    
    Note:
        BFS garantit de trouver le plus court chemin en nombre d'arêtes
        pour un graphe non pondéré.
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("B", "C")
        >>> g.add_edge("A", "C")  # Chemin direct plus court
        >>> bfs_path(g, "A", "C")
        ['A', 'C']
    
    Algorithme:
        Variante de BFS où on stocke le chemin complet dans la file.
        File contient des tuples (nœud, chemin_jusqu'ici).
    """
    if start == goal:               # Si la condition est remplie
        return [start]              # Sortie de la fonction
    file = deque()
    visited = []  
    file.append((start, [start]))   # (noeud actuel, chemin jusqu'ici)

    while file:
        node, path = file.popleft() # popleft = FO du FIFO
        if node not in visited:
            visited.append(node)
            for neighbor in graph.neighbors(node):
                if neighbor == goal:
                    return visited+ [neighbor]        #Changement de la logique pour l'affichage (a revoir)
                if neighbor not in visited:
                    file.append((neighbor, path + [neighbor]))      # Ajouter les voisins plus le chemin
    return None


# ============================================================================
# PALIER D : Problèmes classiques sur graphes
# ============================================================================

def is_connected(graph: Graph) -> bool:
    """
    Vérifie si le graphe est connexe.
    
    Un graphe est connexe si tous les nœuds sont atteignables
    depuis n'importe quel nœud.
    
    Args:
        graph: Le graphe à vérifier
    
    Returns:
        True si le graphe est connexe
        True si le graphe est vide (par convention mathématique)
        False si le graphe a plusieurs composantes connexes
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("C", "D")  # Deux composantes séparées
        >>> is_connected(g)
        False
        
        >>> g2 = Graph()  # Graphe vide
        >>> is_connected(g2)
        True  # Par convention (aucun nœud = connexe)
    
    Algorithme:
        1. Choisir un nœud de départ arbitraire
        2. Faire un parcours (DFS ou BFS) depuis ce nœud
        3. Vérifier si tous les nœuds ont été visités
    """
    nodes=(graph.nodes());nodes_dfs=set()
    if len(nodes)>0:
        for i in dfs(graph,nodes[0]):
            for d in dfs(graph,i):nodes_dfs.add(d)
        return set(nodes)==nodes_dfs
    return True


def reachable_from(graph: Graph, start: str) -> set[str]:
    """
    Retourne l'ensemble des nœuds atteignables depuis un nœud de départ.
    
    Args:
        graph: Le graphe à parcourir
        start: Nœud de départ
    
    Returns:
        Ensemble des nœuds atteignables (incluant start)
    
    Raises:
        ValueError: Si le nœud de départ n'existe pas
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("C", "D")
        >>> reachable_from(g, "A")
        {'A', 'B'}
    """
    return set(dfs(graph, start))


def shortest_path(graph: Graph, start: str, goal: str) -> list[str] | None:
    """
    Trouve le plus court chemin entre deux nœuds.
    
    Wrapper autour de bfs_path() pour plus de clarté sémantique.
    
    Args:
        graph: Le graphe à parcourir
        start: Nœud de départ
        goal: Nœud cible
    
    Returns:
        Liste des nœuds du plus court chemin
        None si aucun chemin n'existe
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("B", "C")
        >>> shortest_path(g, "A", "C")
        ['A', 'B', 'C']
    """
    # TODO: implémenter
    # Astuce : appeler bfs_path()
    return bfs_path(graph, start, goal)


# ============================================================================
# Fonctions utilitaires (optionnel, mais utile pour debug)
# ============================================================================

def path_length(path: list[str] | None) -> int:
    """
    Retourne la longueur d'un chemin (nombre d'arêtes).
    
    Args:
        path: Liste de nœuds ou None
    
    Returns:
        Nombre d'arêtes (len(path) - 1), ou -1 si path est None
    """
    if path is None:
        return -1
    return len(path) - 1