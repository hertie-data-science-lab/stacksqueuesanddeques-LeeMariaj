# Creating the class
class ArrayDequeMaxlen():

    # Basic class parameters
    # max_len: starting size for array
    def __init__(self, max_len):
        self._max_len = max_len
        self._data = [None] * self._max_len
        self._size = max_len

    # Number of "boxes"
    def __len__(self):
        return len(self._data)

    # Number of filled "boxes"
    def length(self):
        if self._data[0] == None: # If there are no "boxes" filled
            return ("Empty Array")

        elif self._data[-1] != None: # If all boxes are filled
            return len(self._data)

        else: # When only some boxes are filled
            return (self._data[self._data.index(None)])
            # Returns the position of the first "box" filled with
            # None, which, because Python is base 0, gives the
            # amount of filled boxes

    def is_empty(self): # The array will be considered empty if the
        # first element is None
        if self._data[0] == None:
            return (True)
        # otherwise, there is at least one element
        else:
            return (False)

    def resize(self):
        # Creates a temporary variable, and saves the required none
        # spaces inside it
        new_space = [None] * self._size
        # Adds the required none spaces to the end of the current
        # array
        self._data.extend(new_space)
        # Doubles the size factor, as this was the most efficient
        # way to increase size for an array acording to class
        # materials
        self._size = self._size * 2

    # Adds an element to the left-most position of the deque
    def add_first(self, element):
        # If the deque has "empty boxes"
        if self._data[-1] == None:
            # Generate a new temp list with the new element at the
            # beginning
            temp_data = [element]
            # Add all but the last element to the temp list
            for i in range(len(self._data) - 1):
                temp_data.append(self._data[i])
            # Replace the data with our temp list
            self._data = temp_data

        else:
            # If no empty spaces, first resize
            self.resize()
            # Then repeat previous process
            temp_data = [element]
            for i in range(len(self._data) - 1):
                temp_data.append(self._data[i])
            self._data = temp_data

    # Adds an element to the right-most position of the deque
    def add_last(self, element):
        # If there are "empty boxes"
        if self._data[-1] == None:
            # Replace the first None element in the deque
            self._data[self._data.index(None)] = element

        else:
            # If no empty spaces, first resize
            self.resize()
            # Then repeat previous process
            self._data[self._data.index(None)] = element

    # Delete left-most element of the deque
    def delete_first(self):
        # Save the current first element
        first = self._data[0]
        # Pop it from our list
        self._data.pop(0)
        # Return the value
        return (first)

    # Delete right-most element of the deque
    def delete_last(self):
        if self._data[-1] == None: # If there are "empty boxes"
            # get the position of the element to the left of the
            # first None
            position = self._data.index(None) - 1
            # Save said element
            last = self._data[position]
            # pop the last element
            self._data.pop(position)
            # return the value
            return (last)

        else: # If there are no empty boxes
            # Save last element
            last = self._data[-1]
            # Pop the element
            self._data.pop(-1)
            # Return the value
            return (last)

    # Remove a specific value from our deque
    def remove(self, element):
        # Get the position of the value we want to remove
        position = self._data.index(element)
        # Pop the value
        self._data.pop(position)

    # Return the first element in the deque
    def first(self):
        # If there are no elements in the deque
        if self._data[0] == None:
            return ("Empty Array")
        else: # If there are elements
            return (self._data[0]) # Return the first element

    # Return the last element in the deque
    def last(self):
        if self._data[0] == None: # If there are no elements in the deque
            return ("Empty Array")

        elif self._data[-1] != None: # If there are no "empty boxes"
            return (self._data[-1]) # Return the last element

        else: # If there are "empty boxes"
            # Return the element to the left of the first none
            return (self._data[self._data.index(None) - 1])