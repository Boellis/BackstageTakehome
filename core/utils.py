def calculate_difference(n: int) -> int:
    """
    Returns the difference between:
    1. The square of the sum of the first n natural numbers, and
    2. The sum of the squares of the first n natural numbers.
    """
    sum_of_squares: int = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum: int = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares
