
import flet as ft


def hello(e):
    print(e)
    print('Click_Function Executed inside the Container')


def main(page: ft.Page):
    page.title = 'Container'
    page.padding = 20
    page.bgcolor = ft.colors.WHITE
    c = ft.Container(
        content = ft.Text(
            value = '도장 환입률 계산 tool',
            color = 'Black',
            weight = 'bold',
            size = 20
        ),
        width = 300,
        height = 100,
        padding = ft.padding.all(10),
        border_radius = ft.border_radius.all(5),
        # border_radius = ft.border_radius.only(top_left = 20, bottom_right = 20),
        on_click = lambda e: hello(e),
        # on_hover = lambda e: hello(e),
        # on_long press = lambda e: hello(e),
        gradient = ft.LinearGradient(
            # title_mode = "mirror"
            begin = ft.alignment.top_right,
            end = ft.alignment.bottom_right,
            colors = [
                "WHITE",
                # "red12",
                # "purple12",
                "WHITE",
                # "blue26"
            ],
        ),
        border = ft.border.all(width = 5, color = ft.colors.BLACK12),
        margin = ft.margin.all(30),
        # margin = ft.margin.only(top = 20, left =20),
        tooltip = "container for showing Hello"
    )

    page.add(c)

ft.app(target = main, view = ft.FLET_APP)
