import flet as ft

def car_page(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.WHITE

    page.add(
        ft.Text(
            value="This is the car details page.",
            size=30,
            color=ft.colors.BLACK
        )
    )

if __name__ == "__main__":
    ft.app(target=car_page)
