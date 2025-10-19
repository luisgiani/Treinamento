import flet as ft

def main(page: ft.Page):
    page.title = "Projetinho teste"
    page.window.width = 830
    page.window.height = 800
    page.bgcolor = "gray"

    titulo = ft.Text(
        value=""
    )
    def valida_resposta(digitar):
        if digitar.value == '1':
            ft.Text(value="certo")
        else:
            ft.Text(value='Errado')

        page.update()

    texto =  ft.Text(value="Qual é a cor de plano de fundo?", 
                color="white", 
                size= 20, 
                text_align='center'
                )

    digitar = ft.TextField(label="Digite aqui a sua resposta:", 
                     text_size=20
                     )

    
    btn = ft.ElevatedButton(
            text="Responder", 
            on_click= valida_resposta(digitar)
            )

    page.add(texto, digitar, btn)

ft.app(main)