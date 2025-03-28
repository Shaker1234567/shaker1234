import flet as ft
 

def main(page: ft.Page):

    page.window.width = 400
    page.window.height = 600
    
    page.window.resizable = False  # لمنع تغيير حجم النافذة
    page.title = "حاسبة زكاة الفطر/ شاكر الزين"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_resizable = False
    selected_option = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="يخمس", label="يخمس"),
            ft.Radio(value="لا يخمس", label="لا يخمس"),
        ]),
        value="لا يخمس"
    )

    price_input = ft.TextField(label="سعر الكيلو", keyboard_type=ft.KeyboardType.NUMBER)
    people_input = ft.TextField(label="عدد الأفراد", keyboard_type=ft.KeyboardType.NUMBER)
    item_dropdown = ft.Dropdown(
        label="نوع المادة",
        options=[
            ft.dropdown.Option("رز"),
            ft.dropdown.Option("زبيب"),
            ft.dropdown.Option("طحين"),
            ft.dropdown.Option("أخرى"),
        ],
        value="رز"
    )

    result_text = ft.Text()

    def calculate_zakat(e):
        try:
            price = float(price_input.value)
            people = int(people_input.value)
            item = item_dropdown.value
            option = selected_option.value

            total = price * 3 * people
            if option == "لا يخمس":
                total *= 1.25  # إضافة 25٪

            result_text.value = f"المبلغ الواجب دفعه: {total:.2f} ريال مقابل {item}"
            page.update()
        except ValueError:
            result_text.value = "يرجى إدخال قيم صحيحة."
            page.update()

    calculate_button = ft.ElevatedButton(text="حساب الزكاة", on_click=calculate_zakat)

    page.add(
        selected_option,
        price_input,
        people_input,
        item_dropdown,
        calculate_button,
        result_text
    )
    
ft.app(target=main)
