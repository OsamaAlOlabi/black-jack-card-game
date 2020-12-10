import art
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
bot_cards = []
my_score = 0
bot_score = 0


# Choose a random card for the player
def random_card_for_me():
    global my_score

    my_card_num_index = random.randrange(len(cards))
    my_card_num_value = cards[my_card_num_index]
    my_cards.append(my_card_num_value)
    my_score = sum(my_cards)

    # If random card is 11, check if the sum of cards > 21 then change 11 to 1
    while True:
        if 11 in my_cards and my_score > 21:
            change = my_cards.index(11)
            my_cards[change] = 1
        else:
            break

    my_score = sum(my_cards)


# Choose a random card for the dealer
def random_card_for_bot():
    global bot_score

    bot_card_num_index = random.randrange(len(cards))
    bot_card_num_value = cards[bot_card_num_index]
    bot_cards.append(bot_card_num_value)
    bot_score = sum(bot_cards)

    # If random card is 11, check if the sum of cards > 21 then change 11 to 1
    while True:
        if 11 in bot_cards and bot_score > 21:
            change = bot_cards.index(11)
            bot_cards[change] = 1
        else:
            break

    bot_score = sum(bot_cards)


# How the game functions
def black_jack():


    print(f"Your cards are {my_cards}, your current score: {my_score}")
    print(f"Dealer starting card is: {bot_cards}")

    # How the dealer functions
    def bot_logic():
        while bot_score <= my_score:
            random_card_for_bot()
            if bot_score == 21 and my_score == 21:
                print(f"Your final hand is: {my_cards}, final score: {my_score}")
                print(f"Dealer final hand is: {bot_cards}, final score: {bot_score}")
                print("It's a draw")
                play_again()
                break
            elif bot_score > 21:
                print(f"Your final hand is: {my_cards}, final score: {my_score}")
                print(f"Dealer final hand is: {bot_cards}, final score: {bot_score}")
                print(f"You win, the dealer {bot_score} is above 21")
                play_again()
                break

        print(f"Your final hand is: {my_cards}, final score: {my_score}")
        print(f"Dealer final hand is: {bot_cards}, final score: {bot_score}")
        print(f"You lose, the dealer has {bot_score} and you have {my_score}\n")
        play_again()

    if my_score == 21:
        bot_logic()

    elif my_score > 21:
        print(f"\nYou're score is {my_score} which is above 21.")
        print("You lose\n")
        play_again()
    elif my_score < 21:
        while True:
            another_card = input("Would you like another card? 'Y' or 'N' ").lower()
            print("")
            if another_card == "y":
                random_card_for_me()
                black_jack()
                break
            elif another_card == "n":
                bot_logic()
                break
            else:
                print("Please type 'Y' or 'N'")


# Play again function
def play_again():
    global my_score
    global bot_score
    global my_cards
    global bot_cards

    while True:
        repeat = input("Would you like to play again? 'Y' or 'N' ")
        if repeat == "y":
            my_cards = []
            bot_cards = []
            my_score = 0
            bot_score = 0
            print("*************************************************************")
            print(art.logo)

            random_card_for_me()
            random_card_for_me()
            random_card_for_bot()

            black_jack()
            break
        elif repeat == "n":
            exit()
        else:
            print("Please type 'Y' or 'N'")
