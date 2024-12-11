from src.streamlit_daisy import *
import streamlit as st


# from rich import print
def main():
    # hide_header()
    theme_index = int(st.number_input("Theme", value=3))
    initUi()
    app_theme = ui.theme(theme_index)
    st_theme(theme_index)
    ui.h("Bienvenue dans mon tableau de bord", 6, "sans", theme=app_theme)
    ui.p(
        "Ce tableau de bord permet de visualiser vos données d'enquête en temps reel. Phew, with any luck we have styled the headings above this text and they look pretty good.sLet’s add a closing paragraph here so things end with a decently sized block of text. I can’t explain why I want things to end that way but I have to assume it’s because I think things will look weird or unbalanced if there is a heading too close to the end of the document.",
        "sans",
        theme=app_theme,
    )
    liste = [
        ("😂", "Total Likes", "25.6K", "Trop cool çà"),
        ("🍔", "Total Fromage", "100.6K", "21% moins"),
        ("🌭", "Total Pain", "25.6K", "21% more than last month"),
    ]
    ui.stats(liste, "warning", theme=app_theme)
    bout1 = ui.button("Bouton 1", "bout1", "primary", app_theme)
    bout1
    circul = ui.button("🍳", "circular-bout", "warning btn-circle", theme=app_theme)
    circul
    options = ["Pizza 🍕", "Oeuf 🥚", "Frites 🍟"]
    dropdown_data = ui.dropdown(
        "list-repas", "Selectionner repas 🍔", options, "top", app_theme
    )
    st.write("\n")
    dropdown_data
    ui.modal(
        "Infos",
        "☘ Vous allez liker ce tableau de bord.\n Il a été conçu par Kambou Anicet Cyrille",
        "Quitter",
        app_theme,
    )
    state = ui.swap_hamburger(
        "sidebar", theme=app_theme, style="position:fixed; top:0;left:0; z-index:100"
    )
    print("Drawer state:", state)
    print("Reloaded...")
    with st.sidebar:
        # sidebar_color(app_theme)
        buttSide=ui.button("Ok","BoutSide","primary",app_theme)
        buttSide
        ui.swap_custom("😊","😒")


if __name__ == "__main__":
    main()
