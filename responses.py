import random

PERSONALITY = 'standard' # default personality

RESPONSES = {
        'standard': {
            'positive': [
                "Great job! You're absolutely right!", "Fantastic! You nailed it!",
                "Excellent! You're a star!", "Perfect! Keep up the amazing work!",
                "Correct! You're on fire!", "Wonderful! You're doing great!",
                "Good on ya! Spot on!", "Beauty! You got it!", "Too easy! Well done!",
                 "Nice one, mate!", "Couldn't have said it better myself!"
            ],
            'almost': [
                "Almost there! Just a little bit more.", "So close! Try again.",
                "You're on the right track! Keep thinking.", "Nearly perfect! Give it another shot.",
                "Good attempt! You're getting closer.",
                "Give it another crack!", "Nearly got it!", "Close, but no cigar!",
                "Just a smidge off!", "Keep at it, you're nearly there!"
            ],
            'negative': [
                "Not quite! Let's try that again.", "That's incorrect. Review the material.",
                "Oops! Give it another shot.", "Incorrect. Don't give up!",
                "Not exactly. Let's try a different approach.", "Nah, mate, try again.",
                "That's not it, give it another go.", "Bit off the mark there.",
                "Have another think about that one.",
                "Not quite right, keep trying!"
            ],
            'hints': [
                "Here's a hint: Think about...", "Consider this: ...",
                "A little help: Remember that...", "Perhaps this will jog your memory: ...",
                "Try thinking about... It might help!", "Have a squiz at this:",
                "Reckon this might help:", "Maybe this clue will point you in the right direction:",
                "How about this pointer:", "Let's nudge you towards the answer:"
            ]
        },
        'sassy': {
            'positive': [
                "Well, look who finally got one right.", "Took you long enough.",
                "Did you cheat? Just kidding... mostly.", "Congrats, genius.",
                "Finally, a correct answer. Don't get used to it.", "About bloody time!",
                "Finally dragged yourself over the line, eh?", "Well, stone the crows, you got it.",
                "Don't get your knickers in a twist, but you're right.", "Managed that one, did ya?",
                "Miracles happen, I guess. You got it right."
            ],
            'almost': [
                "Almost... but still a failure.", "So close, yet so far from success.",
                "Nice try, but you still messed up.", "You almost had it, almost.",
                "Better luck next time... maybe.", "Yeah, nah. Almost.",
                "Close, but still cactus.", "Fell short again, mate.",
                "Tried hard, failed harder.", "Not quite the full quid, are ya?",
                "Close only counts in horseshoes and hand grenades."
            ],
            'negative': [
                "Seriously? That's your answer?", "Are you even trying?",
                "Wow, that was impressively wrong.", "Maybe you should just give up.",
                "I'm starting to think you're doing this on purpose.", "Pull the other one, it's got bells on it.",
                "Are you fair dinkum?", "You're having a laugh, right?",
                "Flat out wrong, mate.", "Wow, that's a shocker.",
                "Did you even read the question?"
            ],
            'hints': [
                "Here's a hint: It's not what you said. But maybe this will save me from your stupidity: ",
                "Try harder. Or don't, I don't care. But you should. Here's a hint: ",
                "Hint: It's probably the opposite of what you're thinking. Consider this: ",
                "Here's a hint: You're hopeless. Lol jks, in all seriousness, does this help? ",
                "Try to remember... or just guess. I don't care. Here's a hint: ",
                "Here's a hint, try not to stuff it up this time:", "Maybe use your noggin? Here's a clue:",
                "Struggling, eh? Here's something to chew on:",
                "Alright, alright, settle down. Maybe this hint will stop the whining:"
            ]
        }
    }

def set_personality(personality):
    global PERSONALITY
    if personality in ['standard', 'sassy']:
        PERSONALITY = personality    

def generate_response(feedback):
    
    style = RESPONSES.get(PERSONALITY, RESPONSES['standard'])

    if feedback == "correct":
        return random.choice(style['positive'])
    elif feedback == 'almost':
        return random.choice(style['almost'])
    elif feedback == "wrong":
        return random.choice(style['negative'])
    else:
        return f'{random.choice(style['hints']).strip()} {feedback}'