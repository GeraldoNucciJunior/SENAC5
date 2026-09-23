import flet as ft


def main(page: ft.Page):
    page.title = "Saudação"
    page.window.width = 400
    page.window.height = 300
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome_input = ft.TextField(label="Digite seu nome", width=250)
    resultado = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def ao_clicar(e):
        nome = nome_input.value.strip()
        if nome:
            resultado.value = f"Oi, {nome}!"
        else:
            resultado.value = "Oi!"
        page.update()

    botao = ft.ElevatedButton(text="OK", on_click=ao_clicar)

    page.add(
        ft.Column(
            controls=[nome_input, botao, resultado],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
