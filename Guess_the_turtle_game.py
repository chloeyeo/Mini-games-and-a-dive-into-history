import turtle, threading, random, time

# The following sets up the display screen
window = turtle.Screen()
window.title("GUESS THE TURTLE GAME")
window.tracer(0)
turtle.bgcolor("black")
turtle.setup(1000,1000)
turtle.pensize(5)
turtle.color("red")
turtle.speed(0)
turtle.penup()
turtle.hideturtle()
turtle.goto(0,-100)
turtle.write("GUESS THE TURTLE GAME BY CHLOE YEO", align = "center", font = ("Arial", 20, "bold"))
time.sleep(2)
turtle.reset()

# this displays "3-2-1-Go!" before the game starts
for i in range(3):
    turtle.hideturtle()
    turtle.pensize(5)
    turtle.color("red")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,-100)
    turtle.write(3-i, align = "center", font = ("Arial", 35, "bold"))
    time.sleep(1)
    turtle.reset()
turtle.hideturtle()
turtle.pensize(5)
turtle.color("red")
turtle.speed(0)
turtle.penup()
turtle.goto(0,-100)
turtle.write("Go!", align = "center", font = ("Arial", 35, "bold"))
time.sleep(1)
turtle.reset()
turtle.update()

squares = {} # squares stores the index of each square, e.g. {0:{"shape": "square", "x":x, "y":y, "width": width}, 1:{"shape": "square", "x":x, "y":y, "width": width}...}

def beginRound(rows, columns):
    '''Sets the timer for each round depending on rows and columns.
       For each column in each row, the information of the (count)th square is stored in
       the form dictionary inside dictionary called squares with count being the key.'''
    
    global myTimer
    myTimer = threading.Timer(rows*columns, stopRound)
    myTimer.start()

    turtle.speed(0)
    count = 0


    for row in range(rows):
        for column in range (columns):
            squares[count] = drawSquare(column*50,row*50,30)
            count = count + 1
            
    
def drawSquare(x,y,width=50,color="red"):
    
    '''Draw a single square on the screen at position (x,y)
       with specified color and width.
       It returns a dictionary of the square data.'''
    
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x-200,y-400)
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4): # this is to draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    return {"shape": "square", "x":x, "y":y, "width": width}



def isCoordinateInSquare(x,y,square):
    
    '''Check whether x,y coordinates fall inside the
       square - which is a dictionary with x,y bottom left point and width.'''
    
    squareLeft = square["x"] - 200
    squareRight = squareLeft + square["width"]
    squareBottom = square["y"] - 400
    squareTop = squareBottom + square["width"]

    return (x >= squareLeft and x <= squareRight and y >= squareBottom and y <= squareTop)


def findBox(x,y):
    
    '''If the x,y coordinates of the point that user clicked is within a square,
        the index of the square in the list called squares is returned.'''
    
    for i in squares:
        if isCoordinateInSquare(x,y,squares[i]):
            return i
    return None

times_won = 0

def changeBox(x,y):
    
    '''Remove the red square that has been clicked by drawing black squares on top.
       When user clicks correct square, white turtle is shown and user wins round.'''
    
    i = findBox(x,y)
    if i == None:
        return
    square = squares[i]
    drawSquare(square["x"]-1, square["y"]-1, square["width"]+2, "black")
    
    if i == correctSquare:
        global times_won
        turtle.goto(x,y)
        turtle.color("white")
        turtle.shape("turtle")
        turtle.showturtle()
        turtle.update()
        time.sleep(2)
        
        turtle.onscreenclick(None)
        turtle.hideturtle()
        turtle.pensize(5)
        turtle.color("pink")
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-360,-200)
        turtle.write("You are the champion!", align = "center", font = ("Arial", 15, "bold"))
        myTimer.cancel()
        times_won += 1
        endRoundTimer = threading.Timer(2, setup_round)
        endRoundTimer.start()
        
def stopRound():
    
    '''When timer runs out, round ends.
       The user loses round and moves on to next round.'''
    
    turtle.hideturtle()
    turtle.pensize(5)
    turtle.color("orange")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-370,-200)
    turtle.write("Time up!\nYou have lost this round.", align = "center", font = ("Arial", 13, "bold"))
    turtle.onscreenclick(None)
    time.sleep(2)
    setup_round()

correctSquare = None
rounds_passed = 0
        
def setup_round():
    '''calls other functions to draw out squares in the row*column grid and
       removes each square when clicked by user and when correct square is clicked, turtle appears.
       when all rounds are finished where number of rounds is set by user, the games score appears
       at the end with a confetti called bouncing_balls.'''
    
    global correctSquare, rounds_passed
    
    # Round is the number of rounds the user sets at first by input, rounds_passed is literally number of rounds passed.
    
    turtle.reset()
    rounds_passed += 1
    if rounds_passed > Round: # this is when all rounds finish
        turtle.onscreenclick(None)
        turtle.reset()
        turtle.penup()
        turtle.color("white")
        turtle.hideturtle()
        turtle.goto(0,-100)
        turtle.write("Game ended! You have won {} out of {} rounds.".format(times_won, Round),align = "center", font = ("Vijaya", 20, "bold"))
        bouncing_ball()
        turtle.bye()
        return
            
    turtle.penup()
    turtle.goto(-400,0)
    turtle.color("white")
    turtle.write("ROUND "+str(rounds_passed), font = ("Arial", 20, "bold"))
    turtle.goto(-460,-100)
    turtle.write("Click the squares within\nthe time limit until\nyou find the turtle!", font = ("Arial", 14, "bold"))
    turtle.hideturtle()
    row = int(input("Please enter the number of rows: "))
    column = int(input("Please enter the number of columns: "))
    while row >= 13 or column >= 15 :
        print("Please try again with less rows and/or columns!")
        row = int(input("Please enter the number of rows: "))
        column = int(input("Please enter the number of columns: "))
    correctSquare = random.randint(0,(row*column)-1)
    beginRound(row,column)
    turtle.onscreenclick(changeBox) # when i click, the program calls changeBox(x,y)
        

def bouncing_ball():

    '''Various shapes floating around screen in random directions.'''
    
    balls = []
    for i in range(10):
        balls.append(turtle.Turtle())
    colours = ["red","yellow","pink","orange","green","white","purple","blue"]
    shapes = ["circle","triangle","square"]
    for ball in balls:
        ball.shape(random.choice(shapes))
        ball.color(random.choice(colours))
        ball.penup()
        ball.speed(0)
        x_ball = random.randint(-290,290)
        y_ball = random.randint(200,400)
        ball.goto(x_ball,y_ball)
        ball.dy = 0
        ball.dx = random.randint(-3,3)
        
    gravity = 0.1
    for i in range(600):
        window.update()
        for ball in balls:
            ball.dy = ball.dy - gravity
            ball.sety(ball.ycor()+ball.dy)
            ball.setx(ball.xcor()+ball.dx)

            # Check for a wall collision
            if ball.xcor() > 300:
                ball.dx = ball.dx*-1
            if ball.xcor() < -300:
                ball.dx = ball.dx*-1

            # Check for a bounce
            if ball.ycor() < -300:
                ball.dy = ball.dy*-1

Round = int(input("How many rounds do you want to play?: "))
    
setup_round()

turtle.mainloop()
