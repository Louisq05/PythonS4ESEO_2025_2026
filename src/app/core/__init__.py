"""
Package core
------------
Cœur algorithmique du projet (100% testable, indépendant de l'UI).
"""

from .graph import Graph
from .algorithms import (
    dfs,
    dfs_path,
    bfs,
    bfs_path,
    bfs_path_to_project,
    is_connected,
    reachable_from,
    shortest_path,
)
from .io import save_graph, load_graph, graph_to_dict, dict_to_graph

__all__ = [
    "Graph",
    "dfs",
    "dfs_path",
    "bfs",
    "bfs_path",
    "is_connected",
    "reachable_from",
    "shortest_path",
    "save_graph",
    "load_graph",
    "graph_to_dict",
    "dict_to_graph",
]
