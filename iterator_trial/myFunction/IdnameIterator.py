class IdnameIterator:
    def __init__(self, contents):
        self._contents = contents
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == len(self._contents):
            raise StopIteration()
        value = self._contents[self._count]
        self._count += 1
        return value