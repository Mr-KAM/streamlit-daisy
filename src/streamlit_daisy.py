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

from rich import print

# -----------------------------------------------
# |          Initialisation Config              |
# -----------------------------------------------
# [Initialisation des paramètres, configuration
# de l'environnement, etc.]


# -----------------------------------------------
# |           Définitions des Fonctions         |
# -----------------------------------------------
def dependencies(chemin, type_contenu):
    # print(chemin)
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
    
def sidebar_color(color):
    st.markdown(
        f"""
        <style>
        section[data-testid=“stSidebar”] div[class=“css-17eq0hr e1fqkh3o1”] .sidebar .sidebar-content {{
            background-color: {color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def st_theme(index=0):
    themes = [
        "#FFFFFF",
        "#1D232A",
        "#FAF7F5",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#1A103D",
        "#ECE3CA",
        "#FFF349",
        "#FAE7F4",
        "#212121",
        "#E9E7E7",
        "#181212",
        "#355DA7",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#000000",
        "#09090B",
        "#282A36",
        "#FFFFFF",
        "#F1F1F1",
        "#202020",
        "#FAFAFA",
        "#F8FEEF",
        "#0E172A",
        "#20161F",
        "#FFFFFF",
        "#2A303C",
        "#ECEFF4",
        "#131C23",
    ]
    selected_theme = themes[index]
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] > .main  {{
            background: {selected_theme};
        }}
        sidebar .sidebar-content .css-1aumxhk{{
            background-color: {selected_theme} !important;
        }}
        </style>
            """,
        unsafe_allow_html=True,
    )
    sidebar_color(selected_theme)

    return selected_theme


def hide_header(stat=True):
    if stat == True:
        stat = "none"
    else:
        stat = "block"
    st.markdown(
        f"""
    <style>
    [data-testid="stHeader"]   {{
        display:{stat}
    }}
    </style>
        """,
        unsafe_allow_html=True,
    )


def initUi():
    """
    Cette fonction permet d'initialiser les dependance css et js de daisy ui
    et tailwinds css
    """
    package_directory = os.path.dirname(__file__)
    source_data = (
        "\n"
        + dependencies(os.path.join(package_directory, "css/daysiui.css"), "css")
        + "\n"
        + dependencies(os.path.join(package_directory, "css/tailwind.css"), "css")
        + "\n"
        + dependencies(os.path.join(package_directory, "css/tailwindcss.js"), "js")
        + "\n"
    )
    html(source_data)
    return True


# -----------------------------------------------
# |             Définitions des Classes         |
# -----------------------------------------------
class ui:
    """Class^pour creer des compsantes ui."""

    def __init__(self):
        """Initialisation de la classe MaClasse."""
        pass

    def theme(index=0):
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
        selected_theme = themes[index]
        # print(len(themes), "theme")

        return selected_theme

    def h(text, size=5, font="sans", theme="light"):
        """Permet de ccreer un header (Balise en h)
        parametres:
            -text: le texte du titre
            -size: taille du texte vari de 1 à 9
                defaut:5
            -font: defini le font family du titre.Valeurs possibles : sans,mono,serif
                defaut:sans
        """
        html(
            f'<h1 data-theme={theme} class="font-{font} text-{size}xl font-bold text-slate-900">{text}</h1>'
        )

    def p(text, font="sans", theme="light"):
        """Permet de creer un paragraphe"""
        html(
            f"""<p data-theme={theme} class="font-{font}">{text}
            </p>
            """
        )

    def stats(liste, style="primary", theme="light"):
        """
        Permet de faire des resumées statstistiques
        parametre:
                liste: une liste de tuple contenant 4 valeurs: (emoji_figure, Titre, valeur, description),
                exemple de tuple: ("😂", "Total Likes", "25.6K", "21% more than last month"),

        """
        all_stats = ""
        for x in range(len(liste)):
            stat = f"""
              <div class="stat">
                <div class="stat-figure text-primary text-5xl">
                  {liste[x][0]}
                </div>
                <div class="stat-title">{liste[x][1]}</div>
                <div class="stat-value text-primary">{liste[x][2]}</div>
                <div class="stat-desc text-{style}">{liste[x][3]}</div>
              </div>
            """
            all_stats += stat
        html(
            f"""
            <center data-theme="{theme}">
            <div class="stats shadow">
            {all_stats}
            </div>
          </center>
            """
        )

    def demo():
        data = bridge("my-bridge", default="no button is clicked")
        html(
            """
        <button onClick="stBridges.send('my-bridge', 'button 1 is clicked')">Button 1</button>
        <button onClick="stBridges.send('my-bridge', 'button 2 is clicked')">Button 2</button>
        <button onClick="stBridges.send('my-bridge', 'button 3 is clicked')">Button 3</button>
        """
        )
        return data

    def button(text, key, model="", theme="light"):
        """
        Creer un bouton cliquable.
        parametres:
                text: le texte du bouton
                model: le type du bouton pour jouer sur l'affichage
                        defaut:""
        liste des differents types de boutons
            <button class="btn">{name}</button>
            <button class="btn btn-neutral">Neutral</button>
            <button class="btn btn-primary">Primary</button>
            <button class="btn btn-secondary">Secondary</button>
            <button class="btn btn-accent">Accent</button>
            <button class="btn btn-ghost">Ghost</button>
            <button class="btn btn-link">Link</button>
            <button class="btn btn-info">Info</button>
            <button class="btn btn-success">Success</button>
            <button class="btn btn-warning">Warning</button>
            <button class="btn btn-error">Error</button>
            <button class="btn btn-outline">Default</button>
            <button class="btn btn-block">Block</button>
            <button class="btn btn-circle">Circle</button>
        """
        data = bridge(key, default=False)
        html(
            f"""
            <button data-theme={theme} class="btn btn-{model}" onClick="stBridges.send('{key}', 'True')">{text}</button>
            """
        )
        if data == False:
            return data
        else:
            return True

    def dropdown(key, text, options, mode="", theme="light"):
        selected = bridge(key, default=options[0])
        liste = ""
        for x in range(len(options)):
            li = f"""<li onClick="stBridges.send('{key}', '{options[x]}')"><a>{options[x]}</a></li>"""
            liste += li

        html(
            f"""
            <div class="dropdown dropdown-{mode}" data-theme="{theme}">
              <div tabindex="0" role="button" class="btn m-1">{text}</div>
              <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
                {liste}
              </ul>
            </div>
            """
        )
        return selected

    def dropdown_navbar():
        html(
            """
            <div class="navbar bg-base-300 rounded-box">
              <div class="flex-1 px-2 lg:flex-none">
                <a class="text-lg font-bold">daisyUI</a>
              </div> 
              <div class="flex justify-end flex-1 px-2">
                <div class="flex items-stretch">
                  <a class="btn btn-ghost rounded-btn">Button</a>
                  <div class="dropdown dropdown-end">
                    <div tabindex="0" role="button" class="btn btn-ghost rounded-btn">Dropdown</div>
                    <ul tabindex="0" class="menu dropdown-content z-[1] p-2 shadow bg-base-100 rounded-box w-52 mt-4">
                      <li><a>Item 1</a></li> 
                      <li><a>Item 2</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            """
        )

    def modal(button="Click", message="This is a modal", close="Ok", theme="light"):
        """To create a modal
        
        Keyword arguments:
        Button -- texte du Bouton declancheur 
        message -- Message a afiicher
        close -- texte du bouton fermer 
        theme -- theme du bouton
        Return: un code html de modal
        """
        
        html(
            f"""
            <button data-theme={theme} class="btn" onclick="my_modal_1.showModal()">{button}</button>
            <dialog id="my_modal_1" class="modal" data-theme={theme}>
              <div class="modal-box">
                <h3 class="font-bold text-lg">Hello!</h3>
                <p class="py-4">{message}</p>
                <div class="modal-action">
                  <form method="dialog">
                    <button class="btn">{close}</button>
                  </form>
                </div>
              </div>
            </dialog>
            """
        )

    def swap_darkmode():
        html(
            """
            <label class="swap swap-rotate">
              <!-- this hidden checkbox controls the state -->
              <input type="checkbox" />
              <!-- sun icon -->
              <svg class="swap-on fill-current w-10 h-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z"/></svg>
              
              <!-- moon icon -->
              <svg class="swap-off fill-current w-10 h-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"/></svg>
              
            </label>

            """
        )

    def swap_hamburger(key, theme="light", style=""):
        state = bridge(key, default=True)
        html(
            f"""
            <label onClick="stBridges.send('{key}', false)" data-theme={theme} class="btn btn-circle swap swap-rotate" style="{style}">   
              <!-- this hidden checkbox controls the state -->
              <input type="checkbox"/>
              
              <!-- hamburger icon -->
              <svg class="swap-off fill-current" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512"><path d="M64,384H448V341.33H64Zm0-106.67H448V234.67H64ZM64,128v42.67H448V128Z"/></svg>
              
              <!-- close icon -->
              <svg class="swap-on fill-current" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512"><polygon points="400 145.49 366.51 112 256 222.51 145.49 112 112 145.49 222.51 256 112 366.51 145.49 400 256 289.49 366.51 400 400 366.51 289.49 256 400 145.49"/></svg>
              
            </label>
            """
        )
        # if state == False:
        #     state = True
        # else:
        #     state = False
        return state

    def swap_custom(on, off):
        html(
            f"""
                <label class="swap swap-flip text-9xl">
                    
                    <!-- this hidden checkbox controls the state -->
                    <input type="checkbox" />
                    
                    <div class="swap-on">{on}</div>
                    <div class="swap-off">{off}</div>
                </label>
            """
        )
    def name():
        """
        Purpose: 
        """
        html(f"""

            """)
        
    # end def

# -----------------------------------------------
# |                 Demo if Main                |
# -----------------------------------------------
if __name__ == "__main__":
    pass
