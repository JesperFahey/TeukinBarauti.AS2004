# Title
print('Quiz about Dusky Dolphins')
print("By Teukin Andreas Barauti")
print()
score=0

# Imports
import os # With os I can clear the screen which is pretty swag
import time # I can pause my program now! :D

# Instructions
print("This quiz will have 6 questions about Dusky Dolphins")
print()
print("You're just going to see how many you can get correct.")

# Input
print()
name = input("Hello! What is your name? ")
print()
print("Hello {}, welcome to my quiz about Dusky Dolphins!".format(name))


# Questions
print('Q.1. Do Dusky Dolphins have beaks?\n A. Yes  \n B. No')
Answer_1 = input('Answer: ')
# Answer for Q.1
if Answer_1 == 'B':
    print('Great Job!')
else:
    print('Wrong! But good guess!')
if Answer_1 == "B":
    score = score+1
    print('One point has been added to your score! {}'.format(score))
time.sleep(3)
os.system('clear)
print('Q.2. What is the estimated population of Dusky Dolphins? \n A. 1000 \n B. 12000 \n C. 1500 \n D. 5000000')
Answer_2 = input('Answer: ')
# Answer for Q.2
if Answer_2 == "B":
    print("Correct again! Man you're a natural")
else:
    print('Nice try, but try harder!')
if Answer_2 == "B":
    score = score+2
    print("2 points have now been added to your score {}, {}".format(name, score))
print('Q.3. Where are Dusky Dolphins confined? \n A. The Northern Hemisphere \n B. The Western Hemisphere \n C The Southern Hemisphere  \n D. The Eastern Hemisphere')
Answer_3 = input("Answer: ")
# Answer for Q.3
if Answer_3 == "C":
    print("Wow! I didn't expect you to get that {}! Congrats!".format(name))
else:
    print("Oof! Nice try! You'll get there!")
if Answer_3 == "C":
    score = score+3
    print("3 points have been added to your score {}! {}".format(name, score))
print()
print("Q.4. What colour are Dusky Dolphins? \n A. Blue and black \n B. Orange and Brown \n C. Lilac and Baby Blue \n D. White and Black")
Answer_4 = input("Answer: ")
# Answer for Q.4
if Answer_4 == "A":
    print("Again with more points scored!")
else:
    print("Man, I'm losing faith in you my friend")
if Answer_4 == "A":
    score = score+4
    print("Congrats {}! Here's 4 points for getting that question correct! {}".format(name, score))
print()
print()
print("Okay, this is the next one! Oh, and your points will be doubled! Good luck {}!".format(name))
print("Here's the 5th question!")
print()
print("Q.5. What types of food do they eat? \n A. Anchovies \n B. Hake \n C. Squid \n D. All of the above")
Answer_5 = input("Answer: ")
# Answer for Q.5
if Answer_5 == "D":
    print("WOW! Okay then! I was definitely not expecting it to be that easy... Good job {}!".format(name))
else:
    print("Damn. So close! Hey, don't give up yet. You might get the last question right! I believe in you {}!".format(name))
if Answer_5 == "D":
    score = score*2
    print("As promised, here's your double points! {}".format(score))
print()
print()
print("Now for the great finale! This is the final question!")
print("Which of the following is a characteristic behavior of Dusky Dolphins? \n A. They migrate long distances between continents. \n B. They are often seen in large pods, exhibiting synchronized swimming patterns. \n C. They exclusively live in deep ocean waters far from coastlines. \n D. They communicate using distinct, non-vocal methods such as color changes.")
Answer_6 = input("Answer: ")
# Answer for Q.6
if Answer_6 == "B":
    print("Wow! You did amazing {}!".format(name))
else:
    print("Well, better luck next time my friend! The answers will be at the bottom of the quiz!")
if Answer_6 == "B":
    score = score*3
    print("Forgot to metion your score is tripled, because you got it right! Good job {}! {}".format(name, score))
print()
print()
if score < 60:
    print("You could've done so much better!")
else:
    print("I'm so happy you got all 6 questions correct!")
