def kaprekar_routine(starting_number):
    iteration_count = 0
    
    while iteration_count < 8:
        if starting_number == 6174:
            print("Kaprekar's routine reached 6174!")
            print("Number of iterations:", iteration_count)
            return
        
        # Convert the number to a list of digits
        digits = [int(digit) for digit in str(starting_number)]
        
        # Ensure the list has 4 digits by adding leading zeros if necessary
        while len(digits) < 4:
            digits.insert(0, 0)

        # Sort the digits in ascending and descending order
        ascending_number = int(''.join(map(str, sorted(digits))))
        descending_number = int(''.join(map(str, sorted(digits, reverse=True))))

        # Calculate the next number in the sequence
        starting_number = descending_number - ascending_number
        iteration_count += 1
        print(f"{descending_number} - {ascending_number} = {starting_number}")

    print("Kaprekar's routine did not reach 6174 after 7 iterations.")

# Example usage
start_number = input("Enter a four digit number : ")
kaprekar_routine(start_number)
