# problem8.py
# Que: Can you chnage the values inside a list which cotained in set S?
S = {8, 7, 12, "Aashish", [1, 2]}
# print(S)

# ==> No, we cannot change the values inside a list in a set because a list cannot be included in a set as it is mutable (unhashable).

# It becomes changeable if we change the list to tuple but expect for the tuple
S1 = {8, 7, 12, "Aashish", (1, 2)}
S1.update([3, 4, 5])
print(S1)