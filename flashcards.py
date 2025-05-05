import random
import difflib
import datetime

class Flashcard:
    def __init__(self, question, answer, hints=None, due_date=None, ease_factor=2.5):
        self.question = question
        self.answer = answer.lower()
        self.hints = hints or []
        self.attempts = 0
        self.correct_attempts = 0
        self.due_date = due_date if due_date else str(datetime.date.today())
        self.ease_factor = ease_factor

    def check_answer(self, user_input):
        """
        Check the user's answer against the correct answer.

        returns 'correct', 'almost', or a hint.
        """
        self.attempts += 1
        user_input = user_input.lower()
        if user_input == self.answer:
            self.correct_attempts += 1
            return 'correct'
        # Use difflib to check for close matches
        similarity_ratio = difflib.SequenceMatcher(None, user_input, self.answer).ratio()
        if similarity_ratio >= 0.8:
            return 'almost'
        # Another check for potentially correct but not exact answers
        if user_input in self.answer or self.answer in user_input:
            return 'almost'
        # Incorrect, provide a hint
        hint = random.choice(self.hints) if self.hints else "wrong"
        return hint

    def update_due_date(self, correct):
        today = datetime.date.today()
        due_date = datetime.datetime.strptime(self.due_date, "%Y-%m-%d").date()
        interval = (due_date - today).days

        if correct:
            self.correct_attempts += 1
            if self.correct_attempts > 1:
                interval = max(1, int(interval * self.ease_factor))
                self.ease_factor += (0.1 - (5 - self.correct_attempts) * (0.08 + (5 - self.correct_attempts) * 0.02))
                self.ease_factor = max(1.3, self.ease_factor)
        else:
            self.correct_attempts = 0
            interval = 1
            self.ease_factor = max(1.3, self.ease_factor - 0.2)

        self.due_date = str(today + datetime.timedelta(days=interval))

class FlashcardDeck:
    def __init__(self):
        self.cards = []
        self.current_index = 0

    def get_next_card(self):
        today = datetime.date.today()
        due_cards = [card for card in self.cards if datetime.datetime.strptime(card.due_date, "%Y-%m-%d").date() <= today]
        if due_cards:
            return random.choice(due_cards)
        
        return None

    def reset_cards(self):
        for card in self.cards:
            card.attempts = 0
            card.correct_attempts = 0
            card.due_date = str(datetime.date.today())
            card.ease_factor = 2.5

    def update_card_status(self, card, correct):
        card.update_due_date(correct)

    def get_due_card_count(self):
        """Returns the number of cards due for review (due_date <= today)."""
        today = datetime.date.today()
        return sum(1 for card in self.cards if datetime.datetime.strptime(card.due_date, "%Y-%m-%d").date() <= today)

    def get_stats(self):
        """Returns a dictionary of statistics about the flashcard deck."""
        total_cards = len(self.cards)
        due_cards = self.get_due_card_count()

        interval_counts = {}
        today = datetime.date.today()
        for card in self.cards:
            due_date = datetime.datetime.strptime(card.due_date, "%Y-%m-%d").date()
            interval = (due_date - today).days
            if interval not in interval_counts:
                interval_counts[interval] = 0
            interval_counts[interval] += 1

        total_ease = sum(card.ease_factor for card in self.cards)
        average_ease_factor = total_ease / total_cards if total_cards > 0 else 0

        return {
            'total_cards': total_cards,
            'due_cards': due_cards,
            'interval_counts': interval_counts,
            'average_ease_factor': average_ease_factor,
        }
