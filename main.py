"""
Choose your path to reach your destiny. You want to meet the wizard king since you seek power,
and so you are going on an expedition to find him. He now lives in a house in the forest, your objective
is to find him and obtain the power you seek. Make the right 
"""
import random
# This is one definition that creates all the events with the help of global lists (some are 2D lists). 
#Note: When I do \n, It just makes so the string of the event question isn't on one incredibly long line.
def Create_Events():
    #Event 0
    event_question.append("You are so tired of the journey you took outside the other day, \n" 
                          "and all you want to do is go to bed. \n" 
                          "You see a room with lots of cobwebs and with a gross smell.")
    event_choices.append(["Sleep in?", "Pass by"])
    event_next.append([1, 2])
    event_health_impact.append([20, -10])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 1
    event_question.append("You wake up. You start realizing that the room is an abandoned shaft, \n"
                          "but you still surprisingly slept comfortably on a random table (+20 health). \n"
                          "When you go back outside, you start walking in a random direction. \n"
                          "You walk and walk then you see a house, with some people outside vibing.")
    event_choices.append(["Stop by?", "Continue walking"])
    event_next.append([3, 4])
    event_health_impact.append([0, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 2
    event_question.append("As you are walking, you pass out. \n"
                          "The next day, your back hurts since you slept on the ground (-10 health). \n"
                          "You keep walking, and you find a green mansion.")
    event_choices.append(["Go inside", "Walk by"])
    event_next.append([5, 6])
    event_health_impact.append([0, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 3
    event_question.append("You get closer and you notice that the people are not human, but dwarfs. \n"
                          "You decide to randomly just join on their conversation. \n"
                          "You get along with them, but you tell them you are cold and whether you can go \n"
                          "inside their house. They agree and their house has a very low ceiling so you have \n"
                          "to bend while walking in it (you are taller). You see a giant bag of 4500 coins, \n"
                          "casually laying in their house.")
    event_choices.append(["Steal the coins?", "I need to control my greediness!"])
    event_next.append([7, 8])
    event_health_impact.append([0, 0])
    event_coins_impact.append([4500, 0])
    event_inventory_impact.append(["", "healing potion"])
    #Event 4
    event_question.append("You think the people do not have anything to do with the wizard king and so you leave, \n"
                          "uninterested. You continue your journey and you see a tree house. \n"
                          "From where you are, you do not hear or see anything coming from it.")
    event_choices.append(["Take a visit?", "Walk by."])
    event_next.append([9, 10])
    event_health_impact.append([0, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 5
    event_question.append("As you are walking in, a little elf welcomes you in the mansion. \n"
                          "You notice on a table, a healing potion.")
    event_choices.append(["Push away the little elf and steal the health potion?", 
                          "Be nice and tell yourself to calm down"])
    event_next.append([11, 12])
    event_health_impact.append([-60, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["healing potion", "healing potion"])
    #Event 6
    event_question.append("You continue walking on your uncurious expedition. \n"
                          "3 days later, you cannot find anything that YOU find INTERESTING. \n"
                          "The forest is cold, you are hungry because you did not go to any stops and \n"
                          "you are out of water from washing your face in the morning like an idiot. \n"
                          "6 hours later, you walk and walk, and then you stop. \n"
                          "After an hour of just laying on the ground, you cannot endure your thirst and hunger.")
    event_choices.append(["Press 1 to quit"])
    event_next.append([0])
    event_health_impact.append([-999])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 7
    event_question.append("As soon as you get out of the house, you tell them it was nice and warm in their house \n"
                          "and you tell them you are on your way to find the one and only wizard king. \n"
                          "They wish you their best luck and as they go back in their house you full-sprint \n"
                          "to somewhere well hidden. After an hour of them yelling and complaining you stole from them, \n"
                          "they give up and think you are really far. You are really rich!")
    event_choices.append(["Press 1 to go to the next stage"])
    event_next.append([15])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 8
    event_question.append("You ask them, out of curiosity, why they had a bag of 4500 Coins laying around. \n"
                          "They said it was for some extremely important trade. \n"
                          "Out of friendship, they give you a healing potion! \n"
                          "You tell them you had a great time and you leave.")
    event_choices.append(["Press 1 to go to the next stage"])
    event_next.append([15])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 9
    event_question.append("You start climbing the tree house and you enter. \n"
                          "You see a witch, but she does not seem to be all bad. \n"
                          "She is trying to find an effective way to make water and food out of a pot. \n"
                          "You do not even ask what she is doing but she asks you in exchange \n"
                          "for doing an experiment on you, she would give you a healing potion \n"
                          "in return after she tried. ")
    event_choices.append(["Accept the offer?", "Decline and politely leave."])
    event_next.append([13, 14])
    event_health_impact.append([-10, 600])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["healing potion", ""])
    #Event 10
    event_question.append("You ignore the tree house and you keep walking forward. \n"
                          "You are incredibly bored, hungry and thirsty. \n"
                          "For some reason, you cannot find anything but a never-ending forest, \n"
                          "with no place to live. You start getting desperate, being out of water \n"
                          "and out of food. 2 days later, you still cannot find anything. \n"
                          "You then rest in peace due to dehydration and from no longer having any hunger.")
    event_choices.append(["Press 1 to quit"])
    event_next.append([0])
    event_health_impact.append([-9999])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 11
    event_question.append("You push the little elf and once he yells out of pain (his head hitting a corner), \n"
                          "You grab a healing potion, you put it in a bag and turn. \n"
                          "You turn back on 9 grown elves (they were having a party for some random reason) \n"
                          "and they start beating you up. -60 health")
    event_choices.append(["Press 1 to go to the next stage"])
    event_next.append([15])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 12
    event_question.append("You ignore your selfish beliefs and you try to have fun. \n"
                          "You see 9 more adult elves (total of 10 elves) and you introduce yourself, \n"
                          "then you join in their party. After the party, they give you a healing potion \n"
                          "out of kindness to show you they really appreciated you there. \n"
                          "You tell everyone your goodbyes and you leave the mansion. ")
    event_choices.append(["Press 1 to go to the next stage"])
    event_next.append([15])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 13
    event_question.append("She cut you on the arm (-10 health) and put the blood from the cut, in the pot. \n"
                          "She then put ingredients and surprisingly, her experiment were successful. \n"
                          "You do not know how, but she made some liquid that gives the nutriments of \n"
                          "average food and more water than average water. \n"
                          "She thanks you, hands you over the healing potion and you leave.")
    event_choices.append(["Press 1 to go to the next stage"])
    event_next.append([15])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 14
    event_question.append("Out of anger, she puts a curse on you, which makes your health increase. \n"
                          "Her intentions were to make a dark spell but she spaced out and now, you run away \n"
                          "and she cries from disappointment. the witch healed you (+600 health)")
    event_choices.append(["Press 1 to go to the next stage"])
    event_next.append([15])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    
    #Event 15
    event_question.append("You are bored after everything and suddenly, you see a shop, and in the distance, \n"
                          "a golden, shining house.")
    event_choices.append(["Stop by the shop before anything", "Visit the golden shining house in the distance,", "Hard pass, waste of time."])
    event_next.append([17, 19, 16])
    event_health_impact.append([0, 0, 0])
    event_coins_impact.append([0, 0, 0])
    event_inventory_impact.append(["", "", ""])
    #Event 16
    event_question.append("You have failed the entire game. You walked by the house owned by the wizard king, your destiny.")
    event_choices.append(["Press 1 to Quit"])
    event_next.append([0])
    event_health_impact.append([-9999])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    #Event 17
    event_question.append("Unfortunately, a rich noble bought everything in the store, but the shield section.")
    event_choices.append(["I'll buy a shield for 700 coins!", "I won't buy a shield"])
    event_next.append([19, 19])
    event_health_impact.append([0, 0])
    event_coins_impact.append([-700, 0])
    event_inventory_impact.append(["shield", ""])
    #Event 18
    event_question.append("You enter the shop, but you do not have enough money to buy anything. \n"
                          "You leave. You now have to decide where you go next.")
    event_choices.append(["The golden shining house in the distance", "Keep walking in another direction in the forest."])
    event_next.append([19, 16])
    event_health_impact.append([0, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 19
    event_question.append("After visiting the shop, you wonder where to go next. \n"
                          "In the distance, there is a golden, shining house.")
    event_choices.append(["Visit the golden shining house in the distance,", "Keep walking in another direction in the forest."])
    event_next.append([20, 16])
    event_health_impact.append([0, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 20
    event_question.append("You knock, and an old man with a white wizard hat above his head and \n"
                          "a long white beard answers and welcomes you inside. \n"
                          "He explains who he is (the wizard king) and asks you why you are here.")
    event_choices.append(["I need Power to abuse for evil", "I need Power to help the poor ones in need and spread good"])
    event_next.append([21, 22])
    event_health_impact.append([0, 0])
    event_coins_impact.append([0, 0])
    event_inventory_impact.append(["", ""])
    #Event 21
    event_question.append("'I do not approve of this! The only way you shall obtain that power is if you live \n"
                          "after I attack you with my strongest spell (150 damage). \n"
                          "O shining sky, come forth, ELETRIC BOLT!!'")
    event_choices.append(["You have no choice, press 1 to try to withstand the punishment (shield blocks 50 damage)"])
    event_next.append([22])
    event_health_impact.append([-150])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])
    
    #Event 22
    event_question.append("The wizard king tells you that you are worthy of having power. \n"
                          "He mentions that this power is strong enough to one handedly take out a nation. \n"
                          "He then casts his permanent buffing spells on you. \n"
                          "You achieved your objective, You Win The Game!")
    event_choices.append(["Press 1 to honor your victory, and leave."])
    event_next.append([99])
    event_health_impact.append([0])
    event_coins_impact.append([0])
    event_inventory_impact.append([""])

    
    return

# choice: list of choices (strings)
def get_user_choice(choices):
    print("Choices:")
    for i, choice in enumerate(choices):
        j = i + 1
        print(str(j) + "- " + choice)
    #This makes so if the user doesn't enter a choice, it will ask again until they do.
    while True:
        try:
            user_choice = int(input("Choose wisely: "))
            if user_choice <= j and user_choice >= 1:
                return user_choice
            else:
                print("Not a valid choice !")
        except ValueError:
            print("Not a valid choice !")
        
    
    return user_choice

#We have the menu that displays the event, the health, the coins, and the inventory.   
def print_Menu():
    print("------------------------------------------------------------------------------")
    print("Event displayed: " + str(event) + "  /  Health: " + str(Health) + "  /  Coins: " +  str(Coins))
    print("Inventory: " + str(inventory))
    print("------------------------------------------------------------------------------")

#Global values
Health = 100
Coins = 0
event = 0
inventory = []

event_question = []

# 2D lists
event_choices = []
event_next = []
event_health_impact = []
event_coins_impact = []
event_inventory_impact = []





Create_Events()
# All events are either lead to a dead end in this while loop, or event 15 and once they get there, 
# the first while loop will end and go to the second one.

# Note that [event] will be 0 when starting the program and will go to the next event 
# which will be based off of what the User_choice is.
while Health >= 0 and event < 15:
    print_Menu()
    print(event_question[event])
    User_choice = get_user_choice(event_choices[event])
    
    Health = Health + event_health_impact[event][User_choice - 1]
    Coins = Coins + event_coins_impact[event][User_choice - 1]
    if ("" != event_inventory_impact[event][User_choice - 1]):
        inventory.append(event_inventory_impact[event][User_choice - 1])
    
    event = event_next[event][User_choice - 1]


# Here, the second loop starts
while Health >= 0 and event <= 22:
    print_Menu()
    print(event_question[event])
    User_choice = get_user_choice(event_choices[event])
    
    
    # After events, it will give you the opportunity to drink your healing potion (if you have one).
    if inventory.count("healing potion") >= 1:
        print("Would you like to drink your health potion ? (random: +20 to +40 health)")
        Health_Choice = get_user_choice(["yes", "no"])
        #Here is where I use random. The potion heals from 20-40 health.
        if Health_Choice == 1:
            health_increase = 20 + int(random.random() * 20)
            Health = Health + health_increase
            inventory.remove("healing potion")
            print("Potion increased health by +" + str(health_increase))
            input("Type Enter to continue. ")
        
    Health = Health + event_health_impact[event][User_choice - 1]
    Coins = Coins + event_coins_impact[event][User_choice - 1]
    if ("" != event_inventory_impact[event][User_choice - 1]):
        inventory.append(event_inventory_impact[event][User_choice - 1])
    
    # During the final trial, I will make if the user had bought a shield in the shop, he or she takes less damage.
    if event == 21:
        if inventory.count("shield") == 1:
            Health = Health + 50
    event = event_next[event][User_choice - 1]

    if event == 17:
        # Check if you have enough Coins to go to event 17
        if Coins < 700:
            event = 18

# Checking if Health is smaller or equal to 0 after every event    
if Health <= 0 or event <= 22:
    print("")
    print("No more Health or Dead End. Sorry Not Sorry, you totally lost.")
else:
    print('-------------------------------')
    print("The end! Thank you for playing!")