raw_input("think about an animal from the list:a goose, a horse, a dog, a cat, a duck, a penguin")
animal1 = raw_input("is it a bird?")
if animal1 == "yes":
	animal2 = raw_input("Does your animal migrate for the winter?")
	if animal2 == "no":
		print("your animal is a duck")
	if animal2 == "yes":
		print("your animal is a goose")
if animal1 == "no":
	animal3 = raw_input("Is your animal smaller than a human being?")
	if animal3 == "yes":
		animal4 = raw_input("does your animal loves coldnes?")
		if animal4 == "yes":
			print("your animal is a penguin")
		if animal4 == "no":
			animal5 = raw_input("does your animal loves humens?")
			if animal5 =="yes":
				print("your animal is a dog")
			if animal5 == "no":
				print("your animal is a cat")
	if animal3 == "no":
		print("your animal is a horse")