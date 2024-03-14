from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.requests import get_categories, get_items_by_category

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
        [InlineKeyboardButton(text='Корзина', callback_data='basket'),
         InlineKeyboardButton(text='Контакты', callback_data='contacts')]
    ], resize_keyboard=True, input_field_placeholder='Выберите опцию'
)

to_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='to_main')]])


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    return keyboard.adjust(2).as_markup()


async def items(category_id: int):
    all_items = await get_items_by_category(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    return keyboard.adjust(2).as_markup()
