# -----------------------------------------------
# |                  Auteur                     |
# -----------------------------------------------
# Auteur: Anicet Cyrille KAMBOU alias Mr_KAM
# Date de création: 21/02/2024
# Description: Un package python pour la creation de site web et de d'applications de datasciences

# -----------------------------------------------
# |           Description du Projet             |
# -----------------------------------------------
"""Documentation

"""

# -----------------------------------------------
# |      Importation de Modules/ Packages       |
# -----------------------------------------------
import streamlit as st
import streamlit.components.v1 as components
from st_bridge import bridge, html
import os

# from rich import print

# -----------------------------------------------
# |          Initialisation Config              |
# -----------------------------------------------
# [Initialisation des paramètres, configuration
# de l'environnement, etc.]


# -----------------------------------------------
# |           Définitions des Fonctions         |
# -----------------------------------------------
def dependencies(chemin, type_contenu):
    print(chemin)
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
        if type_contenu.lower() == "css":
            return f"<style>{contenu}</style>"
        elif type_contenu.lower() == "js":
            return f"<script>{contenu}</script>"
        else:
            print(
                "Type de contenu non pris en charge. Veuillez spécifier 'css' ou 'js'."
            )
            return None
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None


def daisy():
    """
    Cette fonction permet d'initialiser les dependance css et js de daisy ui
    et tailwinds css
    """
    package_directory = os.path.dirname(__file__)
    link_source = (
        dependencies(os.path.join(package_directory, "css/daysiui.css"), "css")
        + "\n"
        + dependencies(os.path.join(package_directory, "css/tailwind.css"), "css")
        + "\n"
        + dependencies(os.path.join(package_directory, "css/tailwindcss.js"), "js")
    )

    return link_source


# -----------------------------------------------
# |             Définitions des Classes         |
# -----------------------------------------------
class ui:
    """Documentation de la classe MaClasse."""

    def __init__(self, parametre):
        """Initialisation de la classe MaClasse."""
        self.parametre = parametre

    def theme(self, index=0):
        themes = [
            "light",
            "dark",
            "cupcake",
            "bumblebee",
            "emerald",
            "corporate",
            "synthwave",
            "retro",
            "cyberpunk",
            "valentine",
            "halloween",
            "garden",
            "forest",
            "aqua",
            "lofi",
            "pastel",
            "fantasy",
            "wireframe",
            "black",
            "luxury",
            "dracula",
            "cmyk",
            "autumn",
            "business",
            "acid",
            "lemonade",
            "night",
            "coffee",
            "winter",
            "dim",
            "nord",
            "sunset",
        ]
        select_theme = themes[index]

    def methode(self):
        """Documentation de la méthode."""
        # Corps de la méthode
        pass


# -----------------------------------------------
# |               Corps du Programme             |
# -----------------------------------------------
# [Corps principal du programme, logique principale,
# appels de fonctions, etc.]

# -----------------------------------------------
# |                 Demo if Main                |
# -----------------------------------------------
if __name__ == "__main__":
    # [Code de démonstration, exemple d'utilisation
    # de fonctions/classes, tests, etc.]
    pass
