class FlatIterator:
    def __init__(self, lists):
        self.lists = lists
        self.start = -1
        self.end = len(lists)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self

    def __str__(self):
        return '\n'.join(str(item) for item in self.lists[self.start])

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)