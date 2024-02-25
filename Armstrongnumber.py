def is_armstrong_number(n):
    """
    Function to check if a number is an Armstrong number or not.
    """
    # Convert the number to a string to determine the number of digits
    num_str = str(n)
    num_digits = len(num_str)

    # Calculate the sum of the digits raised to the power of the number of digits
    digit_sum = 0
    for digit in num_str:
        digit_sum += int(digit) ** num_digits

    return n == digit_sum


# Test the function
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
