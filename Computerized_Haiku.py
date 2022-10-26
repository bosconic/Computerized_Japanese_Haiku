"""
Submitted by: Nicholas Bosco
Student Number: 1005271171
Submitted to: Prof Maher Elshakankiri
Midterm Assignemnt INF451
Topic: Computerized Japanese Haiku using Python
Date Created: 2022-10-25
Date Submitted: 2022-11-2
"""

# Preamble: I would like to inset an image of the page onto python to show user the lists and semantic schema (diagram). 
# The code to import images was found here: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

print(f'Please read the image carefully as it will be your guide to generate your very own Haiku')


from PIL import Image #installing pillow library and calling for images
myImage = Image.open("computerized_haiku_template.png")
myImage.show()


#Step 1 generate lists copied from readme file source 
slot1 = ['White', 'Blue', 'Red', 'Black', 'Grey', 'Green', 'Brown', 'Bright', 'Pure', 'Curved', 'Crowned', 'Starred'] # remember next randomized word is either from slot4 or slot5
slot2 = ['Buds', 'Twigs', 'Leaves', 'Hills', 'Peaks', 'Snow', 'Ice', 'Sun','Rain', 'Cloud', 'Sky', 'Dawn', 'Dusk', 'Mist', 'Fog', 'Spring', 'Heat', 'Cold' ] # remember next randomized word is either from slot5 or slot6
slot3 = ['See', 'Trace', 'Glimpse', 'Flash', 'Smell', 'Taste', 'Hear', 'Seize'] # remember next randomized word is from slot5
slot4 = ['Snow', 'Tall', 'Pale', 'Dark', 'Faint', 'White', 'Clear', 'Red', 'Blue', 'Green', 'Grey', 'Black', 'Round', 'Square', 'Straight', 'Curved', 'Slim', 'Fat', 'Burst', 'Thin', 'Bright'] # remember next randomized word is either from slot6 or slot7
slot5 = ['Trees', 'Peaks', 'Hills', 'Streams', 'Birds', 'Specks', 'Arcs', 'Grass', 'Stems', 'Sheep', 'Cows', 'Deer', 'Stars', 'Clouds', 'Flowers', 'Buds', 'Leaves', 'Trees', 'Pools', 'Drops', 'Stones', 'Bells', 'Trails'] # remember next randomized word is from slot8
slot6 = ['Spring', 'Full', 'Cold', 'Heat', 'Sun', 'Shade', 'Dawn', 'Dusk', 'Day', 'Night', 'Mist', 'Trees', 'Woods', 'Hills', 'Pools'] # remember the next randomized word is from slot2
slot7 = ['Bang', 'Hush', 'Swish', 'Pffftt', 'Whizz', 'Flick', 'Shoo', 'Grr', 'Whirr', 'Look', 'Crash'] # not links proceeding this slot
slot8 = ['Sun', 'Moon', 'Star', 'Cloud', 'Storm', 'Streak', 'Tree', 'Flower', 'Bud', 'Leaf', 'Child', 'Crane', 'Bird', 'Plane', 'Moth'] # remember the next randomized word is from slot5
slot9 = ['Flit', 'Fled', 'Dimmed', 'Cracked', 'Passed', 'Shrunk', 'Smashed', 'Blown', 'Sprung', 'Crashed', 'Gone', 'Fogged', 'Burst']

# Step 2 generate user input
print(f'Would you like to try and generate your own haiku?')

volunteerChoice = str(input("Please enter either yes or no "))

if volunteerChoice == "yes":
    print(f'Look at slot1 and choose a word')
else:
    print(f'Come back when you want to try')
    exit() # program stops if no is selected

#randomized choices chosen ahead of time so I am making some variables global
import random
print(f'Computer is now choosing words from list provided')

randomized_slotchoice1 = random.choice(slot1)
randomized_slotchoice2 = random.choice(slot2)
randomized_slotchoice3 = random.choice(slot3)
randomized_slotchoice4 = random.choice(slot4)
randomized_slotchoice5 = random.choice(slot5)
randomized_slotchoice6 = random.choice(slot6)
randomized_slotchoice7 = random.choice(slot7)
randomized_slotchoice8 = random.choice(slot8)
randomized_slotchoice9 = random.choice(slot9)

#slot1 VolunteerResponseslot1 then we have to see if it is the same as slot4 or slot5
volunteerResponse_slot1 = str(input("Enter your first chosen word here: "))


if volunteerResponse_slot1 != randomized_slotchoice4 or randomized_slotchoice5:
    print(f'your choice has been taken into consideration')
else:
    print(f'Great minds think alike')


#slot2 VolunteerResponse_slot2 then we have to see if it is the same as slot5 or slot6
volunteerResponse_slot2 = str(input("Enter your second chosen word here: "))

if volunteerResponse_slot2 != randomized_slotchoice5 or randomized_slotchoice6:
    print(f'your choice has been taken into consideration')
else:
    print(f'Great minds think alike')

#slot3 VolunteerResponse_slot3 then we have to see if it is the same as slot5
volunteerResponse_slot3 = str(input("Enter your third chosen word here: "))

if volunteerResponse_slot3 != randomized_slotchoice5:
    print(f'your choice has been taken into consideration')
else:
    print(f'Great minds think alike')

#slot4 VolunteerResponse_slot4 then we have to see if it is the same as slot6 or slot7
volunteerResponse_slot4 = str(input("Enter your four chosen word here: "))

if volunteerResponse_slot4 != randomized_slotchoice6 or randomized_slotchoice7:
    print(f'your choice has been taken into consideration')
else:
    print(f'Great minds think alike')


#slot5 VolunteerResponse_slot5 then we have to see if it is the same as slot8
volunteerResponse_slot5 = str(input("Enter your five chosen word here: "))

if volunteerResponse_slot5 != randomized_slotchoice8:
    print(f'your choice has been taken into consideration')
else:
    print(f'Great minds think alike')

#slot6 VolunteerResponse_slot6 then we have to see if it is the same as slot2
volunteerResponse_slot6 = str(input("Enter your sixth chosen word here: "))

if volunteerResponse_slot6 != randomized_slotchoice2:
    print(f'your choice has been taken into consideration')
else:
    print(f'Great minds think alike')

# I dont think id need to ask the volunteer for their choice for slot7 slot8 or slot9



# Step 3 print the different haiku's

# Non user input 
print("Without user input computer generated haiku")
print(f'ALL {randomized_slotchoice1} IN THE {randomized_slotchoice2}')
print(f'I {randomized_slotchoice3} {randomized_slotchoice4} {randomized_slotchoice5} IN THE {randomized_slotchoice6}')
print(f'{randomized_slotchoice7} THE {randomized_slotchoice8} HAS {randomized_slotchoice9}')

# User Input
#lowercase words are user input
#Capitalized words computer input
print("With user input for collaborative haiku")
print(f'ALL {volunteerResponse_slot1} IN THE {volunteerResponse_slot2}')
print(f'I {volunteerResponse_slot3} {volunteerResponse_slot4} {volunteerResponse_slot5} IN THE {volunteerResponse_slot6}')
print(f'{randomized_slotchoice7} THE {randomized_slotchoice8} HAS {randomized_slotchoice9}')
