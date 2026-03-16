import flet as ft
import random

def main(page: ft.Page):
    page.title = "El amazing Magic 8-Ball"
    si_answers = ["Si", "Claro que yes", "OBVIOUSLY", "O pero claroooo"]
    no_answers = ["No", "Claro que no", "Oh gosh", "Girl bye"]
    sixseven_answers = ["Maybe", "Puede ser", "67", "Mas o menos"]
    pregunta_text = ft.TextField(label = "Ask a si/no question", width = 400)
    respuesta_text = ft.Text("", size = 20)

    def get_magic_respuesta(e):
        luka = random.randint(1, 3)
        if luka == 1:
            respuesta_text.value = random.choice(si_answers)
        elif luka == 2:
            respuesta_text.value = random.choice(no_answers)
        else:
            respuesta_text.value = random.choice(sixseven_answers)
        page.update()

    ask_button = ft.Button(ft.Text("Preguntale al 8-Ball"), get_magic_respuesta)
    page.add(pregunta_text, ask_button, respuesta_text)

ft.app(target = main)
#SIX SEVEN PARA SIEMPREE