


class Reverse:
    """Iterator for looping over a sequence backwards."""
    with open('goods.txt', 'r', encoding='utf-8') as data:
        data = data.readlines()

        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index -= 1
            return self.data[self.index]


rev = Reverse(data)
# iter(rev)
for char in rev:
    print(char)