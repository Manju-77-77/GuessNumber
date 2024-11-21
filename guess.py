import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.text_field = tk.Entry(root, width=10)
        self.text_field.pack(pady=5)
        
        self.button = tk.Button(root, text="Guess!", command=self.check_guess)
        self.button.pack(pady=10)

        self.random_number = random.randint(1, 100)

    def check_guess(self):
        try:
            guess = int(self.text_field.get())  # Convert user input to an integer
            if guess < 1 or guess > 100:
                self.label.config(text="Invalid guess. Guess a number between 1 and 100:")
            elif guess < self.random_number:
                self.label.config(text="Too low. Guess again:")
            elif guess > self.random_number:
                self.label.config(text="Too high. Guess again:")
            else:
                self.label.config(text=f"You guessed it! The number was {self.random_number}.")
                self.button.config(state="disabled")  # Disable the button after a correct guess
        except ValueError:
            self.label.config(text="Invalid guess. Enter a number between 1 and 100.")
        
        # Clear the text field for the next guess
        self.text_field.delete(0, tk.END)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = GuessingGame(root)  # Instantiate the game with the window
    root.mainloop()  # Start the main event loop
