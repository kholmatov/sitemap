# -*- coding: utf-8 -*-
import sys
from sitemap import runner
from sitemap.bor import Bor
from sitemap.render import Render


if __name__ == '__main__':
    # main_url = sys.argv[1]
    main_url = 'http://i-taj.com'
    node = Bor().util_url(runner(main_url))
    if node:
        render = Render()
        render.start(node)
        render.finish('graph.png')
