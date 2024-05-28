"""
Function to determine if a given year is a leap year.
"""

def leap_year(year: int) -> bool:

    """
    :param year: int - given year
    :return: bool - True if it is a leap year, False if not.
    """

    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)
