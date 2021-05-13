import os
import random

global colors
colors=["ORANGE","YELLOW","GREEN","BLUE","PURPLE","PINK"]

#number of players
def playerNumber():
        try:
                n=int(input("\n\033[1;35;40mEnter number of players (1 or 2):"))
                if n==1:
                        global colorcode
                        colorcode=compcodemaker()
                        codebreaker()
                elif n==2:
                        player2()
                        return
                else:
                     raise exception   
        except:
                print("Invalid input.")
                print("*************************")

#creates code for single player game
def compcodemaker():
        colorcode=[]
        for i in range(4):
                colorcode.append(random.choice(colors))

        #print(colorcode)               
        return colorcode

#matches guess against code for single player game, increments red and white pins accordingly
def check(guess):
        found=[0,0,0,0]
        red=white=i=0
        for i in range(4):
                tempguess=guess
                if colorcode[i] in guess:
                        pos=guess.index(colorcode[i])
                        while colorcode[i] in tempguess:
                                if found[pos]:
                                        tempguess=guess[pos+1:]
                                        if colorcode[i] in tempguess:
                                                pos=guess.index(colorcode[i],pos+1)
                                        else:
                                                break
                                else:
                                        break
                        if colorcode[pos]==guess[pos] and found[pos]==0:
                                red+=1
                        elif colorcode[i]==guess[i] and found[i]==0:
                                pos=i
                                red+=1
                        else:
                                if found[pos]==0:
                                        white+=1
                        found[pos]=1
        pins=(red,white)
        return pins

#prompts player to guess the code in single player game
def codebreaker():
        print("\n\033[1;37;40mGuess the code within 12 turns to win!\033[1;35;40m")

        i=0
        while i!=12:

                print("\nEnter guess",i+1,":")
                guess=input("\033[1;37;45m").upper().split(",")
                #print(guess)
                for item in range(len(guess)):
                        guess[item]=guess[item].strip()
                #print(guess)

                #print(colors)

                #makes sure player has entered four items
                if len(guess)==4:

                        #checks to see if the colors entered are valid colors from the global list
                        invalidcolor=False
                        print("\n")
                        for guess_item in guess:
                                if guess_item not in colors:
                                        print(guess_item, "is not a valid color")
                                        invalidcolor=True
                        if invalidcolor==True:
                                print("\nThe valid colors are: ")
                                for color in colors:
                                        print(color)
                                print("*************************")

                         
                        if invalidcolor == False:
                                pins=check(guess)
                                i+=1
                                print("\n\033[1;31;40mNumber of red pins:",pins[0])
                                print("\033[1;37;40mNumber of white pins:",pins[1])
                                print("\033[1;35;40m")
                                print("*************************")

                                if pins[0]==4:
                                        print("Victory is yours!!!")
                                        print("*************************")
                                        break

                                else:
                                        pass

                else:
                        print("\nYou have not entered exactly 4 colors. Try again.")
                        print("*************************")
      
        else:
                print("Sorry, you lose :(")
                print("The code was:",colorcode)
                print("*************************")


#for a two player game
def player2():
        print("\n")
        print("*************************")
        print('''\033[1;37;40mThe players will decide on a number of sets.
        Each set consists of two games. In the first game, one player will be the codemaker,
        and the other will be the codebreaker. In the second game, they switch roles.''')
        print('''Point system:
        For every guess made by the codebreaker, the codemaker is awarded 1 point, provided the
        guess is incorrect. If, at the end of 12 turns, the codebreaker has failed to correctly
        guess the code, the codemaker is awarded a bonus of 5 points.''')
        print("At the end of the chosen number of sets, the player with the most points wins!\033[1;35;40m")
        sets=int(input("\n\033[1;35;40mEnter number of sets:"))
        points=[0,0]
        print("*************************")
        
        for i in range(sets):
                print("\nSet",i+1,":")
                print("\nScore:")
                print("Player 1:",points[0])
                print("Player 2:",points[1])
                j=0
                while j!=2:
                                print("\nPlayer",j+1,"- enter your code:")
                                colorcode=input("\033[1;37;45m").upper().split(",")
                                #print(colorcode)
                                for item in range(len(colorcode)):
                                        colorcode[item]=colorcode[item].strip()
                                #print(colorcode)

                                #print(colors)

                                #makes sure player has entered four items
                                if len(colorcode)==4:

                                        #checks to see if the colors entered are valid colors from the global list
                                        print("\n")
                                        invalidcolor=False
                                        for colorcode_item in colorcode:
                                                if colorcode_item not in colors:
                                                        print(colorcode_item, "is not a valid color")
                                                        invalidcolor=True
                                                        
                                        if invalidcolor==True:
                                                print("\nThe valid colors are: ")
                                                for color in colors:
                                                        print(color)
                                                print("*************************")
                         
                                        if invalidcolor == False:
                                                print("\033[1;35;40mYour code is",colorcode,"\nRemember it.")
                                                input("\nPress ENTER to clear screen:")
                                                os.system("clear")
                                                #os.system("cls")
                                                print("*************************")
                                                if j==0:
                                                        print("Player 2, start guessing.")
                                                else:
                                                        print("Player 1, start guessing:")
                                                

                                                turn=0
                                                while turn!=12:
                                                        print("*************************")
                                                        print("\nScore:")
                                                        print("Player 1:",points[0])
                                                        print("Player 2:",points[1])
                                                        print("\nGuess",turn+1,":")
                                                        guess=input("\033[1;37;45m").upper().split(",")
                                                        for item in range(len(guess)):
                                                                guess[item]=guess[item].strip()

                                                        #print(guess)

                                                        #print(colors)
                                                        
                                                        #makes sure player has entered four items
                                                        if len(guess)==4:

                                                                #checks to see if the colors entered are valid colors from the global list
                                                                invalidcolor=False
                                                                print("\n")
                                                                for guess_item in guess:
                                                                        if guess_item not in colors:
                                                                                print(guess_item, "is not a valid color")
                                                                                invalidcolor=True
                                                                        
                                                                                
                                                                if invalidcolor==True:
                                                                        print("\nThe valid colors are: ")
                                                                        for color in colors:
                                                                                print(color)
                                                                        print("*************************")
                                 
                                                                if invalidcolor == False:
                                                                        try:
                                                                                print("\n\033[1;35;40mCodemaker, enter pins:")
                                                                                red=int(input("\033[1;31;40mNumber of red pins:"))
                                                                                white=int(input("\033[1;37;40mNumber of white pins:"))
                                                                                print("\033[1;35;40m")
                                                                                
                                                                                if ((red+white)<=4) and ((red,white) != (3,1)):
                                                                                        if red!=4:
                                                                                                points[j]+=1
                                                                                        else:
                                                                                                print("\033[1;32;40mYou guessed it!!!\033[1;35;40m")
                                                                                                print("*************************")
                                                                                                break
                                                                                        turn+=1
                                                                                else:
                                                                                        print("\nInvalid combination of reds and whites!!")
                                                                        except:
                                                                                print("That wasn't a number!")
                                                                               
                                                        else:
                                                                print("\nYou have not entered exactly 4 colors. Try again.")
                                                                
                                                                
                                                else:
                                                        print("\033[1;31;40mSorry! You're out of turns :(\033[1;35;40m")
                                                        points[j]+=5
                                                        print("The code was:",colorcode)
                                                        print("\nThe codemaker gets an extra five points!!")
                                                        print("\nScore:")
                                                        print("Player 1:",points[0])
                                                        print("Player 2:",points[1])
                                                        print("*************************")
                                                j+=1

                                else:
                                        print("\nYou have not entered exactly 4 colors. Try again.")
                                        print("*************************")
                                        
        print("*************************")                       
        print("\nFinal score:")
        print("Player 1:",points[0])
        print("Player 2:",points[1])
        if points[0]>points[1]:
                print("\033[1;36;40mPlayer 1 wins!!!")
        elif points[0]<points[1]:
                print("\033[1;36;40mPlayer 2 wins!!!")
        else:
                print("\033[1;36;40mTie. Well played!")
        print("*************************")

print("*************************")
print('''The rules are as follows:
There is a codemaker who sets a code of four colors, in a certain order.
Duplicates can be present in the code.
The colors that may be present in the code are:
\033[1;36;40mORANGE,YELLOW,GREEN,BLUE,PURPLE,PINK.\033[1;37;40m
The codebreaker has 12 turns to try and guess the code, based on the pins provided.
There are two types of pins: Red and white.
If a color in your guess exists in the code, you will be awarded a WHITE pin.
If the position of the color in your guess matches the position of the same color in the code,
you are awarded a RED pin instead. Use the pins awarded to crack the code!
(color matches, position matches -> RED)
(color matches, position does not match -> WHITE)''')
print("*************************")

while True:
        game=input("\n\033[1;32;40mStart a new game? (Y/N):").upper()
        if game=="Y":
                playerNumber()
        elif game=="N":
                print("\033[1;36;40mThank you for playing!")
                break
        else:
                print("Invalid input.")
