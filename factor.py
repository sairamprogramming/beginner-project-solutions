# Define a function that creates a list of all the numbers that are factors of the user's number.
# For example, if the function is called factor, factor(36) should return [1, 2, 3, 4, 6, 9, 12, 18, 36].
# The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
# Remember to consider negative numbers as well as 0.
# Bonus:
#     Have the program print the factors of the users number in a comma separated string, without a comma after the last number, and without the brackets of a Python list.
#     If the user's number is prime, note it.


# This is the main function of the program.
def main():
    print("This program gives you the list of all positive factors of a number!\n\n")

    try:        
        number = int(input("Enter a number: "))
        factors_list = factor(number)

        print_factors(factors_list)
    except:
        print("Error: Entered Invalid Input!")

    

# Prints out the appropriate factor list, also takes care of special case.
def print_factors(lst):
    if lst[0] == 0:
        print("Contains zero, which has a infinite amount of factors.")
    elif len(lst) == 2:
        print_with_commas(lst)
        print("The given number is a prime number!")
    else:
        print_with_commas(lst)        

# Prints out a list of numbers with commas and last element with and.
def print_with_commas(lst):
    print("Factors:", end=" ")
    for i in range(0, len(lst) - 1):
        print(lst[i], end = ', ')
    print("and", lst[len(lst) - 1])                

# Function finds the factors of a number, returns all the factors in 
# the form of a list.
def factor(n):
    if n == 0:
        return [0]

    # Taking care of negative integers.
    n = abs(n)    
    factors = []
    for value in range(1, n+1):
        if n % value == 0:
            factors.append(value)

    return factors            

# Call the main function.
main()    
