# Hangman game by Chloe Yeo for 1CT


import turtle, random, time

# The following sets up the display screen
window = turtle.Screen()
window.title("HANGMAN")
window.tracer()
turtle.bgcolor("pink")
turtle.setup(600,600)
turtle.pensize(5)
turtle.color("black")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-230,0)
turtle.write("HANGMAN GAME BY CHLOE YEO", font = ("Arial", 20, "bold"))
time.sleep(2)
turtle.bgcolor("white")
turtle.reset()
turtle.hideturtle()
turtle.pendown()

words = []
with open("nouns.txt") as f:
    for line in f:
        words.append(line.strip())
word_to_guess = random.choice(words) #randomly chooses something from the list

letters = "abcdefghijklmnopqrstuvwxyz"
letter_list = []
correctLetter = []

for letter in range(len(word_to_guess)): # this converts each letter in word to a list
    letter_list.append(word_to_guess[letter])

for letter in word_to_guess: # this sets all letters in word to _
    correctLetter.append("_")

count = 0
letters_pressed = []

print("Press the letter to guess in a word")
turtle.penup()
turtle.goto(-200,200)
turtle.write("_ "*len(word_to_guess), font = ("Arial", 15, "bold")) # this draws out _ for each letter in word at the start


lives = 10
print("You have {} lives left.".format(lives))

def drawHangman():
    global count # count keeps tracks of which piece to draw
    turtle.hideturtle()
    turtle.penup()
    if count == 1:
        turtle.goto(0,0)
        turtle.pendown()
        turtle.forward(100)
    elif count == 2:
        turtle.goto(50,0)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(100)
    elif count == 3:
        turtle.goto(50,100)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(50)
    elif count == 4:
        turtle.goto(100,100)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(20)
    elif count == 5:
        turtle.goto(100,80)
        turtle.pendown()
        turtle.circle(10)
    elif count == 6:
        turtle.goto(100,80)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(45)
    elif count == 7:
        turtle.goto(100,80)
        turtle.pendown()
        turtle.setheading(290)
        turtle.forward(30)
        turtle.setheading(270)
    elif count == 8:
        turtle.goto(100,80)
        turtle.pendown()
        turtle.setheading(250)
        turtle.forward(30)
        turtle.setheading(270)
    elif count == 9:
        turtle.goto(100,35)
        turtle.pendown()
        turtle.setheading(290)
        turtle.forward(25)
        turtle.setheading(270)
    elif count == 10:
        turtle.goto(100,35)
        turtle.pendown()
        turtle.setheading(250)
        turtle.forward(25)
        turtle.setheading(270)
            
def genKeyCallBackFunction(thisLetter):
    # The following definition CREATES A NEW function every time I press a letter
    # This function is called. The new function is linked to the particular
    # letter provided on this call - in the thisLetter parameter...
    def play():
        global count
        global lives
        turtle.hideturtle()
        if letter_list != correctLetter: # This checks if the letter you pressed is one of the correct letters in word to guess
    
            if thisLetter not in word_to_guess and thisLetter not in letters_pressed: # If it is an incorrect guess and you have not pressed that letter before...
                letters_pressed.append(thisLetter)
                count = count + 1
                drawHangman()
                lives = lives - 1
            elif (thisLetter not in word_to_guess or thisLetter in word_to_guess) and thisLetter in letters_pressed: # If you have already pressed that letter before...
                print("You have already guessed this letter. Try another one!")
                    
            elif thisLetter in word_to_guess and thisLetter not in letters_pressed: # If it is a correct guess and you haven not pressed that letter before...
                letters_pressed.append(thisLetter)
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == thisLetter:
                        correctLetter[i] = thisLetter # Replace the _ in correctLetter list with the letter you pressed
            print("You have pressed these letters: {}".format(", ".join(letters_pressed)))



            for letter in range(len(correctLetter)):
                turtle.penup()
                turtle.goto(-200,200)
                turtle.write("_ "*letter+correctLetter[letter], font = ("Arial", 15, "bold"))
               
            if lives > 0 and letter_list != correctLetter:
                print("You have {} lives left.".format(lives))
            elif lives == 0:
                print("Failed! You have 0 lives left.")
                quitFun()
            if letter_list == correctLetter:
                turtle.penup()
                turtle.goto(-200,-150)
                turtle.write("You guessed it right!",font = ("Arial", 15))
                time.sleep(2)
                quitFun()
                
    # ...and return that function.
    return play

def quitFun():
    turtle.bye()

for letter in letters:
    # Get a callback fuction specially for THIS letter
    thisLetterCallBack = genKeyCallBackFunction(letter)

    # and associate it with a key press of THIS letter
    turtle.onkeypress(thisLetterCallBack, letter)

turtle.listen()
turtle.mainloop()
