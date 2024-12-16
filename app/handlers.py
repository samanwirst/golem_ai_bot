from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello!")