# get user's input
user_input = input("Input: ").lower().strip()

# check if user's input start with "h" and is not hello
if user_input.startswith("h"):
    if user_input.startswith("hello") == 0:
        print("$20")
    else:
        print("$0")
else:
    print("$100")

# check if the answer is in dict
