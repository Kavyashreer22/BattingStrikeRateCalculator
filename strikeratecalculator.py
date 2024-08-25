#Batting Strike rate calculator
#Runs per 100 balls i.e. it is an average per 100 balls
print("Welcome to the Batting Strike rate calculator created by KavyaShree R")
name=input("Please enter the name of the batsman:")
r = input("Please enter the runs scored by the batsman: ")
b = input("Please enter the number of balls played by the batsman: ")
r = int(r)
b = int(b)
avg=r/b
sr=avg*100
print("The strike rate of the batsman is", sr)

