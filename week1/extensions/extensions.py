# possible extensions
dict = {
    "image": ["jpeg", "png", "gif"],
    "application": ["pdf", "zip"],
}

# get user's input, lower and delete spaces
user_input = input("user input: ").lower().strip()

# split to get file name and ext(if exists)
parts = user_input.split(".")

# check for ext
if len(parts) < 2:
    print("application/octet-stream")
    exit()

ext = parts[-1]
# check for exeptions
if parts[-1] == "jpg":
    print("image/jpeg")

elif ext == "txt":
    print("text/plain")

# if not exception, check in possible extensions
else:
    for x, y in dict.items():
        if ext in y:
            print(f"{x}/{ext}")
            break
    # if not in dict
    else:
        print("application/octet-stream")
