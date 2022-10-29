def generator(first_number, last_number, step):
    number = first_number

    while number <= last_number:
        yield number
        number += step


numbers = generator(0, 38, 2)
while True:
    try:
        digit = next(numbers)
        print(digit)
    except StopIteration:
        break
