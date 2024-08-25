#Batting Strike rate calculator
#Runs per 100 balls i.e. it is an average per 100 balls
# Print a welcome message for the user
  print("Welcome to the Batting Strike rate calculator created by KavyaShree R")

# Prompt the user to enter the name of the batsman
  name=input("Please enter the name of the batsman:")

# Prompt the user to enter the runs scored by the batsman
  r = input("Please enter the runs scored by the batsman: ")
# Prompt the user to enter the number of balls played by the batsman
  b = input("Please enter the number of balls played by the batsman: ")
# Convert the runs and balls input from string to integer
  r = int(r)
  b = int(b)
# Calculate the average runs per ball
  avg=r/b
# Calculate the strike rate by multiplying the average by 100
  sr=avg*100
# Print the strike rate of the batsman
  print("The strike rate of the batsman is", sr)

