def reverse_digits(n):
    """
    Function to reverse the digits of a number.
    """
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    return rev


def is_adam_number(n):
    """
    Function to check if a number is an Adam number or not.
    """
    square = n * n
    reverse_square = reverse_digits(square)
    reverse_of_reverse = reverse_digits(reverse_square)

    return square == reverse_of_reverse


# Test the function
number = int(input("Enter a number: "))
if is_adam_number(number):
    print(number, "is an Adam number.")
else:
    print(number, "is not an Adam number.")
