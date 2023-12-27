import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
  O |
    |
    |
   ===''', '''
+---+
  O |
  | |
    |
   ===''', '''
+---+
  O |
 /| |
    |
   ===''', '''
+---+
  O |
 /|\|
    |
   ===''', '''
+---+
  O |
 /|\|
 /  |
   ===''', '''
+---+
  O |
 /|\|
 / \|
   ===''', '''
+---+
 [O |
 /|\|
 / \|
   ===''', '''
+---+
 [O]|
 /|\|
 / \|
   ===''']

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def get_random_word(word_dict):
    """This function returns a random string from the passed dictionary of lists of strings and its key."""
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]

def display_board(missed_letters, correct_letters, secret_word):
    """Display the current state of the board and correctly and incorrectly guessed letters"""
    print(f"{HANGMAN_PICS[len(missed_letters)]}\n")

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()

def get_guess(already_guessed):
    """
    This function makes sure the player entered a single letter and not something else,
    and returns the letter the player entered.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    """
     This function returns True if the player wants to play again;
     otherwise, it returns False.
    """
    return input("Do you want to play again? (yes or no) ").lower().startswith('y')

print("H A N G M A N")

difficulty = ""
while difficulty not in 'EMH':
    difficulty = input("Enter difficulty: E - Easy, M - Medium, H - Hard").upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missed_letters = ""
correct_letters = ""
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print(f"The secret word is in the set: {secret_set}.")
    display_board(missed_letters, correct_letters, secret_word)

    # Let the player enter a letter.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess

        # Check if the player has won.
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f"Yes! The secret word is {secret_word}! You have won!")
            game_is_done = True
    else:
        missed_letters += guess

        # Check if player has guessed too many times and lost.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print(f"You have run out of guesses!\nAfter {str(len(missed_letters))} missed guesses"
            f" and {str(len(correct_letters))} correct guesses, the word was {secret_word}")
            game_is_done = True

    # Ask the player if they want to play again (but only if the game is done).
    if game_is_done:
        if play_again():
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break
