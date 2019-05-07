import re
from operator import attrgetter, not_


class Animation:
    buffer = ''
    fields = ['width', 'height', 'frames']

    width = None
    height = None
    frames = None

    frames_position = None

    def __init__(self, path: str, buffer_size: int):
        self.file = open(path, 'r')
        self.buffer_size = buffer_size

    def _read(self, size):
        return self.file.read(size)

    def init(self):
        li = 0
        while True:
            if not li:
                self.buffer = self._read(self.buffer_size)
            else:
                self.buffer = self.buffer[li:] + self._read(li)
                li = 0

            if self.buffer == '':
                aa = [f"'{i}'" for i in self.fields if not attrgetter(i)(self)]

                if not self.frames_position:
                    aa.append("'animation'")

                raise AttributeError(f"'json' object has no attributes: {', '.join(aa)}")

            for i in self.fields:
                if not attrgetter(i)(self):
                    m = re.search(fr'"{i}": (\d+)', self.buffer)
                    if m:
                        setattr(self, i, int(m.group(1)))
                        li = max(li, m.span()[1])

            m = re.search(r'"animation": \[', self.buffer)
            if m:
                self.frames_position = m.span()[1] - 1#???????????????????????????????
                li = max(li, self.frames_position + 1)

            if all(attrgetter('frames_position', *self.fields)(self)):
                self.length = self.width * self.height
                return

    def __iter__(self):
        self.file.seek(self.frames_position)
        self.buffer = self._read(self.buffer_size)
        self.current_frame_index = -1
        return self

    def __next__(self):
        if self.current_frame_index == self.frames - 1:
            raise StopIteration

        current_frame = []

        i = 0
        while i < self.length:
            l = [*re.finditer(r'\[\d{1,3}, \d{1,3}, \d{1,3}]', self.buffer), ][:self.length - i]
            i += len(l)
            for j in l:
                current_frame.append(eval(j.group(0)))

            li = l[-1].span()[1]
            self.buffer = self.buffer[li:] + self._read(li)

        self.current_frame_index += 1
        return current_frame

    def __del__(self):  # ???
        self.file.close()
