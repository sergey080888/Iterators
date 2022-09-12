nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],

    ]


class FlatIterator:
    def __init__(self, list_):
        self._stopped = False
        self.list_ = list_
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self.i < len(self.list_):
                if self.j < len(self.list_[self.i]):
                    v = self.list_[self.i][self.j]
                    self.j += 1
                    return v

                self.i += 1
                self.j = 0
            self._stopped = True
        raise StopIteration


nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
    for list_ in some_list:
        for list_l in list_:
            yield list_l


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for item in flat_generator(nested_list2):
        print(item)
