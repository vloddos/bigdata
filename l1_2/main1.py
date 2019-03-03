from json import load
import tkinter
from threading import Thread, Lock, current_thread  # rlock???
from time import sleep


def draw(canvas: tkinter.Canvas, frames):
    animation.i = (animation.i + 1) % len(frames)

    for i in zip(animation.coords, frames[animation.i]):
        canvas.create_rectangle(*i[0], fill='#' + hex(i[1][0] * 256 ** 2 + i[1][1] * 256 + i[1][2])[2:].zfill(6))


def start(path):
    with start.tk_lock:
        if start.tk:
            start.tk.destroy()
            start.tk = None

    with open(path, 'r') as f:
        frames = load(f)

    start.tk = tkinter.Tk()
    start.tk.bind('<Destroy>', _destroy)
    c = tkinter.Canvas(start.tk, width=450, height=450)
    c.pack()

    t = Thread(target=animation, args=(start.tk, c, frames))
    t.daemon = True
    t.start()


start.tk: tkinter.Tk = None
start.tk_lock: Lock = Lock()


def _destroy(e):
    with start.tk_lock:
        if start.tk:
            start.tk = None


def animation(tk: tkinter.Tk, canvas: tkinter.Canvas, frames):
    t = Thread(target=lambda: tk.mainloop())
    t.daemon = True
    t.start()

    while True:
        with start.tk_lock:
            if start.tk:
                draw(canvas, frames)  # tk.after(0, draw, (canvas, frames))
                print(current_thread())  # debug
            else:
                break
        sleep(0.1)


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

tkinter.Button(
    root,
    text='start',
    command=lambda: start(t.get('1.0', tkinter.END).strip())
).grid(row=1, column=1)

root.mainloop()
