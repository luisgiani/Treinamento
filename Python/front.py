import flet as ft

def main(page: ft.Page):
    page.window.width = 430
    page.window.height = 620
    texto = ft.Text(value="Hello, world!", color="green")
    page.add(texto)

ft.app(main)