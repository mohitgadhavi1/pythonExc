'''
Iterators:
Iterators are objects that implement the
 __iter__() and __next__() methods to allow 
 for iterating over a sequence of data. 
 The __iter__() method returns the iterator 
 object itself and the __next__() method 
 returns the next value in the sequence.
'''

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Using the iterator to print the values of a list
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)
for i in my_iterator:
    print(i)
