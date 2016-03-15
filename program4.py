################################################################################
##
##    CS101
##    Bret Smith
##    Program 4 Algorithm
##    March 6, 2016
##
##    PROBLEM:
##        Scramble and unscramble user-specified text files using transposition of letters
##        Program will use functions to create an easy-to-follow set of code.
##        
##    ALGORITHM:
##        Greet user
##        Ask user if they'd like to scramble, unscramble, or quit the program
##        while loop:
##            if user input is in [scramble, unscramble, quit]:
##                break loop to proceed
##            else:
##                prompt user for proper input
##                return to top of loop until proper input
##        if user input == scramble:
##            try loop:
##                get in_file and out_file from user
##                if correct:
##                    break loop to proceed
##            except FileNotFoundError:
##                prompt user for proper in_file name
##                return to top of loop until proper input
##            for loop for line in file:
##                divide lines of file into slices with [::2] and [1::2] increments
##                concatenate two strings created by slices
##                write to out file
##                close in_file and out_file
##            break to display options again
##        elif user input == unscramble
##            try loop:
##                get out_file and second_out_file from user
##                if correct:
##                    break loop to proceed
##            except FileNotFoundError:
##                prompt user for proper out_file name
##                return to top of loop until proper input
##            for loop for line in file:
##                slice each line in half
##                create empty string result for later concatenation
##                find min length of half lines
##                for index in range of min length:
##                    add letter of first half to result
##                    add letter of second half to result
##                    repeat until out of index range
##                if odd length:
##                    add last letter of longest string to end of result string
##                print result to second_out_file
##            close out_file and second_out_file
##            break for options
##        elif user input == quit:
##            sys.exit()
##
##    ERROR HANDLING:
##        while loop for proper choice selection
##        try/except for proper file input
##
##    SPECIAL:
##        scramble function
##        unscramble function
##        get_option function
##        get_file function
##        replay function
##
################################################################################

import sys

# Function Bank
def get_option(output_string, option1, option2, option3):
    """ask user with output_string and check answer in options"""
    while True:
        user = input(output_string + ': \n') # asks defined question
        user = user.lower()
        if user in [option1, option2, option3]: # error checking for options
            return user
        else:
            print("Please enter a valid option.\n")

def get_file(file_string, action):
    """ask user for file with file_string, check availability, and perform action"""
    while True:
        filename = input(file_string + ' ==> ') # asks user for file name
        try:
            file = open(filename, action) # trys to open defined file with action (r,w,a)
        except FileNotFoundError:
            print("We need a valid file name.\n")
        else:
            return file

def scramble(unscrambled_file):
    """takes txt file and applies slices to encrypt to output file"""
    for line in unscrambled_file:
        s= line[::2].strip('\n') # divides line into even indexes
        t= line[1::2].strip('\n') # odd indexes
        result = s + t # concatenates odd to end of even
        print(result, file=out_file)

def unscramble(scrambled_file):
    """takes txt file and applies slices to decrypt 'scramble()' function to output file"""
    for line in scrambled_file:
        s = line[:int(len(line)/2)].strip('\n') # takes first half of each line
        t = line[int(len(line)/2):].strip('\n') # second half
        result2 = ''
        minlength = min(len(s), len(t)) # finds shortest half
        for index in range(minlength): # increments with index and adds letter from each half
            result2 += s[index]
            result2 += t[index]

        if len(s) >= len(t): # ensures final characters are added to result string based on length
            result2 += s[minlength:]
        else:
            result2 += t[minlength:] # concatenates remaining letter on end of result string
            
        print(result2, file=out_file_2)

def print_header():
    """print crytptology header"""
    print("{:^30}".format("Cryptographical Options:"))
    print("1. Scramble (Encrypt File)")
    print("2. Unscramble (Decrypt File)")
    print("Q. Quit\n")

def replay(prompt):
    """ask user prompt for replay of program (Y/Yes/N/No)"""
    while True:
        user = input(prompt + ': \n') # asks user prompt with y/n answer
        user = user.lower()
        if user in ["y", "yes"]: # error checking
            break
        elif user in ["n", "no"]:
            sys.exit()
        else:
            print("Please enter a valid option (Y/Yes/N/No)\n")

while True: # parent loop
    print_header() # presents options and asks user for answer
    choice = get_option("Scramble, unscramble, or quit? (Please use number options)", "1", "2", "q")
        
    if choice == "1": # scramble option
        in_file = get_file("What file would you like to scramble?", "r") # reads their file choice
        out_file = get_file("Name your output text file please.", "w") # writes to designated file
        scramble(in_file) # scrambles in file contents and prints to out file
        in_file.close()
        out_file.close()
        print("Your file has been scrambled.\n")
        replay("Any more files for me? (Y/Yes/N/No)") # ask user if replay wanted

    elif choice == "2": # unscramble option
        out_file = get_file("What file would you like to unscramble?", "r") # reads their file choice
        out_file_2 = get_file("Name your output text file please.", "w") # writes to designated file
        unscramble(out_file) # unscrambles in file contents and prints to out file
        out_file.close()
        out_file_2.close()
        print("Your file has been unscrambled.\n")
        replay("Any more files for me? (Y/Yes/N/No)") # ask replay

    elif choice == "q": # quit option
        sys.exit()
