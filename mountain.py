responses = {}

while True:
	name = input("What is your name? ")
	mountain = input("Which mountain would you like to climb someday? ")
	responses[name] = mountain

	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat.lower() == 'no':
		break

print("\n--- Poll Results ---\n")
for name, mountain in responses.items():
	print(f"{name} would like to climb {mountain}.")
