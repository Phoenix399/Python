# Define sets (use curly braces for sets)
set1 = {"green", "blue"}
set2 = {"blue", "yellow"}

print("\nSet 1:", set1)
print("Set 2:", set2)

# Union
set3 = set1.union(set2)
print("\nUnion:", set3)

# Intersection
set4 = set1.intersection(set2)
print("Intersection:", set4)

# You can also use | for union and & for intersection
union_set = set1 | set2
intersection_set = set1 & set2

print("Union using | :", union_set)
print("Intersection using & :", intersection_set)
