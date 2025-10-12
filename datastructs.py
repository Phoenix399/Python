Fruits = ['Apple', 'Guava', 'Mango', 'Kiwi']

print("Length of the list is:", len(Fruits))
print("First element is:", Fruits[0])
print("Last element is:", Fruits[-1])

Fruits.append('Papaya')
print("List after appending Papaya:", Fruits)

Fruits.remove('Guava')
print("List after removing Guava:", Fruits)

Fruits.sort()
print("Sorted list:", Fruits)

Fruits.reverse()
print("Reversed list:", Fruits)

print("Multiplication on list:" , Fruits * 2)

Fruits = Fruits[:4]
print("Sliced List is:", Fruits)

Fruits.clear()
