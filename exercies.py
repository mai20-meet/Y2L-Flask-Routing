# First_word = raw_input("First_word")
# print(First_word)

# second_word = raw_input("second_word")
# print(second_word)

# third_word = raw_input("third_word")
# print(third_word)

# print(third_word + First_word)
# print(third_word + second_word)

# user_name = raw_input("user_name")
# print("hey there" + user_name)

# # his age because we ere doing an if statment that based on the user's age

# raw_input("think about an animal from the list:a goose, a horse, a dog, a cat, a duck, a penguin")

# animal = raw_input("is it a bird?")
# if animal == "yes":
# 	animal = raw_input("is it a bird that can fly?")
# elif animal == "no":
# 	animal = raw_input("Does your animal migrate for the winter?")
# if animal == "no":
# 	print("your animal is a duck")
# elif animal== "yes":
# 	print("your animal is a goose")
# if animal == "no":
# 	animal = raw_input("Is your animal smaller than a human being?")
# if animal == "yes":
# 	animal = raw_input("Does your animal love humans?")
# elif animal == "no":
# 	print("the animal name is a cat")
# elif animal =="yes":
# 	print("your animal is a dog")
# if animal == "no":
# 	print("your animal is a horse")
			
# pizza = raw_input("would you like pick up or delivery?")
# if pizza == "pickup":
# 	print("you chose pickup")
# elif pizza == "delivery":
# 	print("you chose delivery")
# pizza_size = raw_input("what size do you want your pizza? xs, s, m, l")
# if pizza_size == "xs":
# 	print("you chose xs")
# elif pizza_size == "s":
# 	print("you chose s")
# elif pizza == "m":
# 	print("you chose m")
# elif pizza == "l":
# 	print("you chose l")

# number = 36
# divisor_counter = 0
# for i in range(1, 37):
# 	if number% i == 0:
# 		divisor_counter=+ 1
# print(" the number " + str(number) + " has " + str(divisor_counter) + " divisors ")

# checked_number = 0
# for i in range(1, 101):
# 	if checked_number% 2 == 0:
# 		print(i)

# def get_divisor_amount(number):
# 	divisor_counter = 0
# 	for i in range(1, 37):
# 		if number_to_check% i == 0:
# 			divisor_counter=+ 1
# 	return divisor_counter

# number_to_check = 36
# divisor_amount = get_divisor_amount(number_to_check)
# print(" the number " + str(number_to_check) + " has " + str(divisor_amount) + " divisors ")

# def prime_number_check():
# 	checked_prime_number = 0
# 	for i in range(1, 101):
# 		if checked_prime_number%2 == False:
# 			print(str(checked_prime_number) + " is a prime number ")
# prime_number_check()

# switch = 2
# while switch < 101:
# 	light = 100 %switch
# 	switch=+1
# 	print(light)

# cookie_counter = 0
# for i in range(0, 11):
# 	for b in range(0, 11):
# 		for c in range(0, 11):
# 			for d in range(0, 11):
# 				for e in range(0, 11):
# 					if i + b + c + d + e == 10:
# 						cookie_counter += 1
# print(cookie_counter) 


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
