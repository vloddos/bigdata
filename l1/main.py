from json import load
import tkinter
from threading import Lock


def draw(canvas: tkinter.Canvas, frames):
    animation.i = (animation.i + 1) % len(frames)

    for i in zip(animation.coords, frames[animation.i]):
        canvas.create_rectangle(*i[0], fill='#' + hex(i[1][0] * 256 ** 2 + i[1][1] * 256 + i[1][2])[2:].zfill(6))


def start():
    with start.after_lock:
        if start.tk:
            start.tk.after_cancel(start.after)
            start.tk.destroy()

    with open(t.get('1.0', tkinter.END).strip(), 'r') as f:
        frames = load(f)

    start.tk = tkinter.Tk()
    start.tk.bind('<Destroy>', _destroy)
    c = tkinter.Canvas(start.tk, width=450, height=450)
    c.pack()

    animation(start.tk, c, frames)


start.tk: tkinter.Tk = None
start.after_lock: Lock = Lock()
start.after = None


def _destroy(e):
    start.tk = None


def animation(tk: tkinter.Tk, canvas: tkinter.Canvas, frames):
    draw(canvas, frames)
    with start.after_lock:
        start.after = tk.after(100, animation, tk, canvas, frames)


animation.i = 0
animation.coords = [
    [0, 0, 150, 150],
    [150, 0, 300, 150],
    [300, 0, 450, 150],
    [0, 150, 150, 300],
    [150, 150, 300, 300],
    [300, 150, 450, 300],
    [0, 300, 150, 450],
    [150, 300, 300, 450],
    [300, 300, 450, 450]
]

root = tkinter.Tk()

t = tkinter.Text(root, width=50, height=1)
t.grid(row=1, column=2)

tkinter.Button(root, text='start', command=start).grid(row=1, column=1)

root.mainloop()
