
import random
import string

# create a class for the word guessing game
class WordGuessingGame:

    def __init__(self, max_lives=6):
        self.words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]

        self.max_lives = max_lives
        self.secret = random.choice(self.words)
        self.blanks = ["_" for _ in self.secret]
        self.lives = self.max_lives
        self.used_letters = set()

# create a method to get a letter
    def get_letter(self):
       #Ask the player to enter a valid letter."""

        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue

            return guess

#create a method to the letter in secret word
    def reveal_letters(self, letter):
        found_any = False

        for i, character in enumerate(self.secret):
            if character == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

#create a method to play the game
    def all_blanks_filled(self):
        return "_" not in self.blanks

#choice a method to display the current state of the guessed word.
    def display_word(self):
        print(" ".join(self.blanks))

    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret)} letters.")
        self.display_word()

        while True:
            guess = self.get_letter()
            self.used_letters.add(guess)

            if self.reveal_letters(guess):
                print("\nWell done, Nice job! You found a letter.")
                self.display_word()

                if self.all_blanks_filled():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret}")
                    print("GAME OVER")
                    break

            else:
                self.lives -= 1

                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                self.display_word()

                if self.lives <= 0:
                    print("\nOut of lives & Sad story!")
                    print(f"The word was: {self.secret}")
                    print("GAME OVER")
                    break

if __name__ == "__main__":
    game = WordGuessingGame()
    game.play()
