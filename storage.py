import json
from flashcards import Flashcard, FlashcardDeck
import datetime

def load_deck(filename):
    deck = FlashcardDeck()
    with open(filename, "r") as f:
        data = json.load(f)
        for item in data:
            card = Flashcard(
                item['question'],
                item['answer'],
                item.get('hints', []),
                item.get('due_date', str(datetime.date.today())),
                item.get('ease_factor', 2.5)
            )
            deck.cards.append(card)
    return deck

def save_deck(deck, filename):
    data = [{
        "question": c.question,
        "answer": c.answer,
        "hints": c.hints,
        "due_date": c.due_date,
        "ease_factor": c.ease_factor
    } for c in deck.cards]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
