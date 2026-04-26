from tkinter import *
from tkinter import ttk
from random import choice, randint
import os
from ..core import Graph,save_graph,load_graph,is_connected,dfs,dfs_path,bfs,bfs_path
from tkinter import messagebox,filedialog

# Détection de l'OS
if os.name == "nt":   # Windows
    IMAGE_PATH = "src\\app\\ui\\"
else:                 # Mac / Linux
    IMAGE_PATH = "src/app/ui/"

button = None

rumeurs = [{"M. Boubaker est en réalité marié à une surveillante de l’Eseo, et il ont des enfants ensemble dans le secret.":"M. Boubaker"},
{"Arthur déteste en secret son pote Victor, il n’a dieu que pour Tomy.":"Victor Bon"}, 
{"Chaque soir sont organisé des soirées par M. Vallee dans le sous-sol de l’Eseo.":"M. Vallee"}, 
{"M. Trenchant prépare un contrôle surprise en physique quantique.":"M. Trenchant"}, 
{"Loan à gagné à l’euro millon et prévoit de racheter le batiment de l’Eseo.":"Loan Bouyahi"}, 
{"M. Schlinquer imprime des armes en 3d dans le lab de l’eseo.":"M. Schlinquer"},{"Nils s’appelle en réalité Nelson.":"Nils Coudry"}, 
{"Tristan s’appelle en réalité Kristian.":"Tristan Bernard"},{"Nils entretient une relation avec une caintinière du RU.":"Nils Coudry"}, 
{"Chloe Jarousseau est encore sous l’emprise d’un illusionniste qui l’a hypnotisé en 2022.":"Chloe Jarousseau"}, 
{"Le batiment de l’Eseo Dijon est construit sur un site paranormal et M. Trenchant analyse les ondes.":"M. Trenchant"},
{"M. Vallee passe les vacances d’été sur un yatch financé par l’eseo.":"M. Vallee"},
{"Louis est sur le point de quitter ESEO pour accepter un CDI chez Atol CD à 42M/an":"Louis Quibeuf"}]

concernés_lst = ["M. Boubaker", "Victor", "M. Vallee", "M. Trenchant", "Loan", "M. Schlinquer", "Nils", "Tristan", "Nils", "Chloe Jarousseau", "M. Trenchant", "M. Vallee" ]
concernés_dict={"M. Boubaker":{"name":"M. Boubaker","x":0.5,"y":0.475},
                "Louberssac Emilie":{"name":"Louberssac Emilie","x":0.4,"y":0.75},
                "Hoerner Isabelle":{"name":"Hoerner Isabelle","x":0.46,"y":0.475},
                "Kempnich Arthur":{"name":"Kempnich Arthur","x":0.5,"y":0.56},
                "M. Trenchant":{"name":"M. Trenchant","x":0.35,"y":0.6},
                "Matteo Aillet":{"name":"Matteo Aillet","x":0.35,"y":0.75},
                "Chloe Jarousseau":{"name":"Chloe Jarousseau","x":0.35,"y":0.475},
                "M. Vallee":{"name":"M. Vallee","x":0.375,"y":0.475},
                "Nicol Matheo":{"name":"Nicol Matheo","x":0.93,"y":0.85},
                "Mary Yanis":{"name":"Mary Yanis","x":0.675,"y":0.75},
                "Victor Bon":{"name":"Victor Bon","x":0.64,"y":0.6},
                "Loan Bouyahi":{"name":"Loan Bouyahi","x":0.67,"y":0.6},
                "M. Schlinquer":{"name":"M. Schlinquer","x":0.6,"y":0.8},
                "Nils Coudry":{"name":"Nils Coudry","x":0.7,"y":0.6},
                "Tristan Bernard":{"name":"Tristan Bernard","x":0.9,"y":0.98},
                "Louis Quibeuf":{"name":"Louis Quibeuf","x":0.08,"y":0.7}
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
        super().__init__(parent)

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Référence image de fond
        self.bg = PhotoImage(file=IMAGE_PATH + "page1.png", master=self.canvas)

        # Image de fond
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # Texte : titre "Rumeur :"
        self.canvas.create_text(
            512, 200,
            text="Rumeur :",
            font=("OCR A Extended", 30, "bold"),
            fill="black"
        )
        global rumeurs_text
        global rumeurs_concernés
        for k,v in choice(rumeurs).items():
            rumeurs_text=k
            rumeurs_concernés=v
            print("Rumeur choisie : ", rumeurs_text, "\nConcerné : ", rumeurs_concernés)  
        if len(rumeurs_text) > 30:
            lines = []
            nb_lignes = len(rumeurs_text) // 30 + 1

            for i in range(nb_lignes):
                lines.append(rumeurs_text[30*i:30*(i+1)])

            rumeurs_text_formated = "\n".join(lines)
        else:
            rumeurs_text_formated = rumeurs_text

        # Texte : titre "Rumeur :"
        self.canvas.create_text(
            512, 300,
            text=rumeurs_text_formated,
            font=("OCR A Extended", 15),
            fill="black",
            justify="center",
            width=625
        )

        # Boutons

        # Zone cliquable invisible pour "Suivant"
        LARGEUR = 200   # augmente ici (x2-x3)
        HAUTEUR = 80

        x = int(0.5 * 1024)
        y = int(0.875 * 608)

        zone_suivant = self.canvas.create_rectangle(
            x - LARGEUR // 2, y - HAUTEUR // 2,
            x + LARGEUR // 2, y + HAUTEUR // 2,
            fill="",
            outline="",
            tags="btn_suivant"
        )

        self.canvas.tag_bind(
            zone_suivant,
            "<Button-1>",
            lambda e: controller.show_frame(Page2)
        ) 
# Zone cliquable invisible pour "Quit" 
        LARGEUR = 100
        HAUTEUR = 40 
        x = int(0.95 * 1024) 
        y = int(0.05 * 608) 
        zone_quit = self.canvas.create_rectangle(
            x - LARGEUR // 2, y - HAUTEUR // 2, 
            x + LARGEUR // 2, y + HAUTEUR // 2, 
            fill="", 
            outline="", 
            tags="btn_quit" ) 
        self.canvas.tag_bind( 
            zone_quit, 
            "<Button-1>", 
            lambda e: controller.destroy() 
)


class Page2(Frame):
    # Liste des noms
    noms = [
        "M. Boubaker", "Louberssac Emilie",
        "Hoerner Isabelle", "Kempnich Arthur",
        "M. Trenchant", "Matteo Aillet",
        "Chloe Jarousseau", "M. Vallee",
        "Nicol Matheo", "Mary Yanis"
    ]
    clavier = [
            [0.42, 0.67], [0.5, 0.69], [0.58, 0.67],
            [0.42, 0.74], [0.5, 0.76], [0.58, 0.74],
            [0.42, 0.81], [0.5, 0.83], [0.58, 0.81],
            [0.5,  0.90]
        ]

    annuaire_data = {
    "M. Boubaker": 0,
    "Louberssac Emilie": 1,
    "Hoerner Isabelle": 2,
    "Kempnich Arthur": 3,
    "M. Trenchant": 4,
    "Matteo Aillet": 5,
    "Chloe Jarousseau": 6,
    "M. Vallee": 7,
    "Nicol Matheo": 8,
    "Mary Yanis": 9
}
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg = PhotoImage(file=IMAGE_PATH + "page2.png", master=self.canvas)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.canvas.create_text(
            512, 225,
            text="A qui voulez-\nvous en parler ?",
            font=("OCR A Extended", 11, "bold"),
            fill="black",
            justify="center"
        )
        start_y = 150        # Y coordinate for the first line
        line_spacing = 35    # Vertical space between each line
        x_name_col = 725     # X coordinate for the names column (left-aligned)
        x_num_col = 950      # X coordinate for the numbers column (right-aligned)

        for index, (name, number) in enumerate(self.annuaire_data.items()):
            current_y = start_y + (index * line_spacing)
            self.canvas.create_text(
                x_name_col, current_y,
                text=f"{name} :",
                font=("Lucida Handwriting", 12, "bold"),
                fill="black",
                anchor="w" 
            )
            self.canvas.create_text(
            x_num_col, current_y,
            text=str(number),
            font=("Lucida Handwriting", 15, "bold"),
            fill="black",
            anchor="e" 
            )

        # Zone cliquable invisible pour "Quit" 
        LARGEUR = 100
        HAUTEUR = 40 
        x = int(0.5 * 1024) 
        y = int(0.545 * 608) 
        zone_quit = self.canvas.create_rectangle(
            x - LARGEUR // 2, y - HAUTEUR // 2, 
            x + LARGEUR // 2, y + HAUTEUR // 2, 
            fill="", 
            outline="", 
            tags="btn_quit" ) 
        self.canvas.tag_bind( 
            zone_quit, 
            "<Button-1>", 
            lambda e: controller.destroy() 
)
        
        # Zones cliquables invisibles calées sur les touches de l'image
        LARGEUR = 60   
        HAUTEUR = 35

        for i in range(len(self.clavier)):
            index = i + 1 if i < 9 else 0

            x = int(self.clavier[i][0] * 1024)
            y = int(self.clavier[i][1] * 608)

            zone = self.canvas.create_rectangle(
                x - LARGEUR // 2, y - HAUTEUR // 2,
                x + LARGEUR // 2, y + HAUTEUR // 2,
                fill="",        # transparent
                outline="",     # pas de bordure visible
                tags=f"btn_{index}"
            )
            self.canvas.tag_bind(
                zone, "<Button-1>",
                lambda e, idx=index: self.choisir_personne(idx)
            )


    def choisir_personne(self, index):
        print("Point de départ :", self.noms[index])
        self.controller.show_frame(Page3)
        global bouton
        bouton = self.noms[index]

class Page3(Frame):
    
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg = PhotoImage(file=IMAGE_PATH + "page3.png", master=self.canvas)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # DFS
        self.btn_dfs = ttk.Button(self, text="Je t'en parle, mais ne le dis à personne (DFS)",
                    command=lambda: self.on_dfs_click())
        self.btn_dfs.place(relx=0.2, rely=0.15, anchor="center")

        # BFS
        self.btn_bfs = ttk.Button(self, text="Tu as entendu la nouvelle ? (BFS)",
                    command=lambda: self.on_bfs_click())
        self.btn_bfs.place(relx=0.2, rely=0.2, anchor="center")

        # Quitter
        # Zone cliquable invisible pour "Quit" 
        LARGEUR = 100
        HAUTEUR = 40 
        x = int(0.95 * 1024) 
        y = int(0.05 * 608) 
        zone_quit = self.canvas.create_rectangle(
            x - LARGEUR // 2, y - HAUTEUR // 2, 
            x + LARGEUR // 2, y + HAUTEUR // 2, 
            fill="", 
            outline="", 
            tags="btn_quit" ) 
        self.canvas.tag_bind( 
            zone_quit, 
            "<Button-1>", 
            lambda e: controller.destroy() 
)
        
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
        for k,v in self.concernés.items():
            self.concernés[k]["circle_id"],self.concernés[k]["text_id"]=self._add_circle(relx=v["x"],rely=v["y"])
        # Bind hover events to the circle using the specific name
            self.canvas.tag_bind(self.concernés[k]["circle_id"], "<Enter>", lambda event, n=v["name"]: self.on_enter(event, n))
            self.canvas.tag_bind(self.concernés[k]["circle_id"], "<Leave>", self.on_leave)
            self.canvas.tag_bind(self.concernés[k]["text_id"], "<Enter>", lambda event, n=v["name"]: self.on_enter(event, n))
            self.canvas.tag_bind(self.concernés[k]["text_id"], "<Leave>", self.on_leave)
    
    def on_enter(self, event, name):
        # Display the name when hovering over the oval
        self.canvas.create_text(event.x + 25, event.y - 15, text=name,
                                fill="red", font=("Arial", 12, "bold"),
                                tags="tooltip")

    def on_leave(self, event):
        # Remove the tooltip
        self.canvas.delete("tooltip")
    
    def show_circle(self,circle_id,text_id):
        self.canvas.itemconfigure(circle_id, state="normal")
        self.canvas.itemconfigure(text_id, state="normal")

    def hide_circle(self,circle_id,text_id):
        self.canvas.itemconfigure(circle_id, state="hidden")
        self.canvas.itemconfigure(text_id, state="hidden")

    def run_dfs(self):
        print("DFS choisi")
        self.show_circle(self.concernés[bouton]["circle_id"], self.concernés[bouton]["text_id"])
        print(bouton)
        result_path = dfs_path(self.graph, bouton, rumeurs_concernés)
        print("result path :", result_path)

        delay = 500
        for i in range(1, len(result_path)):
            from_node = result_path[i - 1]
            to_node = result_path[i]
            self.after(delay, lambda f=from_node, t=to_node: self._bfs_step(f, t))
            delay += 500

    def run_bfs(self):
        print("BFS choisi")
        self.show_circle(self.concernés[bouton]["circle_id"], self.concernés[bouton]["text_id"])
        result_path = bfs_path(self.graph, bouton, rumeurs_concernés)
        print("result path :", result_path)

        delay = 500
        for k, v in result_path.items():
            for link in v["Au courant"]:
                from_node, to_node = link[0], link[1]
                self.after(delay, lambda f=from_node, t=to_node: self._bfs_step(f, t))
                delay += 500

    def _bfs_step(self, from_node, to_node):
        """Affiche une étape BFS : flèche + cercle + message."""
        self.draw_arrow(from_node, to_node)
        self.show_circle(
            self.concernés[to_node]["circle_id"],
            self.concernés[to_node]["text_id"]
        )
        self.show_message(from_node, to_node)

    def on_dfs_click(self):
        self.btn_dfs.place_forget()
        self.btn_bfs.place_forget()
        self.run_dfs()

    def on_bfs_click(self):
        self.btn_dfs.place_forget()
        self.btn_bfs.place_forget()
        self.run_bfs()
    
    def init_graph(self):
        chemin=IMAGE_PATH+f"graph{str(randint(1,5))}.json"
        if chemin:
            try:
                self.graph=load_graph(chemin)   #Utilise la fonction load_graph de src\app\core\io.py pour charger
                #messagebox.showinfo("Succès", "Fichier chargé avec succès !")   #Affiche la réussite du chargement d'un fichier
            except Exception as e:
                messagebox.showerror("Erreur", str(e))              #Affiche l'échec lors du chargement d'un fichier
        print("Graph choisi : ", chemin)
    
    def show_circle_delay(self, prev_node, current_node):
        if prev_node is not None:
            self.draw_arrow(prev_node, current_node)
            self.show_message(prev_node, current_node)

        self.show_circle(self.concernés[current_node]["circle_id"],self.concernés[current_node]["text_id"])

        # if remaining_path:
        #     next_node = remaining_path[0]
        #     remain = remaining_path[1:]
        #     self.after(randint(500, 1500), lambda: self.show_circle_delay(current_node, next_node, remain))

    def show_message(self, from_node, to_node):
        if from_node==to_node:
            message=f"Vous en avez parlé à la personne concerné"
        elif to_node==rumeurs_concernés:
            message=f"{from_node} a appris à {"\n" if len(from_node)+len(to_node)>15 else ""}{to_node} la rumeur le concernant"
        else:
            message = f"{from_node} en a parlé à {to_node}"
        if not hasattr(self, "message_id"):
            self.message_id = self.canvas.create_text(220, 100, text=message, font=("Helvetica", 10, "bold"), fill="#07FB28")
        else:
            self.canvas.itemconfig(self.message_id, text=message)
    
    def draw_arrow(self, from_node, to_node):
        c_coords = self.canvas.coords(self.concernés[from_node]["circle_id"])
        n_coords = self.canvas.coords(self.concernés[to_node]["circle_id"])

        x1 = (c_coords[0] + c_coords[2]) / 2
        y1 = (c_coords[1] + c_coords[3]) / 2
        x2 = (n_coords[0] + n_coords[2]) / 2
        y2 = (n_coords[1] + n_coords[3]) / 2

        # supprimer l’ancienne flèche si elle existe
        if hasattr(self, "arrow_id"):
            self.canvas.delete(self.arrow_id)

        # créer la flèche
        self.arrow_id = self.canvas.create_line(
            x1, y1, x2, y2,
            arrow="last",
            width=5,
            arrowshape=(20, 25, 10),
            fill="#E72A2A"
        )
        
if __name__ == "__main__":
    app = App()
    app.mainloop()