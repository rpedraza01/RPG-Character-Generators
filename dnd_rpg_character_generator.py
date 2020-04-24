import random

# What I want this script to do:
# 1. People can enter in whatever name they want
# 2. Allow people to choose their race and class, or allow the script to randomly choose their race, class, and background
# 3. The script will simualte rolling four 6-sided dice dropping the lowest value and returning the highest 3 dice to create and assign a stat value to an attribute
# 4. A summary of the new character is generated (maybe create a CSV or PDF of the summary?)
# 5. The script asks if the user would like to try again or end the program

# This function rolls four 6-sided dice
# It then sorts the rolls greatest to lowest
# Then it returns the sum of the greatest 3 dice while dropping the lowest die value
def dice_roll_func():
	dice_rolls = [random.randint(1, 6) for _ in range(4)]
	dice_rolls.sort(reverse = True)
	return sum(dice_rolls[:3])


# This function randomly chooses a hero's class
def char_class_func():
	char_class_list = [
		"Barbarian",
		"Bard",
		"Cleric",
		"Druid",
		"Fighter",
		"Monk",
		"Paladin",
		"Ranger",
		"Rogue",
		"Sorcerer",
		"Warlock",
		"Wizard"
		]
	rand_char_class_pick = random.choice(char_class_list)
	return rand_char_class_pick


# This function randomly chooses a hero's race
def char_race_func():
	char_race_list = [
		"Dwarf",
		"Elf",
		"Halfling",
		"Human",
		"Dragonborn",
		"Gnome",
		"Half-Elf",
		"Half-Orc",
		"Tiefling"
		]
	rand_char_race_pick = random.choice(char_race_list)
	return rand_char_race_pick


# This function randomly chooses a hero's background
def char_bkgd_func():
	char_bkgd_list = [
		"Acolyte",
		"Charlatan",
		"Criminal",
		"Entertainer",
		"Folk Hero",
		"Gladiator",
		"Guild Artisan",
		"Guild Merchant",
		"Hermit",
		"Knight",
		"Noble",
		"Outlander",
		"Pirate",
		"Sage",
		"Sailor",
		"Soldier",
		"Urchin"
		]
	rand_char_bkgd_pick = random.choice(char_bkgd_list)
	return rand_char_bkgd_pick


while True:
# Intro to program. Assigns user created name to variable
	print("Welcome mortal to the Dungeons and Dragons Random Character Generator! Proceed if you dare!")
	user_char_name = input("What shall your hero be called? > ")
	print(f"{user_char_name} is a strange name. Might you be from another land? \n Now let's determine your hero's class.")

# Character class
	user_class_pick = input("Would you like to pick your hero's class? If not, I will choose for you. > ")
	if user_class_pick != "yes":
		user_class_pick = char_class_func()
		print(f"Your hero's class shall be {user_class_pick}!")
	else:
		user_class_pick = input("Please pick from the following list: \n Barbarian \n Bard \n Cleric \n Druid \n Fighter \n Monk \n Paladin \n Ranger \n Rogue \n Sorcerer \n Warlock \n Wizard \n Your Pick > ")
		print(f"You've selected {user_class_pick}. \n Next, we shall pick your hero's race.")

# Character race
	user_race_pick = input("Would you like to pick your hero's race? If not, I will choose for you. > ")
	if user_race_pick != "yes":
		user_race_pick = char_race_func()
		print(f"Your hero's race shall be {user_race_pick}! \n Next, we shall pick your hero's background.")
	else:
		user_race_pick = input("Please pick from the following list: \n Dwarf \n Elf \n Halfling \n Human \n Dragonborn \n Gnome \n Half-Elf \n Half-Orc \n Tiefling \n Your Pick > ")
		print(f"You've selected {user_race_pick}. \n Next, we shall pick your hero's background.")

# Character background
	user_bkgd_pick = input("Would you like to pick your hero's background? If not, I will choose for you. > ")
	if user_bkgd_pick != "yes":
		user_bkgd_pick = char_bkgd_func()
		print(f"Your hero's background shall be {user_bkgd_pick}! \n Next, we shall randomly generate your hero's base attributes.")
	else:
		user_bkgd_pick = input("Please pick from the following list: \n Acolyte \n Charlatan \n Criminal \n Entertainer \n Folk Hero \n Gladiator \n Guild Artisan \n Guild Merchant \n Hermit \n Knight \n Noble \n Outlander \n Pirate \n Sage \n Sailor \n Soldier \n Urchin \n Your Pick > ")
		print(f"You've selected {user_bkgd_pick}. \n Next, we shall randomly generate your hero's base attributes.")

# Character base attribute rolls and assignment
	att_stats = [dice_roll_func() for _ in range(6)]
	print(f"{user_char_name}'s base attributes shall be: \n STR {att_stats[0]} \n DEX {att_stats[1]} \n CON {att_stats[2]} \n INT {att_stats[3]} \n WIS {att_stats[4]} \n CHA {att_stats[5]} \n Impressive!.")

# Summary of character build
	summary = (f"Here's a summary of your new Hero. \n Hero name: {user_char_name} \n Hero class: {user_class_pick} \n Hero race: {user_race_pick} \n Hero background: {user_bkgd_pick} \n Stats: \n STR {att_stats[0]} \n DEX {att_stats[1]} \n CON {att_stats[2]} \n INT {att_stats[3]} \n WIS {att_stats[4]} \n CHA {att_stats[5]}")
	print_summary = input("Would you like a summary of your hero? > ")
	if print_summary == "yes":
		print(f"{summary}")
	else:
		print("I see you like to live dangerously!")

# Exit string for user to make another build or exit program
	exit = input(f"I hope you're satisfied with your new Hero. If not would you like to create a new hero? > ")
	if exit != "yes":
		break