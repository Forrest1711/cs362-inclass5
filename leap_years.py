year = input("Give me a year and I'll tell you if it's a leap year: ")

def leap_years(n):
    if n % 4 == 0:
        if n % 100 != 0:
            print("leap year!")
        elif n % 400 == 0:
            print("that's a leap year!")
        else:
            print("that's not a leap year")

leap_years(year)