# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import logging
import re
import urllib.parse


class Spider:

    def __init__(self, main_url,
                 task_queue=set,
                 max_tasks=50,
                 done=dict):
        """
        Spider конструктор
        :param main_url: основной url сайта
        :type main_url: str
        :param max_tasks: максимальное количество заданий.
        :type max_tasks: int
        """
        self.main_url = main_url
        self.task_queue = task_queue()
        self.max_tasks = max_tasks
        self.done = done()
        self.busy = set()
        self.tasks = set()
        self.semaphore = asyncio.Semaphore(max_tasks)
        self.session = aiohttp.ClientSession()

    async def start(self):
        """
        Основная функция для начала парса сайта
        :return:
        """
        future = asyncio.ensure_future(self.add_urls([(self.main_url, '')]))
        await asyncio.sleep(1)
        while self.busy:
            await asyncio.sleep(1)

        await future
        await self.session.close()

        # print([key for key, value in self.done.items() if value])

    async def add_urls(self, urls):
        """
         Добавьте URL в очередь и запустите процесс для парсинга
        :param urls:
        :type urls: list
        :return:
        """
        for url, parent_url in urls:
            url = urllib.parse.urljoin(parent_url, url)
            if (url.startswith(self.main_url) and
                    url not in self.busy and
                    url not in self.done and
                    url not in self.task_queue):
                self.task_queue.add(url)
                # Приобрести семафор
                await self.semaphore.acquire()
                # Создать асинхронную задачу
                task = asyncio.ensure_future(self.work(url))
                # Добавить обратный вызов в задачу, чтобы освободить семафор
                task.add_done_callback(lambda t: self.semaphore.release())
                # Обратный вызов для удаления задачи из задач
                task.add_done_callback(self.tasks.remove)
                # Добавить задачу в задачи
                self.tasks.add(task)

    async def work(self, url):
        """
        Работа с url
        :param url:
        :type url: str
        :return:
        """
        logging.info('в процессе: %s', url)
        # удалить URL из основной очереди
        # и добавить его в список занятости
        self.task_queue.remove(url)
        self.busy.add(url)
        try:
            resp = await self.session.get(url)
        except Exception as exc:
            # в любом исключении пометьте url как плохой
            logging.error('... %s имеет ошибку %s', url, repr(str(exc)))
            self.done[url] = False
        else:
            # парсить только url со status == 200 и
            # типом content == 'text/html'
            if (resp.status == 200 and
                    ('text/html' in resp.headers.get('content-type'))):
                data = (await resp.read()).decode('utf-8', 'replace')
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data)
                asyncio.Task(self.add_urls([(u, url) for u in urls]))

            # даже если у нас нет исключений,
            # мы можем пометить url как хороший
            resp.close()
            self.done[url] = True

        self.busy.remove(url)
        logging.info('%s выполненные задачи, '
                     '%s все еще в ожидании, '
                     'todo_queue %s',
                     len(self.done),
                     len(self.tasks),
                     len(self.task_queue))
