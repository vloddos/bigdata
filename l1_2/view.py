import time
import tkinter
from l1_2.controller import Animation
import random


# fixme endless loop
class Drawer:

    def __init__(self, animation: Animation):
        self.animation = animation
        self.coords = [(j, i) for i in range(self.animation.height) for j in range(self.animation.width)]  # fixme ???

    def draw(self):
        tk = tkinter.Tk()
        c = tkinter.Canvas(tk, width=self.animation.width, height=self.animation.height)

        it = iter(self.animation)

        def frame(f):
            for ji, k in zip(self.coords, f):
                color = '#' + hex(k[0] * 256 ** 2 + k[1] * 256 + k[2])[2:].zfill(6)  # fixme simplify?
                c.create_rectangle(
                    *ji, ji[0] + 1, ji[1] + 1,
                    fill=color,
                    outline=color
                )
            tk.after(100, frame, next(it))

        def loop():
            for i in self.animation:
                frame(i)
                time.sleep(0.1)
                # tk.after(0, frame, i)
            tk.after(0, loop)

        tkinter.Button(tk, text='start', command=lambda: frame(next(it))).pack()
        c.pack()

        tk.mainloop()
