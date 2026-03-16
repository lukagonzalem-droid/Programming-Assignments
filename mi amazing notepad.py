import flet as ft

def main(page: ft.Page):
    page.title = "Mi Amazing Notepad"
    word_count_luka = ft.Text("Words aka Palabras: 0")
    character_count_gonzalez = ft.Text("Characters akaa Personajkes: 0")

    def update_counts(e):
        luka = luka_field.value.strip()
        character_count = len(luka)
        word_count = len(luka.split()) if luka else 0
        word_count_luka.value = f"Words aka Palabras: {word_count}"
        character_count_gonzalez.value = f"Characters aka Personakes: {character_count}"
        page.update()

    def clear_text(e):
        luka_field.value = ""
        update_counts(None)

    luka_field = ft.TextField(multiline = True, expand = True, on_change = update_counts)
    clear_button = ft.TextButton("Clearrrrr", on_click = clear_text)
    page.add(luka_field, word_count_luka, character_count_gonzalez, clear_button)

ft.app(target = main)