'''This is a quiz for submission in DIGITEC1
   based on Dusky Dolphins
   which is very interesting (In my opinion at least)'''

# Title
print('Quiz about Dusky Dolphins')
print("By Teukin Andreas Barauti")

# Import
import os # with os I can clear the screen which is pretty swag
import time # I can pause my program now! :D
print()
score=0

# Input a user name! :D
name = input("Hello! What is your name? ")
print()
print("Hello {}, welcome to my quiz about Dusky Dolphins!".format(name))

# Instructions
print("This quiz will have 6 questions about Dusky Dolphins")
print()
print("You're just going to see how many you can get correct.")

#This is a list containing the Questions! :D
questionlist = [
'Q1: Do Dusky Dolphins have beaks? \n A: Yes \n B: No  \n', 
'Q2: What is the estimated population of Dusky Dolphins \n A: 1200 \n B: 12000 \n C: 20000 \n D: 321053  \n', 
'Q3: Where are Dusky Dolphins Confined? \n A: The Northern Hemisphere \n B: The Eastern Hemisphere \n C: The Southern Hemisphere \n D: The Western Hemisphere  \n',
'Q4: What colour are Dusky Dolphins? \n A: Blue and Black \n B: Yellow and Gold \n C: White and Green \n D: Red and Purple  \n',
'Q5: What types of food do they eat? \n A: Anchovies \n B: Hake \n C: Squid \n D: All of the above  \n',
'Q6: What age do Dusky Dolphins reach sexual maturity? \n A: 7 \n B: 10 \n C: 20 \n D: 15  \n']
answer_list = ['no', '12000', 'the southern hemisphere', 'blue and black', 'all of the above', '7']

# This is how I chose to display the questions
for i in range(len(questionlist)): # Repeats questions until there are no more to state/ask
    answer = input(questionlist[i])
    if answer.lower()== answer_list[i].lower():
        score += 10
        print("Congrats! \n You got some more points! \n Your score is now {}".format(score))
        time.sleep(3)
        os.system('clear')
    else:
        print("Yikes, that was incorrect! \n Until you get a question right, your score will stay at: {}".format(score))
        time.sleep(3)
        os.system('clear')
            
print("Okay, here are your results!{}/60".format(score))
print("Thanks for learning about Dusky Dolphins \n I hope you enjoyed it!")
time.sleep(3)
os.system('clear')

if score == 60:
    print("Congrats! You did a very good job and appear to know more than the average person in terms of Dusky Dolphins!")
else:
    print("To think I had such high hopes for you... No matter, perhaps you should study more.")

