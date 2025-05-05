# COMMAND LINE SPACED REPETITION FLASHCARDS (with personality!)

Struggling to remember stuff? Especially the important things like the names of
each cast member in the hit US sitcom Eight is Enough, or maybe content for
exams, those are coming up, although I personally would rather forget that...

But, if remembering things is a struggle for you, then this app is for you!

This Python script is a cutting-edge, command-line flashcard app. Remember
those? Yeah, me neither. It uses "spaced repetition," which is a fancy way of
saying it'll nag you over varying periods of time until facts are literally
burned into your brain (or you rage quit and throw it in the trash - the code,
hopefully, not your computer).

You can load your own meticulously crafted flashcards, or use the sample ones if
you want to test your knowledge against the standard Year 6 curriculum. Choose
between a "standard" helper (boring!) or a "sassy" one, because you might
remember better with a study tool that also mocks you (this has not been
scientifically tested!). The program saves your progress, relentlessly tracking
how often you forget things. It also calculates the relative ease of each card,
ensuring the things you stuff up the most are shown more often.

If you get an answer wrong, it politely asks if you want to see the correct one,
and, if available, gives a hint. It has some basic fuzzy logic to check if your
answer is close enough to the correct one, but don't get too cocky - it won't
let you off the hook that easily.

Stats are available to show how many cards you have left to review, and how many
you have left to learn. You can also see your overall statistics for the
flashcard deck, including the number of cards due today, the average ease
factor, and a breakdown of intervals.

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
