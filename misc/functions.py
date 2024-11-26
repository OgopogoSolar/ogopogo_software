import random

def number_generator(count, start=0, end=100):
    """
    Generate a list of random values.

    :param count: Number of random values to generate
    :param start: The lower bound of the random values (inclusive)
    :param end: The upper bound of the random values (inclusive)
    :return: List of random values
    """
    return [random.randint(start, end) for _ in range(count)]