from flashcards import FlashcardDeck
from responses import generate_response, set_personality
import storage
import os

def main():
    print("\n🤖 Welcome to the Conversational Flashcard System!")
    print("\n🤖 This works on spaced repetition. Your progress will be saved along the way.")
    print("\n🤖 Comeback each day to refresh yourself on your cards.\n")
    
    use_json = input("📂 Do you have a JSON file with your flashcards? (y/n): ").strip().lower()
    deck = FlashcardDeck()
    filename = "flashcards.json"

    if use_json == 'y':
        json_path = input("🗃️ Please enter the JSON file path: ").strip()
        filename = json_path
        if os.path.exists(json_path):
            try:
                deck = storage.load_deck(json_path)
                print("✅ Flashcards loaded successfully!\n")
            except Exception as e:
                print(f"❌ Error loading flashcards: {e}")
                print("❌ Loading sample flashcards instead.\n")
                deck = storage.load_deck("sample_flashcards.json")
                filename = "sample_flashcards.json"
        else:
            print("❌ File not found. Loading sample flashcards instead.\n")
            deck = storage.load_deck("sample_flashcards.json")
            filename = "sample_flashcards.json"
    else:
        print("📚 Loading sample flashcards...\n")
        deck = storage.load_deck("sample_flashcards.json")
        filename = "sample_flashcards.json"
    
    clear_progress = input("🧹 Clear saved progress and start from the beginning? (y/n): ").strip().lower()
    if clear_progress == 'y':
        deck.reset_cards()
        print("🔄 Progress cleared.")

    # Personality Selection
    personality = input("\n😇 Choose your helper's personality (standard/sassy): ").strip().lower()
    set_personality(personality)

    print("\n🎯 Let's start!\nType:\n'exit' to leave the program,\n'progress' to see your daily progress, or\n'stats' to see your overall statistics for this flashcard deck.")

    while True:
        card = deck.get_next_card()
        if not card:
            print("\n🎉 Congratulations! You've reviewed all cards for today. Come back tomorrow!")
            break

        print(f"\n🔖 {card.question}")
        user_answer = input("📝 Your answer: ").strip()

        user_answer = user_answer.lower()

        if user_answer == 'exit':
            print("\n👋 Session ended. See you next time!")
            break

        elif user_answer == 'progress':
            due_count = deck.get_due_card_count()
            print(f"📊 You have {due_count} cards left to review today.")
            continue

        elif user_answer == 'stats':
            stats = deck.get_stats()
            print("📈 Flashcard Deck Statistics:")
            print(f"  Total Cards: {stats['total_cards']}")
            print(f"  Cards Due Today: {stats['due_cards']}")
            print("  Interval Breakdown:")
            for interval, count in stats['interval_counts'].items():
                print(f"    Interval {interval}: {count} cards")
            print(f"  Average Ease Factor: {stats['average_ease_factor']:.2f}")
            continue

        feedback = card.check_answer(user_answer)
        response = generate_response(feedback)
        if feedback == 'correct':
            print(f"✅ {response}")
        elif feedback == 'almost':
            print(f"🤏 {response}")
        else:
            print(f"❌ {response}")
        
        if feedback != 'correct':
            show_answer = input("👀 Show answer? (y/n): ").strip().lower()
            if show_answer == 'y':
                print(f"💡 The correct answer is: {card.answer}")

        deck.update_card_status(card, feedback == 'correct')

        # Save progress after each card review
        storage.save_deck(deck, filename)

if __name__ == "__main__":
    main()
