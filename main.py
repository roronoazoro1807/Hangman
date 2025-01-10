import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo)

chosen_word = random.choice(word_list)
print(f"(DEBUG: The chosen word is {chosen_word})")  # Remove this in production

placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters or guess in wrong_letters:
        print(f"You've already guessed '{guess}'. Try another letter!")
        continue

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        if guess in wrong_letters:
            print(f"You've already guessed '{guess}' incorrectly. It still doesn't count!")
        else:
            wrong_letters.append(guess)
            lives -= 1
            print(f"You guessed '{guess}', which is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS '{chosen_word.upper()}'! YOU LOSE ***********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[lives])
