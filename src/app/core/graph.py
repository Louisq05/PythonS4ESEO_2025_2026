"""
Module core.graph
-----------------
Implémentation d'un graphe non orienté basé sur une liste d'adjacence.

Ce module doit être TOTALEMENT indépendant de l'UI.
Tous les tests du palier A doivent passer avec ce fichier.
"""

from typing import Any


class Graph:
    """
    Représente un graphe non orienté.
    
    Structure de données : liste d'adjacence (dictionnaire)
    - Clé : nom du nœud (str)
    - Valeur : liste des voisins (list[str])
    
    Exemple d'usage:
        >>> g = Graph()
        >>> g.add_node("A")
        >>> g.add_node("B")
        >>> g.add_edge("A", "B")
        >>> g.neighbors("A")
        ['B']
    """
    
    def __init__(self):
        """Initialise un graphe vide."""
        self.graph=dict()

    def add_node(self, node: str) -> None:
        """
        Ajoute un nœud au graphe.
        
        Si le nœud existe déjà, ne fait rien (pas d'erreur).
        
        Args:
            node: Identifiant unique du nœud (chaîne de caractères)
        
        Raises:
            TypeError: Si node n'est pas une chaîne de caractères
        
        Exemple:
            >>> g = Graph()
            >>> g.add_node("Paris")
            >>> g.has_node("Paris")
            True
        """
        if type(node) != str :
            raise TypeError
        if  self.has_node(node) :
            return None
        else :
            self.graph[node] = []
        pass
    
    def add_edge(self, a: str, b: str) -> None:
        """
        Ajoute une arête non orientée entre deux nœuds.
        
        Si l'arête existe déjà, ne fait rien.
        Si l'un des nœuds n'existe pas, il est créé automatiquement.
        
        Args:
            a: Premier nœud
            b: Deuxième nœud
        
        Exemple:
            >>> g = Graph()
            >>> g.add_edge("Paris", "Lyon")
            >>> g.has_edge("Paris", "Lyon")
            True
            >>> g.has_edge("Lyon", "Paris")  # Non orienté !
            True
        """
        self.graph.setdefault(a, [])
        self.graph.setdefault(b, [])
        if a not in self.graph[b]:
            self.graph[b].append(a)
        if b not in self.graph[a]:
            self.graph[a].append(b)
    
    def remove_node(self, node: str) -> None:
        """
        Supprime un nœud et toutes ses arêtes associées.
        
        Args:
            node: Nœud à supprimer
        
        Raises:
            ValueError: Si le nœud n'existe pas
        """
        if self.has_node(node):
            del self.graph[node]
            for i in self.nodes():
                if self.has_edge(i,node):
                    self.graph[i].remove(node)
        else: 
            raise ValueError
        
    
    def remove_edge(self, a: str, b: str) -> None:
        """
        Supprime une arête entre deux nœuds.
        
        Args:
            a: Premier nœud
            b: Deuxième nœud
        
        Raises:
            ValueError: Si l'arête n'existe pas
        """
        self.graph[a].remove(b)
        self.graph[b].remove(a)
    
    def neighbors(self, node: str) -> list[str]:
        """
        Retourne la liste des voisins d'un nœud.
        
        Args:
            node: Nœud dont on veut les voisins
        
        Returns:
            Liste triée des nœuds voisins (ordre alphabétique)
        
        Raises:
            ValueError: Si le nœud n'existe pas
        
        Note:
            ⚠️ CRITIQUE : Cette méthode DOIT retourner une liste TRIÉE !
            Les algorithmes DFS et BFS en dépendent pour être déterministes.
            Les tests vérifieront explicitement cet ordre alphabétique.
        
        Exemple:
            >>> g = Graph()
            >>> g.add_edge("A", "Z")
            >>> g.add_edge("A", "B")
            >>> g.add_edge("A", "M")
            >>> g.neighbors("A")
            ['B', 'M', 'Z']  # Toujours en ordre alphabétique
        """
        if node not in self.graph :
            raise ValueError
        return sorted(self.graph[node])
    
    def has_node(self, node: str) -> bool:
        """Vérifie si un nœud existe dans le graphe."""
        try:
            self.graph[node]
            return True
        except:
            return False

    
    def has_edge(self, a: str, b: str) -> bool:
        """Vérifie si une arête existe entre deux nœuds."""
        return ((a,b) in self.edges() or (b,a) in self.edges())
    
    def nodes(self) -> list[str]:
        """
        Retourne la liste de tous les nœuds du graphe.
        
        Returns:
            Liste triée des nœuds (ordre alphabétique)
        """
        return list(self.graph.keys())
    
    def edges(self) -> list[tuple[str, str]]:
        """
        Retourne la liste de toutes les arêtes du graphe.
        
        Returns:
            Liste de tuples (a, b) où a < b (ordre alphabétique)
            Chaque arête n'apparaît qu'une seule fois.
        
        Exemple:
            >>> g = Graph()
            >>> g.add_edge("B", "A")
            >>> g.edges()
            [('A', 'B')]  # Ordre normalisé
        """
        edges_list=[]
        for k in self.graph.keys():
            for i in self.graph[k]:
                if (f"{i}",f"{k}") not in edges_list:
                    edges_list.append((f"{k}",f"{i}"))
        return edges_list
    
    def __len__(self) -> int:
        """Retourne le nombre de nœuds dans le graphe."""
        return len(self.graph)
    
    def __repr__(self) -> str:
        """Représentation lisible du graphe pour debug."""
        return f"Graph(nodes={len(self)}, edges={len(self.edges())})"
