# COMMAND LINE SPACED REPETITION FLASHCARDS (with personality!)

## To Get Started

1. Clone the repository
2. Open the terminal and navigate to the directory
3. Run `python3 main.py` to start the program (you must have a recent version of
   Python installed)
4. Follow the prompts to load a deck of flashcards
   - Flashcards should be a JSON file with the following format:
   ```json
   [
       {
       "question": "Author of '1984'?",
       "answer": "george orwell",
       "hints": ["Wrote 'Animal Farm'", "English novelist"]
       },
       ...
   ]
   ```
   - To test the app there is a sample file which will automatically load if you
     answer 'n' to the following prompt:
     `📂 Do you have a JSON file with your flashcards? (y/n):`
5. Choose your personality. You can choose from `standard/sassy`. Be warned,
   `sassy` mode is very cheeky!
6. **Start answering questions.** Your progress will be saved, and you can
   continue later
