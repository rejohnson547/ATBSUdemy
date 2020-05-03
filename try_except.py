# 05/02/2020

def div42by(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many dogs do you have?')
num_dogs = input()
try:
    if int(num_dogs) >= 4:
        print('That is a lot of dogs.')
    else:
        print('That is not that many dogs.')
except ValueError:
    print('You did not enter a number.')