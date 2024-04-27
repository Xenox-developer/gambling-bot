from aiogram import Dispatcher

from ._menu import router as menu_router


def include_routers(dp: Dispatcher) -> None:
    dp.include_routers(
        menu_router,
    )
