"""
Module ui.app
-------------
Fenêtre principale de l'application Tkinter.

Palier F - Séances 6-8.
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from ..core import Graph,save_graph,load_graph
from .interface import App,PageAccueil,Page2

class GraphExplorerApp:
    """
    Application principale avec interface Tkinter.
    
    Fonctionnalités:
    - Créer/charger un graphe
    - Visualiser le graphe
    - Lancer DFS/BFS avec animation
    - Sauvegarder le graphe
    """
    
    def __init__(self):
        """
        Initialise l'application.
        
        Args:
            root: Fenêtre racine Tkinter
        """

        """screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = int(screen_width * 0.8)
        height = int(screen_height * 0.8)

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")"""
        
        # Graphe actuel
        self.graph = Graph()
        
        # Configuration de l'interface
        #self._setup_ui()
        self.app = App()
        self.app.mainloop()
    
    def _setup_ui(self):
        """Configure tous les widgets de l'interface."""
        # TODO: implémenter l'interface
        # Suggestions de structure:
        # 1. Frame haut : boutons de contrôle
        # 2. Frame gauche : liste des nœuds
        # 3. Frame centre : Canvas pour dessiner le graphe
        # 4. Frame bas : zone de status/log
        
        # Exemple de structure de base:
        # top_frame = tk.Frame(self.root)
        # top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        # 
        # tk.Button(top_frame, text="Nouveau", command=self.new_graph).pack(side=tk.LEFT)
        # tk.Button(top_frame, text="Charger", command=self.load_graph).pack(side=tk.LEFT)
        # tk.Button(top_frame, text="Sauver", command=self.save_graph).pack(side=tk.LEFT)
        # ...


        """GRILLE PRINCIPALE"""
        self.root.grid_rowconfigure(1, weight=1)      # Ligne centrale extensible
        self.root.grid_columnconfigure(1, weight=1)   # Colonne centre extensible

        "FRAME HAUT"
        top_frame = tk.Frame(self.root, bg="#00ff00")
        top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Button(top_frame, text="Nouveau", command=self.new_graph).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(top_frame, text="Charger", command=self.load_graph).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(top_frame, text="Sauver", command=self.save_graph).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(top_frame, text="DFS", command=self.run_dfs).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(top_frame, text="BFS", command=self.run_bfs).pack(side=tk.LEFT, padx=5, pady=5)

        """FRAME GAUCHE"""
        left_frame = tk.Frame(self.root, bg="#2200ff", width=200)
        left_frame.grid(row=1, column=0, sticky="ns")

        tk.Label(left_frame, text="Nœuds du graphe").pack(pady=5)

        self.node_listbox = tk.Listbox(left_frame)
        self.node_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        """FRAME CENTRE"""
        center_frame = tk.Frame(self.root)
        center_frame.grid(row=1, column=1, sticky="nsew")

        self.canvas = tk.Canvas(center_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        """FRAME BAS"""
        bottom_frame = tk.Frame(self.root, bg="#ff0000", height=120)
        bottom_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        tk.Label(bottom_frame, text="Logs / Status").pack(anchor="w")

        self.log_text = tk.Text(bottom_frame, height=5)
        self.log_text.pack(fill=tk.X, padx=5, pady=5)

    
    def new_graph(self):
        """Crée un nouveau graphe vide."""
        self.graph=Graph()  #On réinitialise le graph pour en faire un nouveau
    
    def load_graph(self):
        """Charge un graphe depuis un fichier JSON."""
        chemin=filedialog.askopenfilename(
        defaultextension=".json",       #Defini le type du fichier à importer par défaut
        filetypes=[("Fichier JSON", "*.json")],
        title="Charger un Graph",
        )

        if chemin:
            try:
                self.graph=load_graph(chemin)   #Utilise la fonction load_graph de src\app\core\io.py pour charger
                messagebox.showinfo("Succès", "Fichier chargé avec succès !")   #Affiche la réussite du chargement d'un fichier
            except Exception as e:
                messagebox.showerror("Erreur", str(e))              #Affiche l'échec lors du chargement d'un fichier
    
    def save_graph(self):
        """Sauvegarde le graphe actuel en JSON."""
        chemin = filedialog.asksaveasfilename(
        defaultextension=".json",   #Defini le type du fichier par défaut
        filetypes=[("Fichier JSON", "*.json"),
                   ("Tous les fichiers", "*.*")], 
        title="Enregistrer le Graph "
        )

        if chemin:
            try:
                save_graph(self.graph, chemin)                              #Utilise la fonction savegraph de src\app\core\io.py pour enregistrer
                messagebox.showinfo("Succès", "Fichier enregistré avec succès !")       #Affiche la réussite de l'enregistrement
            except Exception as e:
                messagebox.showerror("Erreur", str(e))                      #Affiche l'échec lors de l'enregistrement
    
    def add_node(self):
        """Ajoute un nœud au graphe (via dialogue)."""
        node_name=self.entry_node.get() 
        if node_name and node_name.replace(" ","")!="":
            self.graph.add_node(node_name)
        self.entry_node.delete(0, tk.END)
    
    def add_edge(self):
        """Ajoute une arête au graphe (via dialogue)."""
        edge1_name = self.entry_edge1.get()
        edge2_name = self.entry_edge2.get()
        if edge1_name and edge1_name.replace(" ","")!="" and edge2_name and edge1_name.replace(" ","")!="":
            self.graph.add_edge(edge1_name,edge2_name)
            
        # On vide les deux champs
        self.entry_edge1.delete(0, tk.END)
        self.entry_edge2.delete(0, tk.END)
    
    def run_dfs(self):
        """Lance DFS et visualise le résultat."""
        # Astuce : appeler core.algorithms.dfs()
        # puis render.py pour visualiser
        start = simpledialog.askstring("DFS", "Noeud de départ :")

        if start not in self.graph.nodes:
            messagebox.showerror("Erreur", "Noeud Invalide")
            return 
        
        result = self.graph.dfs(start)

        self.log(f"DFS depuis {start} : {'->'.join(result)}")
    

    def run_bfs(self):
        """Lance BFS et visualise le résultat."""
        start = simpledialog.askstring("BFS", "Noeud de départ :")

        if start not in self.graph.nodes:
            messagebox.showerror("Erreur", "Noeud Invalide")
            return 
        
        result = self.graph.Bfs(start)

        self.log(f"BFS depuis {start} : {'->'.join(result)}")

    
    def clear_canvas(self):
        """Efface le canvas."""
        self.canvas.delete("all")
        self.log("Canvas effacé")
    
    def show_info(self):
        """Affiche des infos sur le graphe actuel."""
        # Exemple : nombre de nœuds, arêtes, connexité...
        nb_nodes = len(self.graph.nodes)
        nb_edges = len(self.graph.edges)

        infos = f""" Nombre de Noeuds : {nb_nodes}  , Nombre d'arrêtes : {nb_edges} """
        messagebox.showinfo("Info du graph", infos)


def main():
    """Point d'entrée de l'application."""
    app = GraphExplorerApp()


if __name__ == "__main__":
    main()
