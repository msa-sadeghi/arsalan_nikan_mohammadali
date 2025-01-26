# f = open("test", "w")
# print("hello", "friends", sep="-", end=" ", file=f)
# print("how are you today?", file=f)
import time
message = "hello friends. how are you today?"
for c in message:
    print(c, end="", flush=True)
    time.sleep(0.2)