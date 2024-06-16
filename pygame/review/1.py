with open("1.txt") as f:
    x = f.read().split("\n")
    
def is_pal(word):
    if word == word[::-1]:
        return True
    return False

str_pal = ""
for w in x:
   if is_pal(w):
       str_pal += w+"\n"

with open("pal.txt", "w") as f:
    f.write(str_pal)