activity = int(input("Please type in what you would like to do -\n(1) Hangman (2) Guess the turtle game (3) Dive into history of women (4) Quit : "))
if activity != 4:               
    if activity == 1:
        import Hangman
    elif activity == 2:
        import Guess_the_turtle_game
    elif activity == 3:
        import History_of_Women
else:
    print("Thank you, Goodbye.")
