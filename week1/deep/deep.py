# get user's input
user_input = str(input("Input: "))

# valid answers
list = ["42", "forty-two", "forty two"]

# Format and check if user's input is valid
if user_input.lower().strip() in list:
    print("Yes")
else:
    print("No")
