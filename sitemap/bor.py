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
