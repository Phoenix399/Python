my_set = {1,2,3,3,4,4,4}
print("Set :", my_set)

my_set.add(5)
print("Updated Set :", my_set)

set1 = my_set
set2 = {1,4,4,6}

print("\nGet 1" , set1)
print("Set 2" , set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric difference")
print(set1.symmetric_difference(set2))