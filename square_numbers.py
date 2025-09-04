def square_filter(start, end):
    numbers = list(range(start, end + 1))             # using list()
    squares = list(map(lambda n: n**2, numbers))      # squares using map + list()

    even_squares = list(filter(lambda x: x % 2 == 0, squares))  # filter evens
    odd_squares = list(filter(lambda x: x % 2 != 0, squares))   # filter odds

    print("Numbers:", numbers)
    print("Squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)


# Example usage
square_filter(1, 10)
