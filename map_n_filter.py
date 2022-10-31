numbers = [1, 2, 3, 4, 5]

# creating new list which have square of only even numbers
squared_num = list(map(lambda x:x**2 if x%2==0 else x, numbers))
print(squared_num)

# creating new list which have sum of corresponding elements
num_1 = [4, 5, 6]
num_2 = [1, 2, 3]
result = list(map(lambda n1,n2: n1+n2, num_1, num_2))
print(result)

# filtering even numbers from the list
even_numbers = list(filter(lambda x:x%2==0, numbers))
print(even_numbers)