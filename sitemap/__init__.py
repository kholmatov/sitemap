# -*- coding: utf-8 -*-
import asyncio
import logging
import signal
from sitemap.spider import Spider


def runner(main_url, max_tasks=100):
    """
    Функция для запуска процесса создание карти сайта
    :param main_url: основной url сайта
    :type main_url: str
    :param max_tasks: максимальное количество заданий.
    :type max_tasks: int
    :return:
    """
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    c = Spider(main_url, max_tasks=max_tasks)
    loop.run_until_complete(c.start())
    try:
        loop.add_signal_handler(signal.SIGINT, loop.stop)
    except RuntimeError:
        pass
    logging.info('done: %d; ok: %d', len(c.done), sum(c.done.values()))
    return c.done
