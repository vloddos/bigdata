import time

from PIL import Image

import matplotlib.pyplot as pp
from matplotlib.animation import FuncAnimation

from l2_boosted.controller import Animation


class Drawer:

    def __init__(self, animation: Animation):
        self.animation = animation

    def draw_PIL(self):
        while True:
            for i in self.animation:
                img = Image.fromarray(i)
                img.show()
                time.sleep(0.1)
                img.close()

    def draw_mpl(self):
        f, a = pp.subplots()

        def update(frame):
            a.clear()
            a.axis('off')
            a.imshow(frame)

        ani = FuncAnimation(f, update, frames=self.animation,
                            interval=100)  # без присваивания чему-то почему-то не работает
        pp.show()
