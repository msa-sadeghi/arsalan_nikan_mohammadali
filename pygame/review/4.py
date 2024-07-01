user_input = input("enter a name or word: ")
user_input = sorted(user_input)
result = []
with open("1.txt") as f:
    for word in f.read().split("\n"):
        if sorted(word) == user_input:
            result.append(word)
            
print(result)
            
        