🕹️ Hangman Game 
This is a simple command-line Hangman game written in Python. The game randomly selects a word from a list provided in a words.py file and allows the player to guess letters. After a number of incorrect guesses, the game ends with a loss.

📂 Project Structure
bash
Copy
Edit
hangman/
├── main.py        # Main game file
├── words.py       # Python file containing the list of words

🧠 Features
Randomly selects a word from the list in words.py

Displays hangman figure in stages as guesses fail

Shows one starting letter as a hint

No display of guessed letters

Game ends when final stage of hangman is drawn

🚀 How to Run

Make sure you have Python installed. You can check by running:

python --version

Navigate to the directory containing main.py and words.py:

cd path/to/hangman

Run the game:

python main.py

🛠 Requirements
Python 3.x (no external libraries required)
