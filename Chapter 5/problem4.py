# problem4.py
#  Que: what will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

# The length of the set is 2 because 20 (int) and 20.0 (float) are considered equal in Python, 
# so only one of them is stored. "20" (string) is different, so it is also included.
# If the value is other then 20.0 like 20.1 then it well be considered as unique value and optput will be 3
