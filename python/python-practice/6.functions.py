
def say_hi():
  print("Hi!")

say_hi()


def say_hello(name = 'everyone'):
  print("Hi {} !".format(name))

say_hello()
say_hello('ABC')
say_hello('DEF')

def name(first, last):
  print('Hi {} {}!'.format(first, last))

name('John', 'Doe')
name(last= 'Doe', first = 'John')