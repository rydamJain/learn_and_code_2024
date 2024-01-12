def get_digits(number):
    """Convert a number to a list of its digits."""
    return [int(digit) for digit in str(number)]

def add_leading_zeros(digits, target_length=4):
    """Ensure the list of digits has the specified length by adding leading zeros if necessary."""
    while len(digits) < target_length:
        digits.insert(0, 0)
    return digits

def sort_digits(digits, reverse=False):
    """Sort the digits in specified order."""
    return sorted(digits, reverse=reverse)

def join_digits(digits):
    """Join the digits to form a number."""
    return int(''.join(map(str, digits)))

def print_iteration_result(descending_number, ascending_number, next_number):
    """Print the result of each iteration in the specified format."""
    print(f"{descending_number} - {ascending_number} = {next_number}")

def kaprekar_routine(starting_number):
    """Perform Kaprekar's routine and print the results."""
    iteration_count = 0
    
    while iteration_count < 8:
        if starting_number == 6174:
            print("Kaprekar's routine reached 6174!")
            print("Number of iterations:", iteration_count)
            return

        digits = get_digits(starting_number)
        digits_with_zeros = add_leading_zeros(digits)
    
        ascending_number = join_digits(sort_digits(digits_with_zeros))
        descending_number = join_digits(sort_digits(digits_with_zeros, reverse=True))

        next_number = descending_number - ascending_number
        iteration_count += 1
        print_iteration_result(descending_number, ascending_number, next_number)
        starting_number = next_number

    print("Kaprekar's routine did not reach 6174 after 7 iterations.")

# Example usage
start_number = int(input("Enter a four-digit number: "))
kaprekar_routine(start_number)
