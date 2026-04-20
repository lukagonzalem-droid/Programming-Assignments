import flet as ft

def main(page: ft.Page):
    page.title = "El Quote Translator"
    quotes = {"English": "It always seems impossible until it's done", "Spanish": "Siempre parece imposible hasta que se logra", "Korean": "무엇이든 이루어지기 전까지는 불가능해 보인다"}
    quote_aja = ft.Text(value = quotes["English"], size = 25, weight = "bold", text_align = "center")

    def change_language(e):
        selected_language = radio_group.value
        quote_aja.value = quotes[selected_language]
        page.update()
    radio_group = ft.RadioGroup(content = ft.Column([ft.Radio(value = "English", label = "English"), ft.Radio(value = "Spanish", label = "Spanish"), ft.Radio(value = "Korean", label = "Korean"),]), value = "English", on_change = change_language)
    image = ft.Image(src = "https://www.thechurning.net/wp-content/uploads/2014/07/1441441_10151804424066977_1756041420_n.jpg", width = 200, height = 200)
    page.add(ft.Text("El Quote Translator", size = 30), image, quote_aja, radio_group)

ft.app(target = main)