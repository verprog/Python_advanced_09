class MyList:
    def __init__(self, *list_):
        self._list = [*list_]

    def pop(self):
        try:
            return self._list.pop()
        except IndexError:
            return f'Error: stack is empty'

    def append(self, item):
        self._list.append(item)

    def insert(self, index, item):
        self._check_range(index)
        self._list.insert(index, item)

    def remove(self, item):
        self._list.remove(item)

    def clear(self):
        self._list.clear()

    def __getitem__(self, index):
        self._check_range(index)
        return self._list[index]

    def __setitem__(self, index, value):
        self._check_range(index)
        self._list[index] = value

    def _check_range(self, index):
        if index < 0 or index > len(self._list):
            raise IndexError

    def __len__(self):
        return len(self._list)

    @property
    def head(self):
        return self[0]

    @property
    def tail(self):
        return self[len(self._list)-1]

    def __str__(self):
        return str(self._list)

a = MyList(1,2,3)

for i in a:
    print(i)
print('\n')
print(a.pop(), '-- pop \n')
a.append(34)
print(a.tail, '-- append \n')

a.insert(2, 100)

print('after insert')
for i in a:
    print(i)

print('\nafter remove ')
a.remove(1)
for i in a:
    print(i)

print('\nafter clear ')
a.clear()
print(a.__len__())


