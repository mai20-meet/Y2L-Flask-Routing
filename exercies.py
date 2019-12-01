raw_input("First word")
First_word = raw_input("First_word")
print(First_word)

raw_input("second word")
second_word = raw_input("second_word")
print(second_word)

raw_input("third word")
third_word = raw_input("third_word")
print(third_word)

print(word_three + word_one)
print(word_three + word_two)

raw_input("user name")
user_name = raw_input("user_name")
print("hey there" + user_name)

# his age because we ere doing an if statment that based on the user's age

raw_input("think about an animal from the list:a goose, a horse, a dog, a cat, a duck, a penguin")
user_animal = raw_input("user_answer")
print (user_answer)

animal = raw_input("is it a bird?")
if animal == "yes":
	animal2 = raw_input("is it a bird that can fly?")
elif animal == "no":
	animal3 = raw_input("Does your animal migrate for the winter?")
	if animal3 == "yes":
		print("the animal name is a goose")
	else animal3 == "no":
		print("your animal is a duck")
		animal4 = raw_input("Is your animal smaller than a human being"?)
		if animal4 == "yes":
			animal5 = raw_input("Does your animal love humans?")
			if animal5 == "yes":
				print("you chose dogs")
			else animal5 == "no":
				print("you chose cats")
		else animal4 == "no":
			print("you chose horses")

pizza = raw_input("would you like pick up or delivery?")
if pizza == "pickup":
	print("you chose pickup")
else pizza == "delivery":
	print("you chose delivery")
pizza_size = raw_input("xs, s, m, l")
if pizza_size == "xs":
	print("you chose xs")
elif pizza_size == "s":
	print("you chose s")
elif pizza == "m":
	print("you chose m")
else pizza == "l":
	print("you chose l")

number = 36
divisor_counter = 0
for i in range(1, 37):
	if number% i == 0:
		divisor_counter=+ 1
print("the number" + str(number) + "has" + str(divisor_number) + "divisors")

checked_number = 0
for i in range(1, 101):
	if checked_number% 2 == 0:
		print(i)

def get_divisor_amount(number):
	divisor_counter = 0
	for i in range(1, 37):
		if number% i == 0:
			divisor_counter=+ 1
	return divisor_counter
number_to_check = 36
divisor_amount = get_divisor_amount(number_to_check)
print("the number" + str(number) + "has" + str(divisor_number) + "divisors")

def prime_number_check():
	checked_prime_number = 0
	for i in range(1, 101):
		if checked_prime_number%2 = False:
			print(str(checked_prime_number) + "is a prime number")

switch = 2
while switch < 100:
	light = 100%switch:
	switch=+1
	print(light)

cookies = 10
for i in range(1, 11):
	children = cookies%5
	print(children)

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
