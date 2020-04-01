# -*- coding: utf-8 -*-
class Bor:
    """
    Бор, или префиксное дерево,
    структура данных для
    эффективного хранения
    и обработки строк
    """

    def __init__(self):
        """
        Bor конструктор
        """
        self.node = {}

    def add(self, items):
        """
        Добавления в бор очередной строки
        :param items:
        :type items:[list, dict, str]
        :return:
        """
        node = self.node
        for item in items:
            if item not in node:
                node[item] = {}
            node = node[item]

    def get(self):
        """
        :return:Bor
        """
        return self.node

    def util_url(self, done):
        """
        Функция которое создаёт
        структуру дерево
        :param done:
        :type done: dict
        :return: dict
        """
        for key, value in done.items():
            self.add([i for i in key
                     .replace("https://", "")
                     .replace("http://", "")
                     .split("/") if i])
        return self.node
