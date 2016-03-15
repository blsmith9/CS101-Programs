################################################################################
##
##    CS101
##    Bret Smith
##    Program 3
##    February 28, 2016
##
##    PROBLEM:
##        Provide user with random string and slice based on choice of difficulty.
##        Assess their answer and give points if answer matches.
##
##    ALGORITHM:
##        Greet User
##        get user input for number of desired rounds using loop:
##            if input is < 0 or > 20, show error and return to
##            user input in correct range
##        once user enters correct rounds, ask for input of difficulty in loop:
##            if input isnt in range, show error and return to
##            top of loop for correct input
##        once user enters valid difficulty:
##            ask if hint indexes are wanted:
##                yes:
##                    display index with format over string
##                no:
##                    break to slice generation
##                else:
##                    promt error and ask for correct input
##            if difficulty == easy:
##                length of string limited to 5
##                generate random string using random.choice()
##                and ascii letters
##                generate random slice using random.randint where
##                all are <= length of the string
##                loop until number of rounds are met
##                keep track if user input == actual slice
##                increment points for correct slices
##            if difficulty == medium:
##                length of string limited to 7
##                generate random string using random.choice()
##                and ascii letters
##                generate random slice using random.randint where
##                all are <= length of the string
##                loop until number of rounds are met
##                keep track if user input == actual slice
##                increment points for correct slices
##            if difficulty == hard:
##                length of string limited to 10
##                generate random string using random.choice()
##                and ascii letters
##                generate random slice using random.randint where
##                all are <= length of the string:
##                    use random.randint() to generate negative slice start chance
##                    use random.randint() to generate negative slice end chance
##                    use random.randint() to generate reverse slice chance
##                    use random.randint() to generate interval chance
##                loop until number of rounds are met
##                keep track if user input == actual slice
##                increment points for correct slices
##        print fraction of user correct and percentage
##        ask user if they'd like to play again:
##            if answer isn't y, yes, n, or no:
##                prompt error and ask again
##            if answer is yes:
##                return to beginning of game
##            if answer is no:
##                sys.exit()
##
##    ERROR HANDLING:
##            play again try/except to make sure user enters y, yes, n, or no
##            number of rounds try/except to make sure user inters integer in range
##            difficulty try/except to make sure user enters integer in range
##            hints try/except to make sure user enters y, yes, n, or no
##
################################################################################

import string
import random
import sys

while True: # parent loop
    score = 0
    print("Welcome to Slice and Dice.")
    while True: # round input loop with try/except
        try:
            trials = int(input("How many rounds would you like to play? (1-20)\n"))
            if trials <= 0 or trials > 20:
                print("Give me a number between 1 and 20")
                continue
        except ValueError:
            print("Give me a number between 1 and 20")
        else:
            break

    while True: # difficulty input loop with try/except
        try:
            difficulty = int(input("Difficulty selection: 1 = Easy, 2 = Medium, 3 = Hard\n"))
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Please enter a valid difficulty")
                continue
        except ValueError:
            print("Please enter a valid difficulty")
        else:
            break

    if difficulty == 1: # easy mode
        hint = input("Do you want to display hint indexes? (Y/YES/N/NO)\n")
        indexfwd = "01234" # hint indexes
        indexrev = "-54321"
        for rnd in range(trials): # loops based on trial (round) number
            s = ''
            while len(s) < 5: #builds random string
                char = random.choice(string.ascii_letters)
                s += char

            # picks random numbers for slices in first and second half of string
            firsthalf = random.randint(0, int(len(s)//2))
            secondhalf = random.randint(int((len(s)//2)+1), len(s))
            slce = s[firsthalf:secondhalf] # makes slice
            display = "[{0}:{1}:]".format(str(firsthalf), str(secondhalf)) # displays slice

            while True: # hint loop with error handling
                if hint.lower() in ["y", "yes"]:
                    print("{:>13}".format(indexfwd))
                    print("{:>13}".format(indexrev))
                    break
                elif hint.lower() in ["n", "no"]:
                    break
                else:
                    print("Please enter a valid answer")
                    hint = input("Do you want to display hint indexes? (Y/YES/N/NO)\n")

            # asks user to enter their guess
            user = input("What is {0} with slice {1}?\n".format(s,display))

            if user == slce: # gives points
                print("Correct, slice was: ", slce, "\n")
                score += 1
            else:
                print("Sorry, slice was:", slce, "\n")

    elif difficulty == 2: # medium mode
        hint = input("Do you want to display hint indexes? (Y/YES/N/NO)\n")
        indexfwd = "0123456"
        indexrev = "-7654321"
        for rnd in range(trials):
            s = ''
            while len(s) < 7:
                char = random.choice(string.ascii_letters)
                s += char

            firsthalf = random.randint(0, int(len(s)//2))
            secondhalf = random.randint(int((len(s)//2)+1), len(s))
            slce = s[firsthalf:secondhalf]
            display = "[{0}:{1}:]".format(str(firsthalf), str(secondhalf))

            while True:
                if hint.lower() in ["y", "yes"]:
                    print("{:>15}".format(indexfwd))
                    print("{:>15}".format(indexrev))
                    break
                elif hint.lower() in ["n", "no"]:
                    break
                else:
                    print("Please enter a valid answer")
                    hint = input("Do you want to display hint indexes? (Y/YES/N/NO)\n")

            user = input("What is {0} with slice {1}?\n".format(s,display))

            if user == slce:
                print("Correct, slice was: ", slce, "\n")
                score += 1
            else:
                print("Sorry, slice was:", slce, "\n")

    elif difficulty == 3: # hard mode
        hint = input("Do you want to display hint indexes? (Y/YES/N/NO)\n")
        indexfwd = "0123456789"
        indexrev = "-0987654321"
        for rnd in range(trials):
            s = ''
            while len(s) < 10:
                char = random.choice(string.ascii_letters)
                s += char
            firsthalf = random.randint(1, int(len(s)//2))
            secondhalf = random.randint(int((len(s)//2)+1), len(s))
            dupfirsthalf = random.randint(1, int(len(s)//2)) # so randint doesn't repeat for certain slice parameters
            dupsecondhalf = random.randint(int((len(s)//2)+1), len(s))

            startslice = random.randint(1,4) # probability of each parameter for hard
            endslice = random.randint(1,4)
            revslice = random.randint(1,4)
            intervalslice = random.randint(1,5)

            while True: # determines hard parameters
                if startslice == 1: # probability start slice negative chain
                    if startslice == endslice:
                        if startslice == endslice == revslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:-secondhalf:-1]
                                display = "[{0}:{1}:-1]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif startslice == endslice == intervalslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-secondhalf:-firsthalf:2]
                                display = "[{1}:{0}:2]".format(str(-firsthalf), str(-secondhalf))
                                break
                        else:
                            slce = s[-secondhalf:-firsthalf]
                            display = "[{1}:{0}:]".format(str(-firsthalf), str(-secondhalf))
                            break

                    elif startslice == revslice:
                        if startslice == revslice == endslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:-secondhalf:-1]
                                display = "[{0}:{1}:-1]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif startslice == revslice == intervalslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:dupfirsthalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(dupfirsthalf))
                                break
                        else:
                            slce = s[-firsthalf:dupfirsthalf:-1]
                            display = "[{0}:{1}:-1]".format(str(-firsthalf), str(dupfirsthalf))
                            break

                    elif startslice == intervalslice:
                        if startslice == intervalslice == revslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:dupfirsthalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(dupfirsthalf))
                                break

                        elif startslice == intervalslice == endslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-secondhalf:-firsthalf:2]
                                display = "[{1}:{0}:2]".format(str(-firsthalf), str(-secondhalf))
                                break
                        else:
                            slce = s[-secondhalf:dupsecondhalf:2]
                            display = "[{1}:{0}:2]".format(str(dupsecondhalf), str(-secondhalf))
                            break
                    
                    else:
                        slce = s[-secondhalf:dupsecondhalf]
                        display = "[{1}:{0}:]".format(str(dupsecondhalf), str(-secondhalf))
                        break
                elif endslice == 1: # probability end slice negative chain
                    if endslice == startslice:
                        if endslice == startslice == revslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:-secondhalf:-1]
                                display = "[{0}:{1}:-1]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif endslice == startslice == intervalslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-secondhalf:-firsthalf:2]
                                display = "[{1}:{0}:2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            
                        else:
                            slce = s[-secondhalf:-firsthalf]
                            display = "[{1}:{0}:]".format(str(-firsthalf), str(-secondhalf))
                            break

                    elif endslice == revslice:
                        if endslice == revslice == startslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:-secondhalf:-1]
                                display = "[{0}:{1}:-1]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif endslice == revslice == intervalslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[secondhalf:-dupsecondhalf:-2]
                                display = "[{1}:{0}:-2]".format(str(-dupsecondhalf), str(secondhalf))
                                break

                        else:
                            slce = s[secondhalf:-dupsecondhalf:-1]
                            display = "[{1}:{0}:-1]".format(str(-dupsecondhalf), str(secondhalf))
                            break

                    elif endslice == intervalslice:
                        if endslice == intervalslice == startslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-secondhalf:-firsthalf:2]
                                display = "[{1}:{0}:2]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif endslice == intervalslice == revslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[secondhalf:-dupsecondhalf:-2]
                                display = "[{1}:{0}:-2]".format(str(-dupsecondhalf), str(secondhalf))
                                break

                        else:
                            slce = s[firsthalf:-dupfirsthalf:2]
                            display = "[{0}:{1}:2]".format(str(firsthalf), str(-dupfirsthalf))
                            break

                    else:
                        slce = s[firsthalf:-dupfirsthalf]
                        display = "[{0}:{1}:]".format(str(firsthalf), str(-dupfirsthalf))
                        break
                    
                elif revslice == 1: # probability slice is reversed chain
                    if revslice == startslice:
                        if startslice == revslice == endslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:-secondhalf:-1]
                                display = "[{0}:{1}:-1]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif startslice == revslice == intervalslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:dupfirsthalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(dupfirsthalf))
                                break
                        else:
                            slce = s[-firsthalf:dupfirsthalf:-1]
                            display = "[{0}:{1}:-1]".format(str(-firsthalf), str(dupfirsthalf))
                            break

                    elif revslice == endslice:
                        if endslice == revslice == startslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:-secondhalf:-1]
                                display = "[{0}:{1}:-1]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif endslice == revslice == intervalslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[secondhalf:-dupsecondhalf:-2]
                                display = "[{1}:{0}:-2]".format(str(-dupsecondhalf), str(secondhalf))
                                break

                        else:
                            slce = s[secondhalf:-dupsecondhalf:-1]
                            display = "[{1}:{0}:-1]".format(str(-dupsecondhalf), str(secondhalf))
                            break

                    elif revslice == intervalslice:
                        if revslice == intervalslice == startslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:dupfirsthalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(dupfirsthalf))
                                break

                        elif revslice == intervalslice == endslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[secondhalf:-dupsecondhalf:-2]
                                display = "[{1}:{0}:-2]".format(str(-dupsecondhalf), str(secondhalf))
                                break

                        else:
                            slce = s[secondhalf:firsthalf:-2]
                            display = "[{1}:{0}:-2]".format(str(firsthalf), str(secondhalf))
                            break
                    else:
                        slce = s[secondhalf:firsthalf:-1]
                        display = "[{1}:{0}:-1]".format(str(firsthalf), str(secondhalf))
                        break
                    
                elif intervalslice == 1: # probability slice has '2' as interval chain
                    if intervalslice == startslice:
                        if startslice == intervalslice == revslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:dupfirsthalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(dupfirsthalf))
                                break

                        elif startslice == intervalslice == endslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-secondhalf:-firsthalf:2]
                                display = "[{1}:{0}:2]".format(str(-firsthalf), str(-secondhalf))
                                break
                        else:
                            slce = s[-secondhalf:dupsecondhalf:2]
                            display = "[{1}:{0}:2]".format(str(dupsecondhalf), str(-secondhalf))
                            break

                    elif intervalslice == endslice:
                        if endslice == intervalslice == startslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-secondhalf:-firsthalf:2]
                                display = "[{1}:{0}:2]".format(str(-firsthalf), str(-secondhalf))
                                break

                        elif endslice == intervalslice == revslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[secondhalf:-dupsecondhalf:-2]
                                display = "[{1}:{0}:-2]".format(str(-dupsecondhalf), str(secondhalf))
                                break

                        else:
                            slce = s[firsthalf:-dupfirsthalf:2]
                            display = "[{0}:{1}:2]".format(str(firsthalf), str(-dupfirsthalf))
                            break

                    elif intervalslice == revslice:
                        if revslice == intervalslice == startslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[-firsthalf:dupfirsthalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(dupfirsthalf))
                                break

                        elif revslice == intervalslice == endslice:
                            if startslice == endslice == revslice == intervalslice:
                                slce = s[-firsthalf:-secondhalf:-2]
                                display = "[{0}:{1}:-2]".format(str(-firsthalf), str(-secondhalf))
                                break
                            else:
                                slce = s[secondhalf:-dupsecondhalf:-2]
                                display = "[{1}:{0}:-2]".format(str(-dupsecondhalf), str(secondhalf))
                                break

                        else:
                            slce = s[secondhalf:firsthalf:-2]
                            display = "[{1}:{0}:-2]".format(str(firsthalf), str(secondhalf))
                            break

                    else:
                        slce = s[firsthalf:secondhalf:2]
                        display = "[{0}:{1}:2]".format(str(firsthalf), str(secondhalf))
                        break
                else:
                    slce = s[firsthalf:secondhalf]
                    display = "[{0}:{1}:]".format(str(firsthalf), str(secondhalf))
                    break

            while True:
                if hint.lower() in ["y", "yes"]:
                    print("{:>18}".format(indexfwd))
                    print("{:>18}".format(indexrev))
                    break
                elif hint.lower() in ["n", "no"]:
                    break
                else:
                    print("Please enter a valid answer")
                    hint = input("Do you want to display hint indexes? (Y/YES/N/NO)\n")

            user = input("What is {0} with slice {1}?\n".format(s,display))

            if user == slce:
                print("Correct, slice was: ", slce, "\n")
                score += 1
            else:
                print("Sorry, slice was:", slce, "\n")
    percent = "{:>8.3f}".format((score/trials) * 100) # shows user correct and %
    print("You got ( {0} / {1} ) which is {2} %".format(score, trials, percent))

    while True: # replay loop with error handling
        replay = input("Would you like to play again? (Y/YES/N/NO)\n")
        if replay.lower() in ["y", "yes"]: # returns to top of parent loop
            break
        elif replay.lower() in ["n", "no"]: # exits program
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Please enter a valid answer")
