# Program to give lyrics to the song 99 bottles.

def main():
    # Initalizing the number of bottles
    bottles = 99
    
    # Looping through and printing the appropriate lyrics
    while bottles > 0:

        if bottles > 1:
            print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer.")
            bottles -= 1

            if bottles != 1:            
                print("Take one down and pass it around,", bottles, "bottles of beer on the wall.")
            # Have to use bottle instead of bottles when the total number of bottles is 1.
            elif bottles == 1:
                print("Take one down and pass it around,", bottles, "bottle of beer on the wall.")

        elif bottles == 1:
            print(bottles ,"bottle of beer on the wall,", bottles, "bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            bottles -= 1

        print()

    # Lyrics for no more bottles.
    print("No more bottles of beer on the wall, no more bottles of beer. ")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    
main()