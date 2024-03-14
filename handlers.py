from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import keyboards as kb
from database.requests import get_item_id, set_user

rt = Router()


@rt.message(CommandStart())
@rt.callback_query(F.data == 'to_main')
async def start(message: Message | CallbackQuery):
    if isinstance(message, Message):
        await set_user(message.from_user.id)
        await message.answer(f'Welcome, <b>{message.from_user.first_name}</b>!',
                             reply_markup=kb.main)
    else:
        await message.message.edit_text(f'Welcome, <b>{message.from_user.first_name}</b>!',
                                        reply_markup=kb.main)


@rt.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Выберите категорию', reply_markup=await kb.categories())


@rt.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='Выберите интересующий вас товар',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@rt.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_info = await get_item_id(callback.data.split('_')[1])
    await callback.answer('')
    await callback.message.answer(f'{item_info.name}\n\n{item_info.description}\n\n<b>$ {item_info.price}</b>',
                                  reply_markup=kb.to_main)
