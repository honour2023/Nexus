# Given a year, report if it is a leap year.
# The tricky thing here is that a leap year in the Gregorian calendar occurs:
# 1 on every year that is evenly divisible by 4
# 2 except every year that is evenly divisible by 100
# 3 unless the year is also evenly divisible by 400


class Leap_Year:
    def __init__(self):
        self.year = int(input("Enter a year to check: "))
        if self.year%4== 0:
            print("" + "is a leapyear")

        else:
            print("" + "is not a leap year")

Year = Leap_Year()