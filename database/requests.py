from database.models import *

from sqlalchemy import select, update, delete


async def set_user(tg_id):
    async with async_session() as connect:
        user = await connect.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            connect.add(User(tg_id=tg_id))
            await connect.commit()


async def get_users():
    async with async_session() as connect:
        users = await connect.scalars(select(User))
        return users

async def get_categories():
    async with async_session() as connect:
        categories = await connect.scalars(select(Category))
        return categories


async def get_items_by_category(category_id: int):
    async with async_session() as connect:
        items = await connect.scalars(select(Item).where(Item.category == category_id))
        return items


async def get_item_id(item_id: int):
    async with async_session() as connect:
        item = await connect.scalar(select(Item).where(Item.id == item_id))
        return item
