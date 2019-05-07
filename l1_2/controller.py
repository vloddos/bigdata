import re


class Animation:
    # buffer = ''

    # нет проверки на количество переменных/значений при множественном присвоении в классе
    # width, height, frames, frames_position = [None] * 4  # syntax???

    def __init__(self, path: str, buffer_size: int):
        self.file = open(path)
        self.buffer_size = buffer_size

        m = re.search(
            r'{"width": (\d+), "height": (\d+), "frames": (\d+), "animation": \[',
            self._read(100)
        )
        if m:
            self.width, self.height, self.frames, self.frames_position = *map(int, m.group(1, 2, 3)), m.span()[1] - 1
            self.length = self.width * self.height
        else:
            self.file.close()
            raise ValueError("'json object has wrong format")

    def _read(self, size):
        return self.file.read(size)

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
            current_frame += [eval(j.group(0)) for j in l]
            li = l[-1].span()[1]
            self.buffer = self.buffer[li:] + self._read(li)

        self.current_frame_index += 1
        return current_frame

    def __del__(self):
        if not self.file.closed:
            self.file.close()
