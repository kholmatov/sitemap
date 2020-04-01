# -*- coding: utf-8 -*-
import sys
from sitemap import runner
from sitemap.bor import Bor
from sitemap.render import Render

def trie(done):
    """
    Функция которое создаёт
    структуру дерево
    :param done:
    :type done: dict
    :return: dict
    """
    bor = Bor()
    for key, value in done.items():
        bor.add([i for i in key
                .replace("https://", "")
                .replace("http://", "")
                .split("/") if i])
    return bor.node


if __name__ == '__main__':
    # main_url = sys.argv[1]
    main_url = 'http://i-taj.com'
    node = trie(runner(main_url))
    if node:
        render = Render()
        render.start(node)
        render.finish('graph.png')
