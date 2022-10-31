"""
hot key for commenting line to a code:
-> Ctrl + /
"""

# def mult_by_2(n):
#     return n*2
mult_by_2 = lambda x: x*2
print(mult_by_2(15))

# sorting a list of strings according to length of string
names = ['Talha Yaseen', 'Selin Koles', 'Hassan Subhani', 'Umme Bebba', 'Zubair']
names.sort(key= lambda x: len(x))
print(names)