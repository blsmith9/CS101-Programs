# Bret Smith
# CS 101
# Program 1 Drone Flight Time
# Creation Date Jan 21, 2016
# Due Date Jan 31, 2016
#
# ALGORITHM
# 1. Gain input from user for mAh, # of motors, and amperage draw per motor
# 2. Convert mAh to Ah, calculate total amp draw, and convert that to time
# 3. Present flight time  and total amperage to user in relative units
###########################################################################

# greets user ands asks their name
name = input("Hello! What is your name? \n")
print("Hello,", name)

# asks user for drone battery mAh
mAh = input("How many mAh does your drone battery have? \n")

# asks user for number of drone motors
motors = input("How many motors does your drone have? \n")

# asks user for number of Amps each motor draws
draw = input("How many Amps does each motor draw? \n")

# converts mAh to Ah
Ah = float(mAh) / 1000

# calculates total amps from number of motors and amperage draw
total_amps = float(motors) * float(draw)

# calculates flight hours by dividing Ah by total amps
flight_hours = Ah / total_amps

# converts hours to minutes
flight_minutes = flight_hours * 60

# drops decimal from minutes
flight_minutes_only = int(flight_minutes)

# makes decimal into integer seconds
flight_seconds = int((flight_minutes - flight_minutes_only) * 60)

# prints the results of the calculations
print("Drone Information:\n"
      "Your drone will use", total_amps, "total Amps.\n"
      "Your flight time will be", flight_minutes, "minutes.\n"
      "This converts to", flight_minutes_only, "minutes and", flight_seconds, "seconds.\n")

# if statement prompting different response based on flight time
if flight_minutes_only >= 10:
    print("SKYNET would be proud.")
else:
    print("SKYNET would be disappointed...")
