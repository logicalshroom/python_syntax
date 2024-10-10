# Objective 1 Task 1 : Code Correction

# We aim to understand the importance of indentation using if statements. Correct the code below.

#I've commented out the bad code.

#weather = "sunny"

#if weather == "sunny":
#print("Wear sunglasses!")
#else:
#print("Take an umbrella!")

# Here's my answer:

weather = "sunny" #this is fine, we dont need to indent variables

if weather == "sunny":
    print("Wear sunglasses!") #indented, since we want this inside the above if statement
else: #else will run on the same indent as if, so this should work fine.
    print("Take an umbrella!") #inside the else statement

# Objective 1 Task 2 : Your Mood Today

# Ask the user how they feel today.

# If they say "happy", print, "That's great to hear!",
# If they say "sad", print "I hope your day get's better!"
# Ensure proper indendation, and used the input() function.

mood = input("How are you feeling today? (happy/sad)")

if mood == "happy":
    print("That's great to hear!")
else:
    print("I hope your day get's better!")