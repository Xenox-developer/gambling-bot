from aiogram import Router, types
from aiogram.filters import CommandStart

from src.utils import messages as msg

router = Router()


@router.message(CommandStart())
async def menu(message: types.Message):
    await message.answer(text=msg.menu)
