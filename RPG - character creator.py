# Character Creator program
# 30 points to spend on Strength, Health, Wisdom, Dexterity.

choice = None
choice1 = None
choice2 = None
choice3 = None
#character start out with a pool of 30
pool = 30
#character starts out with no stats
stats = [0, 0, 0, 0]
#for easy future reference
strength, stanima, intelligence, dexterity = stats

#the main while loop; exits when player selects "0"

while choice != "0":
    print("""
__    __    __      
\ \  /  \  / /          THE GAME
 \ \/ /\ \/ / ELCOME TO THE GAME
  \__/  \__/            THE GAME

IT'S GENERALLY GOOD TO HAVE STATS
 HIGHER THAN 0 IN A ROLE-PLAYING
 GAME. SO THAT IS WHAT YOU WILL
 DO RIGHT NOW. PLEASE SELECT AN
           OPTION:

0 - I'VE SET MY STATS, BEGIN THIS
    "ADVENTURE"!
1 - I'M DUMB AND STILL HAVEN'T
    FINISHED SETTING MY STATS
    """)

    #resets choices
    choice1 = None
    choice2 = None
    choice3 = None

    choice = input("Type your choice here: ")

    #begining the adventure

    if choice == "0":
        input("Thank you. Your stats may or may not have been saved. They may or may not have a purpose later in this game. Press enter to exit the character creator.")

    #Assigning the stats
    
    elif choice == "1":
        while choice1 != "0":

            #resets choices again just to be safe
            choice1 = None
            choice2 = None
            choice3 = None
            
            print("""
            Would you like to add or remove stat points, or are you finished?
            0 - exit
            1 - add
            2 - remove
            """)

            choice1 = input("Type your choice here: ")

            #exiting

            if choice1 == "0":
                print("Well OK then.")

            #adding stats
            elif choice1 == "1":
                print("""
                Which stat would you like to upgrade?
                0 - None, nvmd
                1 - Strength
                2 - Stanima
                3 - Intelligence
                4 - Dexterity
                """)

                print("Your current stats are: STRENGTH - " + str(strength) + ", STANIMA - " + str(stanima) + ", Intelligence - " + str(intelligence) + ", Dexterity - " + str(dexterity) + ".")
                print("You have " + str(pool) + " points in your pool")

                choice3 = input("Type your choice here: ")

                #exiting

                if choice3 == "0":
                    print("Well OK then...")

                elif choice3 == "1":
                    points = int(input("How many points would you like to add? Type your choice here: "))
                    #making sure that there are enough points in the pool
                    if points <= pool and points >= 0:
                        strength = strength + points
                        pool = pool - points
                    else:
                        print("Your dumb.")

                elif choice3 == "2":
                    points = int(input("How many points would you like to add? Type your choice here: "))
                    #making sure that there are enough points in the pool
                    if points <= pool and points >= 0:
                        stanima = stanima + points
                        pool = pool - points
                    else:
                        print("Your dumb.")

                elif choice3 == "3":
                    points = int(input("How many points would you like to add? Type your choice here: "))
                    #making sure that there are enough points in the pool
                    if points <= pool and points >= 0:
                        intelligence = intelligence + points
                        pool = pool - points
                    else:
                        print("Your dumb.")

                elif choice3 == "4":
                    points = int(input("How many points would you like to add? Type your choice here: "))
                    #making sure that there are enough points in the pool
                    if points <= pool and points >= 0:
                        dexterity = dexterity + points
                        pool = pool - points
                    else:
                        print("Your dumb.")

                else:
                    print("Follow the simple instructions.")

        #removing stat points 
            elif choice1 == "2":

                print("""
                Which stat would you like to downgrade?
                0 - None, nvmd
                1 - Strength
                2 - Stanima
                3 - Intelligence
                4 - Dexterity
                """)

                print("Your current stats are: STRENGTH - " + str(strength) + ", STANIMA - " + str(stanima) + ", Intelligence - " + str(intelligence) + ", Dexterity - " + str(dexterity) + ".")

                choice3 = input("Type your choice here: ")

                #exiting

                if choice3 == "0":
                    print("Well OK then...")

                elif choice3 == "1":
                    points = int(input("How many points would you like to remove? Type your choice here: "))
                    #making sure that there are enough points in the stat
                    if points <= strength and points >= 0:
                        strength = strength - points
                        pool = pool + points
                    else:
                        print("Your dumb.")

                elif choice3 == "2":
                    points = int(input("How many points would you like to remove? Type your choice here: "))
                    #making sure that there are enough points in the stat
                    if points <= stanima and points >= 0:
                        stanima = stanima - points
                        pool = pool + points
                    else:
                        print("Your dumb.")

                elif choice3 == "3":
                    points = int(input("How many points would you like to remove? Type your choice here: "))
                    #making sure that there are enough points in the stat
                    if points <= intelligence and points >= 0:
                        intelligence = intelligence - points
                        pool = pool + points
                    else:
                        print("Your dumb.")

                elif choice3 == "4":
                    points = int(input("How many points would you like to remvoe? Type your choice here: "))
                    #making sure that there are enough points in the stat
                    if points <= dexterity and points >= 0:
                        dexterity = dexterity - points
                        pool = pool + points
                    else:
                        print("Your dumb.")

                else:
                    print("Follow the simple instructions.")
                
    #Easter Egg

    elif choice == "XYZZY":
        print("Congrats, you discoved a secret password. It doesn't do anything though.")

    #If people are dumb

    else:
        print("That's not a choice, dummy")
