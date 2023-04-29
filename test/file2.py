import os
print('hello-world!!!')
my_dict = {'a': 1, 'b': 2}
print(my_dict['a'])

class Worker:
    def __init__(self, name):
        self.name = name

    def writeName(self):
        print(self.name)

john = Worker('John')
ania = Worker('Ania')

john.writeName()
ania.writeName()