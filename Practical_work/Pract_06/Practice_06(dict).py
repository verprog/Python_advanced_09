class myDict:
    def __init__(self):
        self.key = []
        self.value = []

    def assign(self, k, v):
        if k in self.key:
            self.value[self.key.index(k)] = v
        else:
            self.keys.append(k)
            self.values.append(v)

    def getval(self, k):
        """ k, immutable object  """
        try:
            return self.values[self.keys.index(k)]

        except:
            raise KeyError('Key not in list')

    def delete(self, k):
        """ k, immutable object """
        try:
            self.values = self.values[0:self.keys.index(k)] + self.values[self.keys.index(k) + 1:]
            self.keys = self.keys[0:self.keys.index(k)] + self.keys[self.keys.index(k) + 1:]

        except:
            raise KeyError('Key not in list')


d1 = myDict()
d1.assign(1, 2)
d1.assign(3, 4)
print(d1.getval(4))

a = MyDict({'test':123,'kay':555,'lol':7777},)
print(a)

