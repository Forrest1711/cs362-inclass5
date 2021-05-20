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
