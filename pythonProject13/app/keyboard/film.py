from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_films_keyboard(films: list):
    builder = InlineKeyboardBuilder()
    for index, film in enumerate(films):
        builder.button(text=film.get('title'),
                       callback_data=f"film_{index}")
    return builder.as_markup()
def build_details_keyboard(url):
    builder = InlineKeyboardBuilder()
    builder.button(text="перейти за посиланням", url=url)
    builder.button(text="перейти назад", callback_data="back")
    return builder.as_markup()

def build_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Go back",callback_data="back")

    return builder.as_markup()
def build_start_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Гетьмани",callback_data="films")

    builder.button(text="Додати Гетьмана", callback_data="filmcreate")


    return builder.as_markup()
