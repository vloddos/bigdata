import tkinter
from .controller import Animation


class Drawer:

    def __init__(self, animation: Animation):
        self.animation = animation
        self.coords = [(j, i) for i in range(self.animation.height) for j in range(self.animation.width)]

    def draw(self):
        tk = tkinter.Tk()
        c = tkinter.Canvas(tk, width=self.animation.width, height=self.animation.height)

        def command():
            b.destroy()

            it = iter(self.animation)

            def i():
                tk.after(100, frame, next(it))

            def frame(f):
                nonlocal it
                for ji, k in zip(self.coords, f):
                    color = '#' + hex(k[0] * 256 ** 2 + k[1] * 256 + k[2])[2:].zfill(6)  # fixme simplify?
                    c.create_rectangle(
                        *ji, ji[0] + 1, ji[1] + 1,
                        fill=color,
                        outline=color
                    )
                try:
                    i()
                except StopIteration:
                    it = iter(self.animation)
                    i()

            i()

        b = tkinter.Button(tk, text='start', command=command)
        b.pack()
        c.pack()

        tk.mainloop()
