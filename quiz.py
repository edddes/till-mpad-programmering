"""
quiz.py: Ett quiz-spel där spelaren testar sina kunskaper inom
         pythons historia och tekniska uppfinningar. 5 frågor för
         varje kategori i flervalsformat. Få så många poäng som
         möjligt!

__author__ = "Edvin Ranheden"
__version__ = "1.0.2"
__email__ = "edvin.ranheden@elev.ga.ntig.se"
"""

import os


VERSION = "1.0.2"

AUTHOR = "Edvin"

python_history_questions = [
    {
        "question": "Vem skapade Python?",
        "options": ["a) Guido Van Rossum", "b) Linus Torvalds", "c) Bill Gates"],
        "answer": "a"
    },
    {
        "question": "Vilket år släpptes Python för första gången?",
        "options": ["a) 1989", "b) 1991", "c) 1995"],
        "answer": "b"
    },
    {
        "question": "Vad är Python uppkallat efter?",
        "options": ["a) En orm", "b) Monty Python's Flying Circus", "c) En programmeringsterm"],
        "answer": "b"
    },
    {
        "question": "När släpptes Python 2.0?",
        "options": ["a) 1998", "b) 2000", "c) 2002"],
        "answer": "b"
    },
    {
        "question": "Vilken funktion kom med Python 2.0?",
        "options": ["a) List Comprehensions", "b) Async/await", "c) Type hints"],
        "answer": "a"
    },
]

technical_inventions_questions = [
    {
        "question": "Vem uppfann åskledaren?",
        "options": ["a) Thomas Edison", "b) Benjamin Franklin", "c) Nikola Tesla"],
        "answer": "b"
    },
    {
        "question": "Vilket år utfärdades det första amerikanska patentet?",
        "options": ["a) 1776", "b) 1790", "c) 1801"],
        "answer": "b"
    },
    {
        "question": "Vem uppfann bomullsrensaren?",
        "options": ["a) Eli Whitney", "b) James Watt", "c) Alexander Graham Bell"],
        "answer": "a"
    },
    {
        "question": "När uppfanns den första praktiska ismaskinen?",
        "options": ["a) 1836", "b) 1856", "c) 1876"],
        "answer": "b"
    },
    {
        "question": "Vem uppfann telefonen?",
        "options": ["a) Thomas Edison", "b) Nikola Tesla", "c) Alexander Graham Bell"],
        "answer": "c"
    },
]

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print(f"{bcolors.BLUE}{'=' * 40}{bcolors.DEFAULT}")
    print(f"{bcolors.YELLOW}{title:^40}{bcolors.DEFAULT}")
    print(f"{bcolors.BLUE}{'=' * 40}{bcolors.DEFAULT}")

def print_footer():
    print(f"{bcolors.BLUE}{'=' * 40}{bcolors.DEFAULT}")

def display_rules():
    clear_screen()
    print_header("Spelregler")
    print(f"{bcolors.CYAN}1. Välj ett ämne: Pythons Historia eller Tekniska Uppfinningar")
    print("2. Svara med flervalsalternativ")
    print("3. Svara med 'a', 'b' eller 'c'")
    print(f"4. Du får 1 poäng för varje rätt svar{bcolors.DEFAULT}")
    print(f"{bcolors.GREEN}Lycka Till!{bcolors.DEFAULT}")
    print_footer()
    input(f"{bcolors.YELLOW}Tryck Enter för att börja!{bcolors.DEFAULT}")

def choose_topic():
    clear_screen()
    print_header("Välj ett ämne")
    print(f"{bcolors.CYAN}1. Pythons Historia")
    print(f"2. Tekniska Uppfinningar{bcolors.DEFAULT}")
    print_footer()
    while True:
        choice = input(f"{bcolors.GREEN}Ange ditt val (1 eller 2): {bcolors.DEFAULT}")
        if choice in ["1", "2"]:
            return python_history_questions if choice == "1" else technical_inventions_questions
        print(f"{bcolors.RED}Ogiltigt val. Försök igen{bcolors.DEFAULT}")

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, q in enumerate(questions, 1):
        clear_screen()
        print_header(f"Fråga {i}/{total_questions}")
        print(f"{bcolors.CYAN}Poäng: {score}/{total_questions}{bcolors.DEFAULT}")
        print()
        print(f"{bcolors.YELLOW}{q['question']}{bcolors.DEFAULT}")
        for option in q["options"]:
            print(f"{bcolors.CYAN}{option}{bcolors.DEFAULT}")
        print_footer()

        while True: 
            user_answer = input(f"{bcolors.GREEN}Ditt svar (a/b/c): {bcolors.DEFAULT}").lower()
            if user_answer in ["a", "b", "c"]:
                break
            print(f"{bcolors.RED}Ogiltigt svar. Ange istället 'a', 'b' eller 'c'.{bcolors.DEFAULT}")

        if user_answer == q["answer"]:
            print(f"{bcolors.GREEN}Rätt!{bcolors.DEFAULT}")
            score += 1
        else:
            print(f"{bcolors.RED}Tyvärr, rätt svar är {q['answer']}.{bcolors.DEFAULT}")
        input(f"{bcolors.YELLOW}Tryck Enter för att fortsätta{bcolors.DEFAULT}")
        clear_screen()

    print_header("Quiz avslutat")
    print(f"{bcolors.CYAN}Ditt slutpoäng: {score}/{total_questions}{bcolors.DEFAULT}")
    print_footer()

def main():
    while True:
        clear_screen()
        print_header(f"Välkommen till Quiz spelet! {VERSION} av {AUTHOR}")
        input(f"{bcolors.YELLOW}Tryck Enter för att se spelreglerna{bcolors.DEFAULT}")
        display_rules()
        clear_screen()
        questions = choose_topic()
        run_quiz(questions)

        play_again = input(f"{bcolors.GREEN}Vill du spela igen? skriv ja/nej: {bcolors.DEFAULT}").lower()
        if play_again != "ja":
            break

    clear_screen()
    print(f"{bcolors.CYAN}Tack för att du spelade!{bcolors.DEFAULT}")

if __name__ == "__main__":
    main()
