import random

correct = 'you guessed correctly!'
too_low = 'Too Low!!'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    
    while True:
        try:
            return int(input('Guess the secret number? '))
        except ValueError:
            print("Your entry was not an integer number.")
    

def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    play_again = "Yes"
    while play_again != 'stop':
        (low, high) = configure_range()
        low = input("Choose the low number for the range: ")
        high = input("Choose the high number for the range: ")
        secret = generate_secret(low, high)
        cntr = 0
        while True:
            cntr = cntr + 1
            guess = get_guess()
            result = check_guess(guess, secret)
            print(result)

            if result == correct:
                print("It took you: ",cntr, "guesses.")
                break
        play_again = input("Press enter to play again or type 'Stop' to end the game: ")
        play_again = play_again.lower()

if __name__ == '__main__':
    main()
