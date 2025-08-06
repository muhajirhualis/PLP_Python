# 3. Random Joke Generator 🤣
# Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡


python_jokes = {
    "joke_1": {
        "setup": "Why did the Python developer go to therapy?",
        "punchline": "Because they had deep inheritance issues!"
    },
    "joke_2": {
        "setup": "Why don’t Python developers ever get lost?",
        "punchline": "Because they always follow the indent-ation!"
    },
    "joke_3": {
        "setup": "Why did the programmer quit their job?",
        "punchline": "They didn’t get arrays. (Get it? A raise!)"
    },
    "joke_4": {
        "setup": "Why is Python the most polite language?",
        "punchline": "Because it always follows PEP — Python Enhancement Proposals (or 'Please Be Polite')!"
    },
    "joke_5": {
        "setup": "How does a Python programmer say “I love you”?",
        "punchline": "With an infinite loop: while True: print('I love you')"
    },
    "joke_6": {
        "setup": "What do you call a snake that loves coding?",
        "punchline": "A Python developer — runs on Windows, but only if you sudo-charm it!"
    },
    "joke_7": {
        "setup": "Why did the function stop calling its parents?",
        "punchline": "Because it had serious recursion issues — too deep, stack overflow!"
    },
    "joke_8": {
        "setup": "Why did the developer go to the bar?",
        "punchline": "Because the password was 'incorrect' — and the system said: 'Please enter your password'. So they did!"
    },
    "joke_9": {
        "setup": "What’s a programmer’s favorite snack?",
        "punchline": "Chips & bytes! Bonus if eaten at 2 AM during debugging."
    },
    "joke_10": {
        "setup": "Why did the Python list break up with the tuple?",
        "punchline": "Because the tuple said, 'I can’t change for you,' and the list wanted someone mutable!"
    }
   
}


import random

# Pick a random joke
key = random.choice(list(python_jokes.keys()))
joke = python_jokes[key]

print(f"😂 {joke['setup']}")
input("👉 Press Enter to see the punchline...")  # To Makes it interactive!
print(f"🎉 {joke['punchline']}")