import flet as ft
import json

def main(page: ft.Page):
    page.title = "Счётчик кликов"
    count = 0
    try:
        with open("result.json", "r") as f:
            count = json.load(f).get("count", 0)
    except:
        count = 0

    text = ft.Text(f"Кликов: {count}")

    def save_count():
        with open("result.json", "w") as f:
            json.dump({"count": count}, f)
        page.snack_bar = ft.SnackBar(ft.Text("Сохранено!"))
        page.snack_bar.open = True
        page.update()

    def on_click(e):
        nonlocal count
        count += 1
        text.value = f"Кликов: {count}"
        page.update()

    def on_click2(e):
        nonlocal count
        count = 0
        text.value = f"Кликов: {count}"
        page.update()

    def on_click3(e):
        save_count()

    button = ft.ElevatedButton("Нажми меня", on_click=on_click)
    button2 = ft.ElevatedButton("Сбросить", on_click=on_click2)
    button3 = ft.ElevatedButton("save", on_click=on_click3)

    page.add(text, button, button2, button3)

ft.app(target=main)