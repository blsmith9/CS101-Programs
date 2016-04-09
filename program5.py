################################################################################
##
##    CS101
##    Bret Smith
##    Program 5
##    March 27, 2016
##
##    PROBLEM:
##        Convert PPM image at 255 color depth to grayscale and vintage
##        
##    ALGORITHM:
##        Greet user
##        Ask user if they want grayscale, vintage, or quit
##        while loop:
##            if user input is in [grayscale, vintage, quit]:
##                break loop to proceed
##            else:
##                prompt user for proper input
##                return to top of loop until proper input
##        if user input == grayscale:
##            try loop:
##                get in_file and out_file from user
##                if correct:
##                    break loop to proceed
##            except FileNotFoundError:
##                prompt user for proper in_file name
##                return to top of loop until proper input
##            for loop for line in file:
##                check first line to make sure P3
##                    break if wrong header, loop to file input
##                check third line to make sure file at 255 depth
##                    break if wrong depth, loop to file input
##                take .299 * first value (red)
##                take .587 * second value (green)
##                take .114 * third value (blue)
##                print new pixel values to out_file
##            close in_file and out_file
##            break to display options again
##        elif user input == vintage:
##            try loop:
##                get in_file and out_file from user
##                if correct:
##                    break loop to proceed
##            except FileNotFoundError:
##                prompt user for proper in_file name
##                return to top of loop until proper input
##            for loop for line in file:
##                check first line to make sure P3
##                    break if wrong header, loop to file input
##                check third line to make sure file at 255 depth
##                    break if wrong depth, loop to file input
##                take .5 * third value (blue)
##                print new pixel values to out_file
##            close in_file and out_file
##            break for options
##        elif user input == quit:
##            sys.exit()
##
##    ERROR HANDLING:
##        check file handle, header, and color depth
##        while loop for proper choice selection
##        try/except for proper file input
##
##    SPECIAL:
##        get file function
##        get option function
##        replay function
##        grayscale function
##        vintage function
##
################################################################################

import sys

def get_file(file_string, action, handle):
    """ask user for file with file_string, check availability, and perform action"""
    while True:
        filename = input(file_string + ' ==> ') # asks user for file name
        if handle not in filename: # checks designated file handle
            print("We need a valid file with the correct handle. (.ppm)")
            continue
        try:
            file = open(filename, action) # trys to open defined file with action (r,w,a)
        except FileNotFoundError:
            print("Could not locate designated file.\n")
        except Exception:
            print("General Error.\n")
        else:
            return file

def get_option(output_string, option1, option2, option3):
    """ask user with output_string and check answer in options"""
    while True:
        user = input(output_string + ': \n') # asks defined question
        user = user.lower()
        if user in [option1, option2, option3]: # error checking for options
            return user
        else:
            print("Please enter a valid option.\n")

def print_header():
    """print conversion header"""
    print("{:^30}".format("Image Processing Options:"))
    print("1. Convert to Grayscale")
    print("2. Convert to Vintage")
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

def grayscale(file, outfile):
    """enter file and outfile to convert ppm to grayscale"""
    cnt = 0
    while cnt < length: # loop for reading sets of 3 lines
        redgray = 0 # initiate red value/reset for print loop
        bluegray = 0 # blue
        greengray = 0 # green

        for line in file.readlines(1): # read red pixel, strip break, convert to grayscale value
            line_strip = line.strip('\n')
            line_int = int(line_strip)
            redgray = int(line_int * .299)
        for line1 in file.readlines(1): # read green pixel, strip break, convert to grayscale value
            line1_strip = line1.strip('\n')
            line1_int = int(line1_strip)
            greengray = int(line1_int * .587)
        for line2 in file.readlines(1): # read blue pixel, strip break, convert to grayscale value
            line2_strip = line2.strip('\n')
            line2_int = int(line2_strip)
            bluegray = int(line2_int * .114)

        print(redgray + bluegray + greengray, file=outfile) # print sum of pixel values 3 times
        print(redgray + bluegray + greengray, file=outfile)
        print(redgray + bluegray + greengray, file=outfile)
        cnt += 3

def vintage(file, outfile):
    """enter file and outfile to convert ppm to vintage"""
    cnt = 0
    while cnt < length: # loop for reading sets of 3 lines
        redvint = 0 # initiate red/reset for new pixel set
        bluevint = 0 # blue
        greenvint = 0 # green

        for line in file.readlines(1): # reprints red value
            line_strip = line.strip('\n')
            line_int = int(line_strip)
            redvint = line_int
            print(redvint, file=outfile)
        for line1 in file.readlines(1): # reprints green value
            line1_strip = line1.strip('\n')
            line1_int = int(line1_strip)
            greenvint = line1_int
            print(greenvint, file=outfile)
        for line2 in file.readlines(1): # halves blue value, then prints
            line2_strip = line2.strip('\n')
            line2_int = int(line2_strip)
            bluevint = int(line2_int * .5)
            print(bluevint, file=outfile)
        cnt += 3

while True:
    print_header()
    choice = get_option("Grayscale, Vintage, or Quit?", "1", "2", "q") # get user choice function
    if choice in ["1", "2"]:
        while True:
            infile = get_file("Which file would you like to convert?", "r", ".ppm")
            out = get_file("What file would you like to print to?", "w", ".ppm")
            header = infile.readline().strip('\n') # get header, resolution, length of file, color depth
            resolution = infile.readline().strip('\n')
            length = int(resolution.split()[0]) * int(resolution.split()[1]) * 3
            depth = infile.readline().strip('\n')
            if header != "P3": # check header and color depth for error
                print("File did not have correct file header.")
            elif depth != "255":
                print("File did not have correct color depth")
            else:
                break
        if choice == "1": # grayscale option
            print(header, file=out)
            print(resolution, file=out)
            print(depth, file=out)
            grayscale(infile, out)
            infile.close()
            out.close()
            print("Success\n")
            replay("Any more images for me? (Y/Yes/N/No)")
            
        elif choice == "2": # vintage option
            print(header, file=out)
            print(resolution, file=out)
            print(depth, file=out)
            vintage(infile, out)
            infile.close()
            out.close()
            print("Success\n")
            replay("Any more images for me? (Y/Yes/N/No)")
    elif choice == "q": # quit option
        print("Instagram probably would've been easier.")
        sys.exit()
