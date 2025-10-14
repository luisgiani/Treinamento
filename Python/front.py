import flet as ft

def main(page: ft.Page):
    page.window.width = 430
    page.window.height = 620
    page.bgcolor = "gray"
    texto = ft.Text(value="Hello, world!", color="green")
    page.add(
	ft.Row(controls=[
		texto,
		ft.Text("B"),
		ft.Text("C")
		])
	)
    page.add(
    ft.Row(controls=[
        ft.TextField(label="Digite aqui:"),
        ft.ElevatedButton(text="Clique aqui!")
    ])
    )

ft.app(main)