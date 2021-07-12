##Kyriacos Rouvas
#rock paper scissors Game Theory & random responce machine
## importing required modules
from random import randint
from collections import OrderedDict
from tabulate import tabulate
import msvcrt as m
import sys
import time
import datetime
import json
import os


## stating variables
userInput = "0"
nextChoice = "0"
gameResult = "0"
rpsNum = 0
tobeIntepreted = -1
score = [0, 0, 0]  # User : Program : # of rounds
escape = "no"
goodByemsg = "bye"
timeNow = datetime.datetime.now()
timeID = time.time()
tmrStrt = 0
tmrEnd = 0
rndGame = "no"
swtchModes = "yes"
playerName = ""
# UserID/playDateTime : UserUser Name : user points : program points : Difference
saveScore = {"User Name": "", "User Points": 0,
             "Program Points": 0, "Difference": 0}
saveFile = {}
listsave = []
jItterator = 0
top10Ranks = []
asd = 0


## stating all functions w/ 0.5" delays at their end
# program first choice finder sequence
def FindRandChoice():
    global rpsNum, nextChoice
    # rand num to find frst choice
    firstChoice = randint(1, 3)

    # intepreting frst choice from num to value
    if firstChoice == 1:
        firstChoice = "rock"
        rpsNum = 0
        print("Program: " + firstChoice)
    elif firstChoice == 2:
        firstChoice = "paper"
        rpsNum = 1
        print("Program: " + firstChoice)
    elif firstChoice == 3:
        firstChoice = "scissors"
        rpsNum = 2
        print("Program: " + firstChoice)

    nextChoice = firstChoice
    time.sleep(0.5)

# program next choice
def ComputNextChoice():
    global nextChoice, gameResult, rpsNum, tobeIntepreted
    # finding next choice(unintepreted)
    if gameResult == "Victory":
        rpsNum += 2
        tobeIntepreted = rpsNum % 3
    elif gameResult == "Loss":
        rpsNum -= 1
        tobeIntepreted = rpsNum % 3
    elif gameResult == "Tie":
        FindRandChoice()
        return (nextChoice, gameResult, rpsNum, tobeIntepreted)

    # intepreting
    if tobeIntepreted == 0:
        nextChoice = "rock"
        print("Program: " + nextChoice)
    elif tobeIntepreted == 1:
        nextChoice = "paper"
        print("Program: " + nextChoice)
    elif tobeIntepreted == 2:
        nextChoice = "scissors"
        print("Program: " + nextChoice)

    time.sleep(0.5)

# user input & refiner
def GetUserInput():
    global userInput
    while True:
        # user input
        rawuserInput = input("rock paper or scissors? ")
        rawuserInput = str(rawuserInput)

        # refiner
        if (rawuserInput == "r") or (rawuserInput == "ro") or (rawuserInput == "roc") or (rawuserInput == "rock"):
            userInput = "rock"
            break
        elif (rawuserInput == "p") or (rawuserInput == "pa") or (rawuserInput == "pap") or (rawuserInput == "pape") or (rawuserInput == "paper"):
            userInput = "paper"
            break
        elif (
            (rawuserInput == "s")
            or (rawuserInput == "sc")
            or (rawuserInput == "sci")
            or (rawuserInput == "scis")
            or (rawuserInput == "sciss")
            or (rawuserInput == "scisso")
            or (rawuserInput == "scissor")
            or (rawuserInput == "scissors")
        ):
            userInput = "scissors"
            break
        elif (rawuserInput == "Tips"):
            print(
                "If you figure out the special Game Theory Algorithm that this Program uses you'll get 100/100")
            time.sleep(2)
            continue
        elif (rawuserInput == "Credits"):
            print("""
This program has been created completely with the use of Python3 and is my first experience on programming with this language

I have been challenged by a fellow soldier to prove that i was infact capable of programming in order to vindicate my spot on the local laptop so...

Andro Fakka tin to PC tora en diko m BUAHAHAHAHAHAHAHA

Anw life is going smoothely, i get some random punishments here and there but when your vlocaptain keeps a grudge on you thats the definition of a smooth life


Finally this program uses ideas and techniques which were studied and presented in the 2017 EuroMath Conference GC School presentation 
"Game Theory" featuring various methods to maximise your chances of Success in different Game scenarios much like this one

Special Thanks and Respect to our Teacher-Coaches:
Christiana Hadjipandeli & Eleni Apostolou (The Amazing Duo)
and ofcourse to my team mates formally, in the present time, known as:
Captain Egli Metaxa
Trusted Reserve Officer Kronides Glafkos
Corporal Rouvas Kyriacos
Private Georgiou Grigoris
                                            ---Δνεας (ΠΖ) Ρούβας Κυριάκος
                                            3/2/2019 -- ΕΓΑ/ΓΕΕΦ
            """)
            time.sleep(3)
            continue
        elif rawuserInput == "Andros":
            print("Andro fakka tin")
        # check
        else:
            print("wrong input try again")
            time.sleep(0.5)
            continue

    # stating userInput
    print("User: " + userInput)

    time.sleep(0.5)

# win/lose function
def FindGameResult():
    global nextChoice, gameResult, userInput, score
    if userInput == "rock":
        if nextChoice == "rock":
            gameResult = "Tie"
        elif nextChoice == "paper":
            gameResult = "Loss"
            score[1] += 1
        elif nextChoice == "scissors":
            gameResult = "Victory"
            score[0] += 1

    elif userInput == "paper":
        if nextChoice == "rock":
            gameResult = "Victory"
            score[0] += 1
        elif nextChoice == "paper":
            gameResult = "Tie"
        elif nextChoice == "scissors":
            gameResult = "Loss"
            score[1] += 1

    elif userInput == "scissors":
        if nextChoice == "rock":
            gameResult = "Loss"
            score[1] += 1
        elif nextChoice == "paper":
            gameResult = "Victory"
            score[0] += 1
        elif nextChoice == "scissors":
            gameResult = "Tie"

    print(gameResult)
    time.sleep(0.5)

# asking if player wants to continue from first round
def StopTheRnd():
    global escape, rndGame, swtchModes
    # round count
    score[2] += 1
    userInput = input("Do you want to Keep on playing? ")
    if (userInput == "y") or (userInput == "ye") or (userInput == "yes"):
        print("Next round:")
    elif (userInput == "n") or (userInput == "no"):
        print("Game Over")
        escape = "yes"
        swtchModes = "no"
    elif (userInput == "Random"):
        rndGame = "yes"
        swtchModes = "yes"
        escape = "yes"
        print("Next round")
    elif (userInput == "Game Theory"):
        rndGame = "no"
        swtchModes = "yes"
        escape = "yes"
        print("Next round")
    else:
        print("Next round:")

    time.sleep(0.5)

# waiting for key press (no time delay)
def PressKey():
    print("Press Any Key to Close Program")
    m.getch()

# goodbye msg awarness fnctn (no time delay)
def TimeAwarness():
    global timeNow, goodByemsg
    timeNow = datetime.datetime.now()
    if (5 <= timeNow.hour < 13):
        goodByemsg = "Have a Good Morning"
    elif (13 <= timeNow.hour <= 17):
        goodByemsg = "Have a Nice Afternoon"
    elif (17 < timeNow.hour < 22):
        goodByemsg = "Good Evening Hope to see you again"
    else:
        goodByemsg = "Buenas Noches mi Amigo\nHasta luego"


##game begins
# getting player name and ID w/respect to time
playerName = input("Enter User Name:")
playerName = str(playerName)
saveScore["User Name"] = playerName


# check for then create or load save file
if os.path.exists("./rouvasRPS_saveFile.json") == True:
    with open("rouvasRPS_saveFile.json", "r") as read_file:
        saveFile = json.load(read_file)
else:
    with open("rouvasRPS_saveFile.json", "w") as write_file:
        json.dump(saveFile, write_file)


# starting game timer
tmrStrt = time.time()


# play game w/ game loops for random or computed play
GetUserInput()

FindRandChoice()

FindGameResult()

StopTheRnd()

while (swtchModes == "yes"):
    swtchModes = "no"
    escape = "no"
    if rndGame == "no":
        while escape == "no":
            GetUserInput()

            ComputNextChoice()

            FindGameResult()

            StopTheRnd()

    elif rndGame == "yes":
        print("Random Program Responce Mode")
        time.sleep(0.5)
        while escape == "no":
            GetUserInput()

            FindRandChoice()

            FindGameResult()

            StopTheRnd()

        print("Random Mode Escaped")
        time.sleep(0.5)


# end game / report w/ gameplay time (stopping timer)
tmrEnd = time.time()
print("Score:\nUser : Program\n" +
      str(score[0:2]) + "\n" + str(score[2]) + " rounds played")
print("GamePlay Time: " + str(tmrEnd - tmrStrt) + '"')


# store scores
saveScore["User Points"] = score[0]
saveScore["Program Points"] = score[1]
saveScore["Difference"] = score[0] - score[1]
saveFile[timeID] = saveScore

# sort saved scores
saveFile = OrderedDict(
    sorted(saveFile.items(), key=lambda i: i[1]["Difference"], reverse=True))

saveFile = dict(saveFile)


# display top 10 ranks
time.sleep(2)
saveFile = dict(saveFile)

for k in saveFile.keys():
    listsave.append(saveFile[k])

asd = min(len(listsave), 10)

while jItterator < asd:
    top10Ranks.append(listsave[jItterator])
    jItterator += 1

print(tabulate(top10Ranks, headers="keys"))


# save game data
with open("rouvasRPS_saveFile.json", "w") as write_file:
    json.dump(saveFile, write_file)


# closing program
TimeAwarness()
PressKey()
print("Closing Program")
time.sleep(1)
print(goodByemsg)
time.sleep(2)
sys.exit()
