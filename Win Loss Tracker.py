import webbrowser
"""
The 'deck' variable is a dictionary with the key being the name of the faced
deck and the value being a list containing 4 values, an int for wins, an int
for losses and the last two variables being strings containing the comments
for those wins and losses(in that order)
"""
def main():
    deckName = input("What is your deck name? ")
    deck = {}
    key = ''
    file = None
    filename = None
    commmand = None
    while (commmand != "quit"):
        command = input("Enter a command(Enter \"help\" for a list of commands): ")

        #lists all commands
        if(command == "help"):
            print("'load' for loading a file")
            print("'save' to save the current file")
            print("'win' records a win for current decks")
            print("'loss' for losses for all listed decks")
            print("'winrate' for winrate percentage")
            print("'show' to show all deck match records")
            print("'update' to show all\n")
            
        #lists wins for all listed decks
        elif(command == "win"):
            deckW = input("What deck did you win against? ")
            commentW = []
            commentW.append(input("Did you have any comments about the match? "))
            if deck.get(deckW) != None:
                deck[deckW][0] += 1
                deck[deckW][2].append(commentW)
            else:
                deck[deckW] = [1, 0, commentW, []]
                
        #lists all losses for all listed decks
        elif(command == "loss"):
            deckS = input("What deck did you lose against? ")
            commentL = []
            commentL.append(input("Did you have any comments about the match? "))
            if deck.get(deckS) != None:
                deck[deckS][1] += 1
                deck[deckS][3].append(commentL)
            else:
                deck[deckS] = [0, 1, [], commentL]
                
        #lists winrate against all listed decks
        elif(command == "winrate"):
            deckWR = input("What deck did you want to see the winrate of?\n(Type 'all' to see the winrate against all recorded decks): ")
            if (deckWR == 'all'):
                for cards in deck:
                    winrate = "%.3f" % ((deck[cards][0] / (deck[cards][0] + deck[cards][1]))* 100)
                    print(deckName,"wins against "+ str(deckWR) + " " + str(winrate) + "% of the time.\n")
            else:
                if deck[deckWR] != None:
                    winrate = "%.3f" % ((deck[deckWR][0] / (deck[deckWR][0] + deck[deckWR][1])) * 100)
                    print(deckName,"wins against "+ str(deckWR) + " " + str(winrate) + "% of the time.\n")
                else:
                    print("Deck does not exist in current set, please add it or check if you spelled it correctly")

        #saves the dictionary to a text file
        elif(command == "save"):
            if len(deck) == 0:
                print("No decks have been loaded!")
            else:
                filename = input("What would you like to name the file? ")
                try:
                    f = open(filename, 'w')
                    for cards in deck:
                        #save deck name
                        f.write(cards + "\n")
                        #saves the wins and losses
                        f.write(str(deck[cards][0]) + "\n")
                        f.write(str(deck[cards][1]) + "\n")
                        #the last two are lists containing commments
                        lt = ''
                        i = 0
                        j = 0
                        lengthW = len(deck[cards][2])
                        lengthL = len(deck[cards][3])
                        #win comments
                        while i < lengthW:
                            if(lengthW == 0):
                                lt = ''
                                i += 1
                            elif(lengthW == 1):
                                lt += ("[" + str(deck[cards][3][0]) + "]%\n")
                                i += 1
                            elif(i == lengthW - 1):
                                lt += ("[" + str(deck[cards][2][i]) + "]%\n")
                                i += 1
                            else:
                                lt += ("[" + str(deck[cards][2][i]) + "]%")
                                i += 1
                                
                        f.write(lt)
                        lt = ''
                        #loss comments
                        while j < lengthL:
                            if (lengthL == 0):
                                lt = ''
                            elif(lengthL == 1):
                                lt += ("[" + str(deck[cards][3][0]) + "]%\n\n")
                                j += 1
                            elif(j == lengthL - 1):
                                lt += ("[" + str(deck[cards][3][j]) + "]%\n\n")
                                j += 1
                            else:
                                lt += ("[" + str(deck[cards][3][j]) + "]%")
                                j += 1
                        f.write(lt)
                finally:
                    f.close()
                    
        #loads the file to the dictionary
        elif(command == "load"):
            fileName = input("What is the name of the file? ")
            thisList = []
            wins = 0
            loss = 0
            i = 0
            f = open(fileName, 'r')
            
            for line in f:
                #read deck name
                if i == 0:
                    key = line
                    parse = key.find('\n')
                    key = key[:parse]
                    i += 1
                #reads match wins and losses
                elif i == 1 or i == 2:
                    parse = line.find('\n')
                    newLn = int(line[:parse])
                    if i == 1:
                        wins = newLn
                    elif i ==2:
                        loss = newLn
                    thisList.append(newLn)
                    i += 1
                #reads the comments in
                elif i == 3 or i == 4:
                    temp = line.split("%")
                    j = 0
                    k = wins
                    if i == 4:
                        k = loss
                    if k == 0:
                        thisList.append('')
                    else:
                        while j <= (k-1):
                            temp[j] = temp[j][1:-1]
                            j += 1
                        temp.remove("\n")
                        thisList.append(temp)
                    i += 1
                #puts deck into dictionary with key value being its name
                else:
                    deck[key] = thisList
                    i = 0
                    thisList = []

        #quits the program
        elif(command == "quit"):
            return 0
        #this will update the wins/losses for the given deck
        elif(command == "update"):
            """
            0 = url is opened in the same browser window if possible
            1 = new browser window if possible
            2 = new browser page (“tab”) is opened if possible
            """
            webbrowser.open('https://www.youtube.com/watch?v=-h5WrWncDZw', new = 1)
        #shows all decks with their wins and losses
        #work on this to eventually show each game with each comment
        #ex. Comments for Wins: \n Game 1: comment 
        elif(command == "show"):
            for cards in deck:
                print(cards, "\nWins: ", deck[cards][0])
                print("\nLosses: ", deck[cards][1])
                
                print("\nComments for Wins against",cards,"\n ")
                i = 1
                print(deck[cards][2])
                for commentsW in deck[cards][2]:
                    print("Win " + str(i) + ":", commentsW,"\n")
                    i += 1

                print("\nComments for Losses against",cards,"\n ")
                i = 1
                for commentsL in deck[cards][3]:
                    print("Loss " + str(i) + ":", commentsL,"\n")
                    i += 1
        else:
            print("Invalid command")


main()
