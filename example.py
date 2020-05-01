def hello():
    print('Howdy')
    print('Howdy!!!')
    print('Hello there')

hello()
hello()
hello()

def hello_2(name):
    print('Hello ' + name)
hello_2('Alice')
hello_2('Bob')

def plus_one(number):
    return number + 1
new_number = plus_one(5)
print(plus_one(5))

print('hello', end='')
print('World')