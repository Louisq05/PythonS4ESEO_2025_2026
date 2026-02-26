from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Affichage d'une Image")
        self.geometry("1024x608")

        # Conteneur principal
        container = Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PageAccueil, Page2):
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
        self.bg = PhotoImage(file="test tkinter\page_rumeur.png")

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
            text="M. Boubaker est en réalité marié\n à une serveillante de l’Eseo,  et ils\n ont des enfants ensemble dans\n le secret.",
            font=("Helvetica", 20),
            fill="black"
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

        self.bg = PhotoImage(file="test tkinter\page_rumeur.png")
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
        print("Bouton n°",index, ", nom :", self.noms[index])

        self.controller.personne_choisie = index
        self.controller.show_frame(PageAccueil)

if __name__ == "__main__":
    app = App()
    app.mainloop()