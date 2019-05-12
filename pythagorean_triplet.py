# Program to check if a given triplet is a pythagorean triplet.

# A pythagorean triplet is any triplet (a, b, c) that satisfes a ** 2 + b ** 2 == c ** 2

# Main body of the program.
def main():
    # flag for if we need to check for other values.
    should_continue = 'y'

    while should_continue == 'y':
        # Getting the sides from the user
        sides = get_sides()

        # Checking if the given triplet is a pythagorean triplet
        pythagorean_triplet_status = is_pythagorean_triplet(sides)

        if pythagorean_triplet_status:
            print("The given sides form a pythagorean triplet.")
        else:
            print("The given sides do not form a pythagorean triplet.")

        should_continue = input("Do you want to enter more vales(y for yes, anything else for no): ")

# Boolean function which checks if a given triplet is a pythagorean triplet.
def is_pythagorean_triplet(sides):
    # need to sort since we need to check if the sum of squares the smallest two 
    # numbers is equal to the square of the largest number.
    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    
    return False

# Function gets the sides from the user.
# Does exception handling too.
def get_sides():
    sides = []
    
    for side_number in range(1,4):
        incorrect_input = True

        while incorrect_input:
            try:
                side = float(input("Enter the side " + str(side_number) + ": "))
                incorrect_input = False
            except ValueError:
                print("Error, Enter a valid value.")
        
        sides.append(side)

    return sides

main()