# TO DO: Implement GUI

# Program to simulate a magic 8-ball.

# Magic 8-ball is a fortune game in which you enter a question and the system
# gives back an answer.
import random    
import time

# List holding predefined answers.
answers = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',      
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',           
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]

def main():
    # Flag for if we want to quit or not.
    is_quit = 'n'  

    # Getting the questions and giving back answers.
    while is_quit != 'y':
        input('\nEnter your question: ')
        
        print("thinking....")
        # Causes the system to sleep for 3 seconds.
        time.sleep(3)
        
        answer = get_answer()
        print(answer)

        is_quit = input("Do you want to quit(y for yes, anything else for no): ")

# Function returns a random answer from the above list of answers.
def get_answer():
    answer_number = random.randint(0, len(answers) - 1)

    return answers[answer_number]

# Calling main function.
main()