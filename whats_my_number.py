# Between 1 and 1000, there is only 1 number that meets the following criteria:

#     The number has two or more digits.
#     The number is prime.
#     The number does NOT contain a 1 or 7 in it.
#     The sum of all of the digits is less than or equal to 10.
#     The first two digits add up to be odd.
#     The second to last digit is even and greater than 1.
#     The last digit is equal to how many digits are in the number.

def main():
    numbers = list(range(1,1000 + 1))
    temp = []

    # Numbers have two or more digits
    numbers = numbers[9:]

    # The sum of all digits is less than or equal to 10.
    for number in numbers:
        if sum([int(x) for x in str(number)]) <= 10:
            temp.append(number)
    # print(temp)
    numbers = temp
    temp = []

    # The sum of the first two digits is odd.
    for number in numbers:
        number = str(number)
        digit_sum_2 = int(number[0]) + int(number[1])
        if digit_sum_2 % 2 != 0:
            temp.append(number)

    
    numbers = temp
    temp = []            

    # The second to last digit is even and greater than 1.
    for number in numbers:
        number = str(number)
        if int(number[-2]) % 2 == 0 and int(number[-2]) > 1:
            temp.append(number)
    
    numbers = temp
    temp = []

    # The last digit is equal to how many digits are in the number.
    for number in numbers:
        number = str(number)
        digit_sum = len(number)
        if digit_sum == int(number[-1]):
            temp.append(number)
    
    numbers = temp
    temp = []        

    # The number does NOT contain a 1 or 7 in it.
    for number in numbers:
        number = str(number)
        lst = list(number)
        if '1' not in lst and '7' not in lst:
            temp.append(int(number))
    # print(temp)
    numbers = temp
    temp = []

    # The number is prime.                
    for number in numbers:
        is_prime = True

        if number % 2 == 0:
            continue

        for i in range(3,number, 2):
            if number % i == 0:
                is_prime = False
                break              

        if is_prime:
            temp.append(number)

    numbers = temp
    temp = []    

    # The resultant number.                        
    print(numbers[0])

# Calling the main function.
main()    