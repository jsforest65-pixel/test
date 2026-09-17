import flet as ft

def main(page: ft.Page):
    page.title = "Flet 카운터 앱"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 숫자를 표시할 텍스트 컴포넌트
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # 화면에 버튼과 입력창 배치
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
