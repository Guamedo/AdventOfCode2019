from day1 import day1, day1_star
from day2 import day2, day2_star
from day3 import day3, day3_star
from day4 import day4, day4_star
from day5 import day5, day5_star
from day6 import day6, day6_star
from day7 import day7, day7_star
from day8 import day8, day8_star
from day9 import day9, day9_star


if __name__ == "__main__":
    day = int(input("Select a day:"))
    if day == 1:
        day1()
        day1_star()
    elif day == 2:
        day2()
        day2_star()
    elif day == 3:
        day3()
        day3_star()
    elif day == 4:
        day4()
        day4_star()
    elif day == 5:
        day5()
        day5_star()
    elif day == 6:
        day6()
        day6_star()
    elif day == 7:
        day7()
        print("Day 7* is not working yet")
        # day7_star()
    elif day == 8:
        day8()
        day8_star()
    elif day == 9:
        day9()
        day9_star()
    else:
        print(f"Day {day} is not done yet")