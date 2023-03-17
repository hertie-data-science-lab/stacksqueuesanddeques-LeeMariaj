class Empty(Exception): pass


class ArrayDequeMaxlen():

    def __init__(self, max_len):
        self._max_len = max_len
        self._data = [None] * self._max_len
        self._size = max_len

    def __len__(self):
        return len(self._data)

    def length(self):
        if self._data[0] == None:
            return ("Empty Array")

        elif self._data[-1] != None:
            return (self._data[-1])

        else:
            return (self._data[self._data.index(None) - 1])

    def is_empty(self):
        if self._data[0] == None:
            return (True)

        else:
            return (False)

    def resize(self):
        new_space = [None] * self._size
        self._data.extend(new_space)
        self._size = self._size * 2

    def add_first(self, element):
        if self._data[-1] == None:
            temp_data = [element]
            for i in range(len(self._data) - 1):
                temp_data.append(self._data[i])
            self._data = temp_data

        else:
            self.resize()
            temp_data = [element]
            for i in range(len(self._data) - 1):
                temp_data.append(self._data[i])
            self._data = temp_data

    def add_last(self, element):
        if self._data[-1] == None:
            self._data[self._data.index(None)] = element

        else:
            self.resize()
            self._data[self._data.index(None)] = element

    def delete_first(self):
        first = self._data[0]
        self._data.pop(0)
        return (first)

    def delete_last(self):
        if self._data[-1] == None:
            position = self._data.index(None) - 1
            last = self._data[position]
            self._data.pop(position)
            return (last)

        else:
            last = self._data[-1]
            self._data.pop(-1)
            return (last)

    def remove(self, element):
        position = self._data.index(element)
        self._data.pop(position)

    def first(self):
        if self._data[0] == None:
            return ("Empty Array")
        else:
            return (self._data[0])

    def last(self):
        if self._data[0] == None:
            return ("Empty Array")

        elif self._data[-1] != None:
            return (self._data[-1])

        else:
            return (self._data[self._data.index(None) - 1])