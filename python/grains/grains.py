"""Functions to calculate the number of grains per square and the total given that
the number of grains double with each square in a board of chess.
"""


def square(number: int) -> int:
    """

    :param number: int - number of grains given the number of the square.
    :return: int - total number of grains in the nth square.
    """

    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << number - 1


def total() -> int:
    """

    :return: int - total number of grains in a board of chess.
    """

    total_of_grains: int

    for n in range(65):
        total_of_grains = 1 << n

    return total_of_grains - 1

    # return 1 * (1 - 2 ** 64) / (1 - 2)
    # return 1 * (1 - (1 << 64)) / (1 - 2)
