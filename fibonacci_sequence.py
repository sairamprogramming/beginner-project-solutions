# In complete

# Fibonacci Sequence

# Define a function that allows the user to find the value of the nth term in the sequence.
# To make sure you've written your function correctly, test the first 10 numbers of the sequence.
# You can assume either that the first two terms are 0 and 1 or that they are both 1.
# There are two methods you can employ to solve the problem. One way is to solve it using a loop and the other way is to use recursion.
# Try implementing a solution using both methods.

def main():
    correct_input = True

    try:
        number = int(input('Enter a number: '))
    except:
        print('Error, Invalid input.')
        correct_input = False

    if correct_input:
        fibonacci_term = loop_fibonacci(number)

    print(fibonacci_term)

def loop_fibonacci(number):
    a = 0
    b = 1

    while b <= number:
        temp = a
        a = b
        b = b + a

        