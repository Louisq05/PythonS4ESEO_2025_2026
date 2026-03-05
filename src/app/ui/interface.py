from tkinter import *
from tkinter import ttk
from random import choice

rumeurs = ["M. Boubaker est en réalité marié à une surveillante de l’Eseo, et il ont des enfants ensemble dans le secret.",
"Arthur déteste en secret son pote Victor, il n’a dieu que pour Tomy.", 
"Chaque soir sont organisé des soirées par M. Valée dans le sous-sol de l’Eseo.", 
"M. Trenchant prépare un contrôle surprise en physique quantique.", 
"Loan à gagné à l’euro millon et prévoit de racheter le batiment de l’Eseo.", 
"M. Schlinquer imprime des armes en 3d dans le lab de l’eseo.”, “Nils s’appelle en réalité Nelson.", 
"Tristant s’appelle en réalité Kristian.","Nils entretient une relation avec une caintinière du RU.", 
"Chloé Jarrousseau est encore sous l’emprise d’un illusionniste qui l’a hypnotisé en 2022.", 
"Le batiment de l’Eseo Dijon est construit sur un site paranormal et M. Trenchant analyse les ondes.",
"Cyril Vallée passe les vacances d’été sur un yatch financé par l’eseo."]

concernés = ["M. Boubaker", "Victor", "M. Valée", "M. Trenchant", "Loan", "M. Schlinquer", "Nils", "Tristan", "Nils", "Chloé Jarousseau", "M. Trenchant", "Cyril Valée" ]

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

        for F in (PageAccueil, Page2, Page3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageAccueil)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class PageAccueil(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Référence image de fond
        self.bg = PhotoImage(file="src\\app\\ui\\page_rumeur.png", master=self.canvas)

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
    noms = [
        "M. Boubaker", "Loubersac Emilie",
        "Hoerner Isabelle", "Kempnich Arthur",
        "Trenchant Vincent", "Matteo Aillet",
        "Gechi Justin", "Vallée Cyril",
        "Nicol Matheo", "Mary Yanis"
    ]
    
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg = PhotoImage(file="src\\app\\ui\\page_rumeur.png", master=self.canvas)
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
                   command=lambda: controller.show_frame(PageAccueil))\
            .place(relx=0.5, rely=0.9, anchor="center")

        # Quitter
        ttk.Button(self, text="Quit",
                   command=controller.destroy)\
            .place(relx=0.95, rely=0.05, anchor="center")

    def choisir_personne(self, index):
        print("Bouton choisi :", self.noms[index])
        self.controller.personne_choisie = index
        self.controller.show_frame(Page3)

class Page3(Frame):
    
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller

        self.canvas = Canvas(self, width=1024, height=608, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg = PhotoImage(file="src\\app\\ui\\batiment Eseo 1.png", master=self.canvas)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # Bouton retour
        ttk.Button(self, text="Aller à la page 1",
                   command=lambda: controller.show_frame(PageAccueil))\
            .place(relx=0.5, rely=0.9, anchor="center")

        # Quitter
        ttk.Button(self, text="Quit",
                   command=controller.destroy)\
            .place(relx=0.95, rely=0.05, anchor="center")

        # Cercle
        self._add_circle(relx=0.5, rely=0.5, radius=10, color="#E74C3C", text="!")

    # Fonction pour créer un cercle 
    def _add_circle(self, relx=0.5, rely=0.5, radius=35, color="#E74C3C", outline="#ffffff", text="", text_color="white"): # Choisir les couleurs
        """Dessine un cercle sur le canvas principal."""

        x = int(relx * 1024)
        y = int(rely * 608)

        self.canvas.create_oval(x - radius, y - radius,
                                x + radius, y + radius,
                                fill=color, outline=outline, width=2)   # Choisir l'épaisseur du contour
        
        if text:
            self.canvas.create_text(x, y, text=text,
                                    fill=text_color,
                                    font=("Arial", 12, "bold"))         # Choix du text

if __name__ == "__main__":
    app = App()
    app.mainloop()