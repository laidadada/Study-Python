# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")
#
# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 18:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)
#
#
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I want to go " + city.title())
# #
#
# current_number = 0
# while current_number <= 30:
#     current_number += 1
#
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)


responses = {}
responses_active = True
while responses_active:
    name =input("\nWhat is you name?")
    response = input("Which mountain would you like to climb someday ?")
    responses[name] = response
    repeat = input("\nWould you like to let another person respond?(yes/no)")
    if repeat == 'no':
        responses_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(name + " would like to climb " + response + ".")


