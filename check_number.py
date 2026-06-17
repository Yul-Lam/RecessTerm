def main():
    try:
        value = float(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if value > 0:
        print("The number is positive.")
    elif value < 0:
        print("The number is negative.")
    else:
        print("The number is zero, which is neither positive nor negative.")

if __name__ == "__main__":
    main()
