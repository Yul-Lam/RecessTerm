def get_day_of_week(day_number):
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number. Please enter a number between 1 and 7."

def main():
    try:
        day_number = int(input("Enter a day number (1-7): "))
        day_name = get_day_of_week(day_number)
        print(f"Day {day_number}: {day_name}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
