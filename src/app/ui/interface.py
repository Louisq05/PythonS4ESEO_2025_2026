from tkinter import *
from tkinter import ttk
from random import choice
import os
from ..core import Graph,save_graph,load_graph,is_connected
from tkinter import messagebox,filedialog

# Détection de l'OS
if os.name == "nt":   # Windows
    IMAGE_PATH = "src\\app\\ui\\"
else:                 # Mac / Linux
    IMAGE_PATH = "src/app/ui/"

rumeurs = ["M. Boubaker est en réalité marié à une surveillante de l’Eseo, et il ont des enfants ensemble dans le secret.",
"Arthur déteste en secret son pote Victor, il n’a dieu que pour Tomy.", 
"Chaque soir sont organisé des soirées par M. Valée dans le sous-sol de l’Eseo.", 
"M. Trenchant prépare un contrôle surprise en physique quantique.", 
"Loan à gagné à l’euro millon et prévoit de racheter le batiment de l’Eseo.", 
"M. Schlinquer imprime des armes en 3d dans le lab de l’eseo.”, “Nils s’appelle en réalité Nelson.", 
"Tristant s’appelle en réalité Kristian.","Nils entretient une relation avec une caintinière du RU.", 
"Chloé Jarrousseau est encore sous l’emprise d’un illusionniste qui l’a hypnotisé en 2022.", 
"Le batiment de l’Eseo Dijon est construit sur un site paranormal et M. Trenchant analyse les ondes.",
"M. Vallée passe les vacances d’été sur un yatch financé par l’eseo.",
"Louis est sur le point de quitter ESEO pour accepter un CDI chez Atol CD à 42M/an"]

concernés_lst = ["M. Boubaker", "Victor", "M. Valée", "M. Trenchant", "Loan", "M. Schlinquer", "Nils", "Tristan", "Nils", "Chloé Jarousseau", "M. Trenchant", "Cyril Valée" ]
concernés_dict={"M. Boubaker":{"name":"M. Boubaker","x":0.5,"y":0.475},
                "Louberssac Emilie":{"name":"Louberssac Emilie","x":0.4,"y":0.75},
                "Hoerner Isabelle":{"name":"Hoerner Isabelle","x":0.46,"y":0.475},
                "Kempnich Arthur":{"name":"Kempnich Arthur","x":0.5,"y":0.56},
                "M. Trenchant":{"name":"M. Trenchant","x":0.35,"y":0.6},
                "Matteo Aillet":{"name":"Matteo Aillet","x":0.35,"y":0.75},
                "Chloé Jarousseau":{"name":"Chloé Jarousseau","x":0.35,"y":0.475},
                "M. Valée":{"name":"M. Valée","x":0.375,"y":0.475},
                "Nicol Matheo":{"name":"Nicol Matheo","x":0.98,"y":0.85},
                "Mary Yanis":{"name":"Mary Yanis","x":0.675,"y":0.75},
                "Victor Bon":{"name":"Victor Bon","x":0.7,"y":0.6},
                "Loan Bouyahi":{"name":"Loan Bouyahi","x":0.7,"y":0.6},
                "M. Schlinquer":{"name":"M. Schlinquer","x":0.6,"y":0.8},
                "Nils Coudry":{"name":"Nils Coudry","x":0.7,"y":0.6},
                "Tristan Bernard":{"name":"Tristan Bernard","x":0.9,"y":0.98}
                }                

bouton = None

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Explorateur de Graphes - ESEO S4")
        self.geometry("1024x608")

        # Conteneur principal
        container = Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Page1, Page2, Page3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page1)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class Page1(Frame):
    def __init__(self, parent, controller):
        print("page1")
        super().__init__(parent)

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Référence image de fond
        self.bg = PhotoImage(file=IMAGE_PATH + "page_rumeur.png", master=self.canvas)

        # Image de fond
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # Texte : titre "Rumeur :"
        self.canvas.create_text(
            512, 100,
            text="Rumeur :",
            font=("Helvetica", 30, "bold"),
            fill="black"
        )
        # Texte : titre "Rumeur :"
        self.canvas.create_text(
            512, 300,
            text=choice(rumeurs),
            font=("Helvetica", 20),
            fill="black",
            justify="center",
            width=625
        )

        # Boutons

        # Changer de page
        ttk.Button(self, text="Suivant",
                   command=lambda: controller.show_frame(Page2))\
            .place(relx=0.5, rely=0.9, anchor="center")


        # Quitter
        ttk.Button(self, text="Quit",
                   command=controller.destroy)\
            .place(relx=0.95, rely=0.05, anchor="center")


class Page2(Frame):
    # Liste des noms
    print("page2")
    noms = [
        "M. Boubaker", "Louberssac Emilie",
        "Hoerner Isabelle", "Kempnich Arthur",
        "M. Trenchant", "Matteo Aillet",
        "Chloé Jarousseau", "M. Valée",
        "Nicol Matheo", "Mary Yanis"
    ]
    
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg = PhotoImage(file=IMAGE_PATH + "page_rumeur.png", master=self.canvas)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.canvas.create_text(
            512, 100,
            text="A qui voulez-vous en parler ?",
            font=("Helvetica", 30, "bold"),
            fill="black"
        )

        # Frame pour la grille
        grid_frame = Frame(self)
        self.canvas.create_window(512, 320, window=grid_frame)

        # Création 5 lignes x 2 colonnes
        for row in range(5):
            for col in range(2):
                index = row * 2 + col

                btn = ttk.Button(
                    grid_frame,
                    text=self.noms[index],
                    command=lambda i=index: self.choisir_personne(i),
                    width=30
                )
                btn.grid(row=row, column=col, padx=10, pady=10)

        # Bouton retour
        ttk.Button(self, text="Aller à la page 1",
                   command=lambda: controller.show_frame(Page1))\
            .place(relx=0.5, rely=0.9, anchor="center")

        # Quitter
        ttk.Button(self, text="Quit",
                   command=controller.destroy)\
            .place(relx=0.95, rely=0.05, anchor="center")


    def choisir_personne(self, index):
        print("Bouton choisi :", self.noms[index])
        self.controller.show_frame(Page3)
        global bouton
        bouton = self.noms[index]

class Page3(Frame):
    
    def __init__(self, parent, controller):
        print("page3")

        super().__init__(parent)
        self.controller = controller

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg = PhotoImage(file=IMAGE_PATH + "batiment Eseo 1.png", master=self.canvas)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # DFS
        self.btn_dfs = ttk.Button(self, text="DFS",
                    command=lambda: self.on_dfs_click())
        self.btn_dfs.place(relx=0.55, rely=0.9, anchor="center")

        # BFS
        self.btn_bfs = ttk.Button(self, text="BFS",
                    command=lambda: self.on_bfs_click())
        self.btn_bfs.place(relx=0.45, rely=0.9, anchor="center")

        # Quitter
        ttk.Button(self, text="Quit",
                   command=controller.destroy)\
            .place(relx=0.95, rely=0.05, anchor="center")
        
        self.concernés=concernés_dict
        self.init_graph()
        self._create_circle()

    # Fonction pour créer un cercle 
    def _add_circle(self, relx=0.5, rely=0.5, radius=10, color="#E74C3C", outline="#ffffff", text="!", text_color="white"): # Choisir les couleurs
        """Dessine un cercle sur le canvas principal."""

        x = int(relx * 1024)
        y = int(rely * 608)

        circle_id=self.canvas.create_oval(x - radius, y - radius,
                                x + radius, y + radius,
                                fill=color, outline=outline, width=2, state="hidden")   # Choisir l'épaisseur du contour
        
        if text:
            text_id=self.canvas.create_text(x, y, text=text,
                                    fill=text_color,
                                    font=("Arial", 12, "bold"), state="hidden")         # Choix du text
            return circle_id,text_id
    def _create_circle(self):
        print("Création des cercles : ")
        for k,v in self.concernés.items():
            self.concernés[k]["circle_id"],self.concernés[k]["text_id"]=self._add_circle(relx=v["x"],rely=v["y"])
            
    
    def show_circle(self,circle_id,text_id):
        self.canvas.itemconfigure(circle_id, state="normal")
        self.canvas.itemconfigure(text_id, state="normal")

    def hide_circle(self,circle_id,text_id):
        self.canvas.itemconfigure(circle_id, state="hidden")
        self.canvas.itemconfigure(text_id, state="hidden")

    def run_dfs(self):
        self.show_circle(self.concernés[bouton]["circle_id"],self.concernés[bouton]["text_id"])

    def run_bfs(self):
        self.show_circle(self.concernés[bouton]["circle_id"],self.concernés[bouton]["text_id"])

    def on_dfs_click(self):
        self.btn_dfs.place_forget()
        self.btn_bfs.place_forget()
        self.run_dfs()

    def on_bfs_click(self):
        self.btn_dfs.place_forget()
        self.btn_bfs.place_forget()
        self.run_bfs()
    
    def init_graph(self):
        chemin=IMAGE_PATH+"graph.json"
        if chemin:
            try:
                self.graph=load_graph(chemin)   #Utilise la fonction load_graph de src\app\core\io.py pour charger
                messagebox.showinfo("Succès", "Fichier chargé avec succès !")   #Affiche la réussite du chargement d'un fichier
            except Exception as e:
                messagebox.showerror("Erreur", str(e))              #Affiche l'échec lors du chargement d'un fichier
        print(self.graph.edges())
        
if __name__ == "__main__":
    app = App()
    app.mainloop()

    """
    Idée pour la suite :
    créer les boutons DFS BFS qui apparaitront au debut de page3
    attendre qu'on clique pour déclencher l'apparition du premier cercle"""