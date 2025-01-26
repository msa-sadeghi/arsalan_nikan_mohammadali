# scores = []
# for i in range(4):
#     scores.append(float(input(f"enter score #{i + 1}: ")))
# print("all scores before adding", scores)
# for i in range(4):
#     scores[i] += 2
# print("all scores after adding", scores)

my_dict1 = {
    2 : ["mohammad", "mammad"],
    (1, "first") : ["arsalan", "arsi"],
    3 : ["nikan", "niki"]
}
my_dict2 = {
    (1, "first") : ["arsalan", "arsi"],
    2 : ["mohammad", "mammad"],
    3 : ["nikan", "niki"]
}

print(my_dict1[(1, "first")])
print(my_dict1[2])
print(my_dict1[3])
print(my_dict1 == my_dict2)
print(id(my_dict1))
print(id(my_dict2))
print([1,2,3] == [3,1,2])
print((1,2,3) == (3,1,2))