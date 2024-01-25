import flet as ft
from client import predict

all_categories = [
    "Беспроводные наушники",
    "Мужская футболка",
    "Женская футболка",
    "Женские кроссовки",
    "Светодиодная лента",
    "Чехол на телефон",
]

model_configs = {
    "Беспроводные наушники": {
        "name_model": "models/беспроводные наушники.joblib",
        "size": 120,
    },
    "Мужская футболка": {
        "name_model": "models/мужскяа футболка.joblib",
        "size": 393,
    },
    "Женская футболка": {
        "name_model": "models/женская футболка.joblib",
        "size": 113,
    },
    "Женские кроссовки": {
        "name_model": "models/женские кроссовки.joblib",
        "size": 86,
    },
    "Светодиодная лента": {
        "name_model": "models/светодиодная лента.joblib",
        "size": 153,
    },
    "Чехол на телефон": {
        "name_model": "models/чехол на телефон.joblib",
        "size": 184,
    },
}

class PageWidget:
    def __init__(self, page: ft.Page):
        self._page = page
        self._choose_category_label = ft.Text("Выберите категорию товаров: ")
        self._selected_category = ft.Text()
        self._dropdown = ft.Dropdown(options=[ft.dropdown.Option(item) for item in all_categories], width=200)
        self._filepath_text = ft.Text(value="Selected file path")
        self._filepicker = ft.FilePicker(on_result=self._return_file)
        self._filepicker_row = self._create_filepicker_row()
        self._file_preview = ft.Image(src=f"{self._filepath_text.value}", width=200, height=200)
        self._file_preview_container = ft.Container(content=self._file_preview)
        self._name_field = ft.TextField(label="Введите название", autofocus=True)
        self._price_field = ft.TextField(label="Цена", autofocus=True)
        self._predict_text = ft.Text()
        self._predict_btn = ft.ElevatedButton(text="Предсказать", on_click=self._button_clicked)

        page.title = "SalesVision"

    def render(self):
        self._page.horizontal_alignment = "center"
        self._page.vertical_alignment = "top"
        self._page.padding = 25
        self._page.theme_mode = "light"

        self._page.add(
            self._choose_category_label,
            self._dropdown,
            self._filepicker_row,
            ft.Divider(thickness=1),
            self._file_preview_container,
            ft.Divider(thickness=1),
            self._name_field,
            self._price_field,
            ft.Divider(thickness=1),
            self._predict_btn,
            self._predict_text
        )

        self._page.update()

    def _create_filepicker_row(self):
        row = ft.Row()
        row.controls.append(ft.ElevatedButton(text="Выберите изображение...", on_click=self._select_file))
        row.controls.append(self._filepath_text)

        return row

    def _select_file(self, e):
        self._page.add(self._filepicker)
        self._filepicker.pick_files("Select file...")

    def _return_file(self, e: ft.FilePickerResultEvent):
        filepath = e.files[0].path
        # Заменяем обратные слеши на прямые
        filepath = filepath.replace("\\", "/")

        self._filepath_text.value = filepath
        self._file_preview.src = filepath
        self._page.update()

    def _button_clicked(self, e):
        model_config = model_configs[self._dropdown.value]

        if model_config:
            predicted_sold_value = predict(
                model_config["name_model"],
                f"{self._file_preview.src}",
                self._name_field.value,
                self._price_field.value,
                model_config["size"]
            )
            self._predict_text.value = f"Количество продаж: {predicted_sold_value}"

        self._page.update()


def main(page: ft.Page):
    page_widget = PageWidget(page)
    page_widget.render()


ft.app(target=main)
