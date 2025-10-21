import flet as ft

def main(page: ft.Page):
    page.title = "Projetinho teste"
    page.window.width = 830
    page.window.height = 800
    page.bgcolor = "gray"
    page.spacing = 20
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    titulo = ft.Text(
        value="Teste",
        size= 32
    )

    texto =  ft.Text(value="Qual é a cor de plano de fundo?", 
                color="white", 
                size= 20, 
                )

    digitar = ft.TextField(label="Digite aqui a sua resposta:", 
                     text_size=20
                     )

    
    btn = ft.ElevatedButton(
            text="Responder", 
           # on_click= valida_resposta(digitar)
            )

    page.add(titulo, texto, digitar, btn)

ft.app(main)