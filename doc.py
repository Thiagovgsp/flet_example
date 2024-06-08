import flet as ft

def main(page: ft.Page):
    
    page.title = "Routes Example"
    page.scroll = ft.ScrollMode.ALWAYS

    
    def route_change(route):

        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit car", on_click=lambda _: page.go("/car")),




ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='https://www.shutterstock.com/image-photo/passenger-blue-car-isolated-on-600nw-2307569255.jpg',
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://www.shutterstock.com/image-photo/passenger-blue-car-isolated-on-600nw-2307569255.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            #on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://img.freepik.com/vetores-gratis/carro-vermelho-hatchback-isolado-no-branco-vector_53876-67348.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            #on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://img.freepik.com/vetores-gratis/imagem-tridimensional-do-carro-verde-isolado-no-fundo-branco_53876-40876.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            #on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )







                ],
            )
        )
        if page.route == "/car":
            page.views.append(
                ft.View(
                    "/car",
                    [
                        ft.AppBar(title=ft.Text("car"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    layout = ft.Container(
        width=1200,
        height=600,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,

        )
    )

    centered_layout = ft.Container(
        alignment=ft.alignment.center,
        content=layout
    )

    page.add(centered_layout)


if __name__ == "__main__":
    ft.app(target=main)