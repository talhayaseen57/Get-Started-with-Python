def generate_fiboonacci(last_number):
    """
    Generates fibonacci series till 
    the given last_number
    """

    n1 = 0
    n2 = 1
    while n2 <= last_number:
        yield n1
        n1, n2 = n2, n1+n2


fab_seq = generate_fiboonacci(30)
while True:
    try:
        digit = next(fab_seq)
        print(digit)
    except StopIteration:
        break