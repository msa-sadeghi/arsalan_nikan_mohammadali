# students = {
#     2500000:{
#         'name': "mohammad", 
#         "family":"khezri", 
#         "age":14, 
#     },

#     2600000:{
#         'name': "nikan", 
#         "family":"ariaii", 
#         "age":12, 
#     }
# }

x = list(range(1_000_000, 1_200_001, 2))
print(x)

x = []
for i in range(1_000_000, 1_200_001, 2):
    if i != 1_100_000:
        x.append(i)
  
print(x)

x = [i for i in range(1_000_000, 1_200_001, 2) \
    if i != 1_100_000]
print(x)

numbers = ["a", "b", "c","d"]
for c in numbers:
    print(c)
    
for i in range(len(numbers)):
    print(f"number {i+1} is {numbers[i]}")
    
for i, value in enumerate(numbers):
    print(f"number {i+1} is {value}")
    
name = "nikan"  
name2 = "mohammad" 
x = [f"hello {name}", f"hello {name2}"]
print(x)
print(x[0])