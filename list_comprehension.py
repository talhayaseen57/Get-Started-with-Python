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