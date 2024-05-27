"""
Function to calculate the number of steps taken to get to number 1 through Collatz Conjecture
"""

def steps(number: int) -> int:
    """

    :param number: int - initial number to go through Collatz Conjecture.
    :return: int - numbers of steps taken to get to number 1 through Collatz Conjecture.
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step: int = 0

    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        step += 1

    return step
