import random  # used to choose random tarot cards for game
import time  # used for timers between print statements
from colorama import Fore  # used to color the font
from pyfiglet import figlet_format  # used to create header and footer

life_tarot = {
    1: "the Magician! You have the ability to bring your dreams to reality.",
    2:
    "the High Priestess! Listen to your intuition and pay attention to your inner world.",
    3: "the Empress! You are nuturing and provide for others.",
    4: "the Emperor! You exude authority and love structure.",
    5:
    "the Hierophant! You are in the pursuit of knowledge and value tradition.",
    6: "the Lovers! You have an inner harmony and value partnerships.",
    7:
    "the Chariot! Your willpower and control will take you where you desire.",
    8:
    "Strength! While you are strong, it is highlighted with balance and compassion.",
    9: "the Hermit! This is a time for self relection."
}

tarot_cards = [
    "the Fool! Look for new beginnings and the opportunity to explore.",
    "the Magician! You have the ability to bring your dreams to reality.",
    "the High Priestess! Listen to your intuition and pay attention to your inner world.",
    "the Empress! You are nuturing and provide for others.",
    "the Emperor! You exude authority and love structure.",
    "the Hierophant! You are in the pursuit of knowledge and value tradition.",
    "the Lovers! You have an inner harmony and value partnerships.",
    "the Chariot! Your willpower and control will take you where you desire.",
    "Strength! While you are strong, it is highlighted with balance and compassion.",
    "the Hermit! This is a time for self relection.",
    "the Wheel of Fortune! Change is coming and it is not within your control.",
    "Justice! Now is the time for karma. The results are a direct result of your actions.",
    "the Hanged Man! You understand the value of self-sacrfice and are at peace with it.",
    "Death! You are at the end of a cycle and new beginning is coming.",
    "Temperance! Find balance to acheive peace and calm.",
    "the Devil! Find yourself feeling playful? Do not let it lead to excess.",
    "the Tower! Diaster is on the horizon but the aftermath can be an opportunity for new beginnings.",
    "the Star! Keep faith. A new beginning is coming.",
    "the Moon! Listen to your instincts.",
    "the Sun! You are overcoming fears and it results in great joy.",
    "Judgement! Evaluate yourself and your situation honestly to move forward.",
    "the World! Harmony abounds. You seek fulfillment and acheive it."
]


def title():
    print(figlet_format("TAROT READER", font="standard"))
    print(
        "[] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []"
    )


def choose():
    print()
    print(f"{Fore.GREEN}You have a few choices:")
    print("[1] Ask the cards a question")
    print("[2] Find the tarot card that defines your life")
    print("[3] Get a fortune for your past, present, and future")
    print(f"[4] Leave and quit the game{Fore.WHITE}")
    print()
    while True:
        choice = input("> ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return choice
        print()
        print(
            f"{Fore.GREEN}Sorry, I didn't understand that. Would you like to try again?{Fore.WHITE}"
        )
        print()


def pull_card():
    print()
    print(f"{Fore.GREEN}What is your question?")
    print()
    input(f"{Fore.WHITE}> ")
    card_number = random.randint(0, 22)
    print()
    print(f"{Fore.GREEN}You pulled {tarot_cards[card_number]}")


def life_card():
    print()
    print(f"{Fore.GREEN}What's your birthday? Please use MMDDYYYY format.")
    print()
    bday = int(input(f"{Fore.WHITE}> "))
    while bday >= 10:
        bday = str(bday)
        bday = list(map(int, bday))
        bday = sum(bday)
    print()
    print(f"{Fore.GREEN}Your life card is {life_tarot[bday]}")


def past_present_future():  # find a way to dry out this code
    print()
    card_number = random.choice(list(tarot_cards))
    time.sleep(1)
    print(f"{Fore.GREEN}Your past is represented by {card_number}")
    tarot_cards.remove(card_number)
    print()
    time.sleep(3)
    card_number = random.choice(list(tarot_cards))
    print(f"Your present is represented by {card_number}")
    tarot_cards.remove(card_number)
    print()
    time.sleep(3)
    card_number = random.choice(list(tarot_cards))
    print(f"Your future is represented by {card_number}")
    tarot_cards.remove(card_number)
    time.sleep(3)


def quit_game():
    print()
    time.sleep(1)
    print(f"{Fore.GREEN}Goodbye my dear! I'm sure I'll see you again soon...")
    time.sleep(1)
    print()
    print(
        f"{Fore.WHITE}[] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []"
    )
    print()
    print(figlet_format("TAROT READER", font="standard"))


def play_game():
    title()
    print()
    print()
    time.sleep(1)
    print(f"{Fore.GREEN}Hello! My name is Madame Loretta.")
    print()
    time.sleep(1)
    print("Welcome to my fortune telling room.")
    time.sleep(1)
    while True:
        choice = choose()
        if choice == "1":
            pull_card()
        if choice == "2":
            life_card()
        if choice == "3":
            past_present_future()
        if choice == "4":
            break
        print()
        print("Would you like to play again? [Y] of [N].")
        print()
        play_again = str.upper(input(f"{Fore.WHITE}> "))
        if play_again == "N":
            break
    quit_game()


play_game()