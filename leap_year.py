from typing import Type


def leap_year(n):
    if n % 4 == 0:
        if n % 100 != 0:
            return True
        elif n % 400 == 0:
            return True
        else:
            return False
    else:
        return False


leap_year(-36)
leap_year(1984)
leap_year(1998)
leap_year(2016)
leap_year(2021)
leap_year(99999)
