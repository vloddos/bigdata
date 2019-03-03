from json import dump
from random import randint


def generate(path, width, height, frames):
    with open(f'{path}', 'w') as f:
        dump(
            {
                'width': width,
                'height': height,
                'frames': frames,
                'animation': [[[randint(0, 255) for i in range(3)] for j in range(width * height)] for k in
                              range(frames)]
            },
            f
        )
