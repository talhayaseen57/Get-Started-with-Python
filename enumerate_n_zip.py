import time

names = ['Anna', 'Alexa', 'Marine']
marks = [98, 56, 89]

for count, name in enumerate(names):
    if name == 'Marine':
        print("Using enumerate....")
        print(f'{name} got {marks[count]} marks.\n\n')
        break

for name, mark in zip(names, marks):
    if name == 'Alexa':
        print("Using zip() function....")
        print(f'{name} got {mark} marks.\n\n')
        break