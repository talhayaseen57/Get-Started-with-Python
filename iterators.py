class Even:
    """
    A function which produces even numbers 
    till the given last_number one by one
    """

    def __init__(self, last_number):
        self.number = 2
        self.last_number = last_number
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number <= self.last_number:
            result = self.number
            self.number += 2
            return result
        else:
            raise StopIteration


numbers = Even(21)
values = iter(numbers)

while(True):
    try:
        element = next(values)
        print(element)
    except StopIteration:
        break
