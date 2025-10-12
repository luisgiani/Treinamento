import flet as ft

def main(page: ft.Page):
    texto = ft.Text(value="Hello, world!", color="green")
    page.controls.append(texto)
    page.update()

ft.app(main)