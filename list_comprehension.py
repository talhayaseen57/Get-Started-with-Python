from math import sqrt

list_1 = [i*i for i in range(1,6)]
print(list_1)

numbers = [49, 64, 81, 100, 121]
list_2 = [sqrt(n) for n in numbers if n%2!=0]
print(list_2)

team_1 = ['Talha', 'Yaseen', 'Zafar']
team_2 = ['Selin', 'Koles']
list_3 = [(x, y) for x in team_2 for y in team_1]
print(list_3)

matrix = [[1, 2, 10], [3, 4, 11], [5, 6, 12], [7, 8, 13]]
transpose =  [[row[i] for row in matrix] for i in range(3)]
print(transpose)

numbers = [1, 2, 3, 4, 5]
square_dict = {num: num**2 for num in numbers}
print(square_dict)

old_price = {'milk': 1.5, 'egg': 2.5, 'bread': 3.0}
new_price = {key: value*1.5 if value>=2.0 else value for (key, value) in old_price.items()}
print(new_price)