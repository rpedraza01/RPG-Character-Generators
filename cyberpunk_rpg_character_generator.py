import random
# from random import randint

# def random_char_class(edgerunner_pick):
# 	edgerunner_list = ["Rockerboy", "Solo", "Netrunnner", "Corporate", "Techie", "Cop", "Fixer", "Media", "Nomad"]
# 	edgerunner_pick = random.choice(edgerunner_list)
# 	print(f"Your character's class will be {edgerunner_pick}")

# def random_char_stats(stats_pick):
# 	stats_pick = random.choice(range(1, 11))
# 	print(f"Your character's stats are as follows: \n INT {stats_pick} \n REF {stats_pick} \n DEX {stats_pick} \n TECH {stats_pick} \n COOL {stats_pick} \n WILL {stats_pick} \n LUCK {stats_pick} \n MOVE {stats_pick} \n BODY {stats_pick} \n EMP {stats_pick}")

while True:
	print("Welcome to the Cyberpunk Random Character Generator! \n Let's get you set up with your next favorite Edgerunner!")
	user_char_name = input("Please enter the name of your charcter. > ")
	print(f"{user_char_name} is a cool name! \n Now let's pick your character's class.")

	char_class_list = ["Rockerboy", "Solo", "Netrunnner", "Corporate", "Techie", "Cop", "Fixer", "Media", "Nomad"]
	# random_char_pick = random.choice(char_class_list)
	user_class_pick = input("Please pick a class from the following list: \n Rockerboy \n Solo \n Netrunnner \n Corporate \n Techie \n Cop \n Fixer \n Media \n Nomad \n> ")
	if user_class_pick in char_class_list:
		print(f"{user_char_name}'s class will be {user_class_pick}. Very nice! \n Your character's stats will now be randomly generated.")
	elif user_class_pick not in char_class_list:
		user_class_pick = input("Sorry, you must pick a class from the list provided. Please pick again. > ")

	# stats_list = ["INT", "REF", "DEX", "TECH", "COOL", "WILL", "LUCK", "MOVE", "BODY", "EMP"]
	# for stats in range(1):
	stats_pick_int = random.choice(range(1, 11))
	stats_pick_ref = random.choice(range(1, 11))
	stats_pick_dex = random.choice(range(1, 11))
	stats_pick_tech = random.choice(range(1, 11))
	stats_pick_cool = random.choice(range(1, 11))
	stats_pick_will = random.choice(range(1, 11))
	stats_pick_luck = random.choice(range(1, 11))
	stats_pick_move = random.choice(range(1, 11))
	stats_pick_body = random.choice(range(1, 11))
	stats_pick_emp = random.choice(range(1, 11))
	print(f"{user_char_name}'s stats will be: \n INT {stats_pick_int} \n REF {stats_pick_ref} \n DEX {stats_pick_dex} \n TECH {stats_pick_tech} \n COOL {stats_pick_cool} \n WILL {stats_pick_will} \n LUCK {stats_pick_luck} \n MOVE {stats_pick_move} \n BODY {stats_pick_body} \n EMP {stats_pick_emp} \nNot too shabby.")

	exit = input(f"Here's a summary of your new character. \n Character name : {user_char_name} \n Character class: {user_class_pick} \n Stats: \n INT {stats_pick_int} \n REF {stats_pick_ref} \n DEX {stats_pick_dex} \n TECH {stats_pick_tech} \n COOL {stats_pick_cool} \n WILL {stats_pick_will} \n LUCK {stats_pick_luck} \n MOVE {stats_pick_move} \n BODY {stats_pick_body} \n EMP {stats_pick_emp} \nI hope you're satisfied with your new Edgerunner. If not would you like to generate a new character? > ")
	if exit != "yes":
		break
