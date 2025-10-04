friends = ["Fredua", "Aseye", "Michael"]

# Loop through the list
for friend in friends:
    print(f"Hello, {friend}!")

# Let's use arithmetic operators
friend_count = len(friends)  # This is 3
print(f"\nYou have {friend_count} friends.")

# Adding a new friend
friend_count += 1  # Using += (addition)
print(f"After making a new friend, you now have {friend_count} friends.")

# Removing a friend
friend_count -= 1  # Using -= (subtraction)
print(f"After losing a friend, you now have {friend_count} friends.")

# Doubling your friends (just for fun)
friend_count *= 2  # Using *= (multiplication)
print(f"If you cloned your friend group, you'd have {friend_count} friends.")

# Dividing your friends into 2 groups
groups = friend_count // 2  # Using // (integer division)
print(f"You can make {groups} groups of 2 friends each.")
