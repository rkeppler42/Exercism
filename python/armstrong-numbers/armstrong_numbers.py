"""
Function to determine if a given number is an Armstrong Number.
"""

def is_armstrong_number(number: int) -> bool:
    """
    :param number: int - A number that should be tested to be an Armstrong Number.
    :return: bool - Returns True if Armstrong Number and False otherwise.
    """

    n_of_digits = len(str(number))
    total_number = sum(int(digit) ** n_of_digits for digit in str(number))

    return number == total_number
