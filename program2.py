################################################################################
##
##    CS101
##    Bret Smith
##    Program 2
##    February 14, 2016
##
##    PROBLEM:
##        Get luggage from origin to destination while counting hops, max hops,
##        and outputting each trial
##
##    ALGORITHM:
##        get input from user to determine number of trials
##        convert input to int
##        if trials <= 0:
##            prompt error, ask for number >= 1
##            return to input of trials
##        if trials > 0:
##            ask if detailed output is wanted
##            convert input to lower case
##            if input == (y, yes, n, no):
##                proceed
##                if input == (y, yes)
##                    print each trial
##                else:
##                    do not print each trial
##                    skip to on time percentage and max hops
##            else:
##                prompt error, ask for correct input
##                return to input of detailed output
##            while loop percentage chances of arriving at each destination:
##                use random.randint() to generate random numbers
##                use random number ranges to based on percentages to print destinations
##                once intermediate destination is reached, calculate new percentages in loop until HNL
##                count hops to reach final destination
##                if hops <=2:
##                    arrival is on time
##                else:
##                    arrival is not on time
##                keep track of maximum hops
##
##            when final destination is reached, break loop
##            take ontime / total trials to get on time percentage
##            display max hops
##
##            ask user input to run again
##            convert input to lower case
##            if input != (y, yes, n, no):
##                prompt error, ask for correct input
##            if input == (y, yes):
##                return to beginning of program
##            if input == (n, no):
##                exit program
##
##    ERROR HANDLING:
##        trial input error if trial int <= 0
##        detailed output error if input != (y, yes, n, no)
##        run program again error if input != (y, yes, n, no)
##
################################################################################

# various info repeats, so similar code below initial comment holds similar function

import random
import sys

print("Welcome to 'Where In The World Is My Luggage?'") # User Greeting
print("This game was created to track your bags!\n")

while True: # parent while loop
    trials = input("How many luggage trials would you like to run? \n") # asks for trial input
    try:
        trials = int(trials)
    except ValueError: # stops non int input
        print("We need a positive number, please.")
    else:
        if trials <= 0: # stops non positive int input
            print("We need a positive number, please.")
            continue
        if trials > 0:
            isdetail = True
            while isdetail == True: # initializes loop for detailed output
                details = input("Would you like detailed output for each trial? (Y/Yes/N/No) \n")
                if details.lower() not in ["y", "yes", "n", "no"]:
                    print("Please answer (Y/Yes/N/No)") # stops unwanted input
                    continue
                if details.lower() in ["y", "yes", "n", "no"]:
                    port = "MCI" # port directs what set of percentages the trial goes to
                    count = 0 # keeps track of number of trials
                    hops = 0 # keeps track of hops per trial
                    maxhops = 0 # keeps track of max hops
                    ontime = 0 # keeps track of trials w/ <= 2 hops
                    if details.lower() in ["y", "yes"]: # if detail is wanted, each trial has a print statement
                        isdetail = False # sets loop variable to false so after desired trial, loop stops
                        
                        while count in range(0, trials): # loops for number of trial input
                            if port == "MCI": # percentages for MCI destinations
                                prob1 = random.randint(1,10) # initializes random number
                                if 1 <= prob1 <= 4: # probability based on random number
                                    print("MCI => ",end = "") # prints current airport
                                    print("LVS => ",end = "")
                                    port = "LVS" # sets port for next portion of loop
                                    hops += 1 # increments hops
                                elif 5 <= prob1 <= 7:
                                    print("MCI => ",end = "")
                                    print("SEA => ",end = "")
                                    port = "SEA"
                                    hops += 1
                                else:
                                    print("MCI => ",end = "")
                                    print("HNL")
                                    port = "MCI" # resets port to MCI for new trial
                                    count += 1 # increments count for trial number
                                    hops += 1
                                    if hops <= 2:
                                        ontime += 1 # increments on time for later percentage
                                    if hops >= maxhops:
                                        maxhops = hops # sets max hops to highest hop value
                                    if count < trials: # keeps trials from printing 1 more than necessary
                                        print("Trial", count + 1, ": \t", end = "")
                                    hops = 0 # resets hops after max hops found for next trial
                            if port == "LVS": # if port matches, LVS percentages calculated here
                                prob2 = random.randint(1,10)
                                if 1 <= prob2 <= 3:
                                    port = "MCI"
                                    hops += 1
                                elif 4 <= prob2 <= 8:
                                    print("SEA => ",end = "")
                                    port = "SEA"
                                    hops += 1
                                else:
                                    print("HNL")
                                    port = "MCI"
                                    count += 1
                                    hops += 1
                                    if hops <= 2:
                                        ontime += 1
                                    if hops >= maxhops:
                                        maxhops = hops
                                    if count < trials:
                                        print("Trial", count + 1, ": \t", end = "")
                                    hops = 0
                            if port == "SEA": # if port matches, SEA percentages calculated here
                                prob3 = random.randint(1,10)
                                if prob3 <= 1:
                                    port = "MCI"
                                    hops += 1
                                elif 2 <= prob3 <= 7:
                                    print("LVS => ",end = "")
                                    port = "LVS"
                                    hops += 1
                                else:
                                    print("HNL")
                                    port = "MCI"
                                    count += 1
                                    hops += 1
                                    if hops <= 2:
                                        ontime += 1
                                    if hops >= maxhops:
                                        maxhops = hops
                                    if count < trials:
                                        print("Trial", count + 1, ": \t", end = "")
                                    hops = 0

                    if details.lower() in ["n", "n"]: # same as above, only without print statements
                        isdetail = False
                        while count in range(0, trials):
                            if port == "MCI":
                                prob1 = random.randint(1,10)
                                if 1 <= prob1 <= 4:
                                    port = "LVS"
                                    hops += 1
                                elif 5 <= prob1 <= 7:
                                    port = "SEA"
                                    hops += 1
                                else:
                                    port = "MCI"
                                    count += 1
                                    hops += 1
                                    if hops <= 2:
                                        ontime += 1
                                    if hops >= maxhops:
                                        maxhops = hops
                                    hops = 0
                            if port == "LVS":
                                prob2 = random.randint(1,10)
                                if 1 <= prob2 <= 3:
                                    port = "MCI"
                                    hops += 1
                                elif 4 <= prob2 <= 8:
                                    port = "SEA"
                                    hops += 1
                                else:
                                    port = "MCI"
                                    count += 1
                                    hops += 1
                                    if hops <= 2:
                                        ontime += 1
                                    if hops >= maxhops:
                                        maxhops = hops
                                    hops = 0
                            if port == "SEA":
                                prob3 = random.randint(1,10)
                                if prob3 <= 1:
                                    port = "MCI"
                                    hops += 1
                                elif 2 <= prob3 <= 7:
                                    port = "LVS"
                                    hops += 1
                                else:
                                    port = "MCI"
                                    count += 1
                                    hops += 1
                                    if hops <= 2:
                                        ontime += 1
                                    if hops >= maxhops:
                                        maxhops = hops
                                    hops = 0

        percentontime = float((ontime/trials)*100) # calculates percentage of on time trials
        print("\nYour actual on-time arrivals were: (",ontime, "/", trials,")") # displays on time vs total trials
        print("Your on-time percentage was: ","%.3f" % percentontime, "%") # displays actual percentage with 3 decimals
        print("Your max hops were:", maxhops) # displays max hops
        if percentontime < 30.0:
            print("Did Delta seem like the best choice?") # showing my respect for delta
            
        while True: # replay loop initialized after info display
            replay = input("\nWould you like to run another trial set? (Y/Yes/N/No) \n")
            if replay.lower() in ["y", "yes"]: # breaks loop and returns to top of parent while loop
                break
            if replay.lower() in ["n", "no"]: # exits program
                sys.exit()
            if replay.lower() not in ["y", "yes", "n", "no"]: # stops unwanted input
                print("Please answer (Y/Yes/N/No)")
                continue
