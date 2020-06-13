# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 87?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 81?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 84?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 82?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 83?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 83

print("Please think of a number between 0 and 100!")

game_playing = True
guess = 50
max_number = 100
min_number = 0
message = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."


while game_playing:
    print("Is your secret number {}?".format(guess))
    user_input = input(message)

    if user_input == 'h':
        max_number = guess
        guess = (max_number + min_number) / 2
        print(guess)
        guess = round(guess)
    elif user_input == 'l':
        min_number = guess
        guess = (max_number + min_number) / 2
        print(guess)
        guess = round(guess)
    elif user_input == 'c':
        print("Game over. Your secret number was:{}".format(guess))
        game_playing = False
    else:
        print("Invalid Input")