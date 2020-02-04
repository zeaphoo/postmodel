
__version__ = '0.1.0'

import sys

if sys.version_info < (3, 6):  # pragma: nocoverage
    raise RuntimeError("Postmodel requires Python 3.6")

from postmodel.main import Postmodel
from postmodel.model import Model
import asyncio
from typing import Coroutine


def run_async(coro: Coroutine) -> None:
    """
    Simple async runner that cleans up DB connections on exit.
    This is meant for simple scripts.

    Usage::

        from postmodel import Postmodel, run_async

        async def do_stuff():
            await Postmodel.init(
                db_url='sqlite://db.sqlite3',
                modules=['app.models']
            )

            ...

        run_async(do_stuff())
    """
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(coro)
    finally:
        loop.run_until_complete(Postmodel.close())