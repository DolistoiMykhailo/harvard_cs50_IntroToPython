# replacement loop
def do_replace(text, replacement_dict):
    for key, value in replacement_dict.items():
        text = text.replace(key, value)
    return text


# chars to be replaced
replacement_dict = {":)": "🙂", ":(": "🙁"}

# user input
user_input = input("Input: ")

# print user's input with replacements
print(do_replace(user_input, replacement_dict))
