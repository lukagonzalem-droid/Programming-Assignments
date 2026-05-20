import flet as ft

def main(page: ft.Page):
    def changeVolume(e):
        Number_rojo = int(Slider_rojo.value)
        Number_verde = int(Slider_verde.value)
        Number_azul = int(Slider_azul.value)

        if Number_rojo <= 85:
            extraMessage = "Red LOWWWW"
        elif Number_verde <= 85:
            extraMessage = "Green LOWWWWW"
        elif Number_azul <= 85:
            extraMessage = "Blue LOWWWW"
        else:
            extraMessage = "Mixed colorrr"
        volumeText.value = f"RGB({Number_rojo}, {Number_verde}, {Number_azul}) - {extraMessage}"
        page.bgcolor = f"#{Number_rojo:02x}{Number_verde:02x}{Number_azul:02x}"

    Slider_rojo = ft.Slider(label = "Red", value = 0, min = 0, max = 255, divisions = 255, on_change = changeVolume)
    Slider_verde = ft.Slider(label = "Green", value = 0, min = 0, max = 255, divisions = 255, on_change = changeVolume)
    Slider_azul = ft.Slider(label = "Blue", value = 0, min = 0, max = 255, divisions = 255, on_change = changeVolume)
    volumeText = ft.Text(value = "RGB(0, 0, 0)")
    page.add(volumeText, Slider_rojo, Slider_verde, Slider_azul)

ft.run(main = main)