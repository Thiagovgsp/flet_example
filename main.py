import flet as ft

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.BLACK

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5

        main_image.update()
        options.update()


    product_images = ft.Container(
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
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://img.freepik.com/vetores-gratis/carro-vermelho-hatchback-isolado-no-branco-vector_53876-67348.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://img.freepik.com/vetores-gratis/imagem-tridimensional-do-carro-verde-isolado-no-fundo-branco_53876-40876.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )
    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='CARROS',
                    color=ft.colors.AMBER,
                ),
                ft.Text(
                    value='Carro Azul Hatch',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Carro de passeio',
                    color=ft.colors.GREY, italic=True
                ),
                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 100.000',
                            color=ft.colors.WHITE,
                            size=30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            spacing=5,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='O carro é Azul e é muito confortável para passeios e viagens de longa distância. Maravilhoso para qualquer ocasião.',
                                    color=ft.colors.GREY
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='- Azul, \n- Hatch \n- Rodas de liga leve \n- Brilho \n- Vidro',
                                    color=ft.colors.GREY
                                )
                            )
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Cor',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Amarelo'),
                                ft.dropdown.Option(text='Azul'),
                                ft.dropdown.Option(text='Vermelho'),
                            ]
                        ),
                        ft.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} uni.') for num in range(1, 8)
                            ]
                        ),
                    ]
                ),
                ft.Container(expand=True),
                ft.ElevatedButton(
                    on_click=lambda _: print("done") and page.go("/car"),
                    width=900,
                    text='Adicionar à lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.WHITE,
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK
                        }
                    )
                ),
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                        style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER)
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.AMBER,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.WHITE
                        }
                    )
                )
            ]
        )
    )

    layout = ft.Container(
        width=1200,
        height=600,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )

    centered_layout = ft.Container(
        alignment=ft.alignment.center,
        content=layout
    )

    page.add(centered_layout)

if __name__ == "__main__":
    ft.app(target=main)
