# Get input from the user as a string
user_input = input("Enter a list of words separated by spaces: ")

# Split the input string into a list based on spaces
words = user_input.split()
def match_str(words : list[str]):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
    return result

match_str(words)

print(match_str(words))