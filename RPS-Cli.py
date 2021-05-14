import random

def getAndValidateInput():
    validInput = False    
    while not validInput:
        userInput = str(input("\tEnter your sign (R/P/S) "))
        if userInput in ['R','P','S','r','p','s']:
            validInput = True
        else:
            print("\n\tInvalid Input \n\tPlease enter R/P/S\n")
    return userInput

def randomGenerator():
    randValue = str(random.randint(1,3))
    wrapper = {'1': 'R', '2':'P', '3':'S'}
    return wrapper.get(randValue)

def run(totalScore):
    computerScore = 0
    userScore = 0
    tied = 0
    while True:
        userInput = getAndValidateInput()
        computerInput = randomGenerator()
        pointFor = logic(userInput.upper(), computerInput)
        if pointFor == 'user':
            userScore+=1
        elif pointFor == 'computer':
            computerScore+=1
        else:
            tied+=1
        if userScore>=totalScore or computerScore>=totalScore:
            verdict = '\t  You lose' if computerScore>userScore else '   Congratulations\n\t\t   You win'
            print(f"\n\t\t GAME OVER \n\t    {verdict}\n\n\t User Score is {userScore}\n\t Computer Score is {computerScore}\n\t Total Tied: {tied}")
            play_again = input("Play again? (y/n) ")
            if play_again.lower() != 'y':
                break
            else:
                totalScore=getMaxPoints()
                computerScore = 0
                userScore = 0
                tied = 0

def getMaxPoints():
    validInput = False
    while not validInput:
        totalScore = input("\tEnter maximum points: ")
        try:
            int(totalScore)
        except ValueError as e:
            print("\n\tPlease enter a number\n")
        else:
            validInput = True
    return int(totalScore)

def logic(userInput, computerInput):
    if userInput == 'R' and computerInput == 'S':
        return 'user'
    elif userInput == 'R' and computerInput == 'P':
        return 'computer'
    elif userInput == 'P' and computerInput == 'R':
        return 'user'
    elif userInput == 'P' and computerInput == 'S':
        return 'computer'
    elif userInput == 'S' and computerInput == 'P':
        return 'user'
    elif userInput == 'S' and computerInput == 'R':
        return 'computer'
    else:
        print("\tTied ")
        return 'tied'

if __name__=="__main__":
    run(getMaxPoints())

