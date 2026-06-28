# TASK 1
tup = (99, "shaurya", 12.2, 15, "rana")

# TASK 2
print("First element:", tup[0])
print("Last element:", tup[len(tup)-1])

# TASK 3
print("Occurrences of 'shaurya':", tup.count("shaurya"))

# TASK 4
print("Length of tuple:", len(tup))

# TASK 5
set1 = set(tup)
set2 = {"shaurya", 15, "hello"}

print("Set1:", set1)
print("Set2:", set2)

# TASK 6
set1.add("new")
set1.remove(99)
print("After adding new and removing 99:", set1)

# TASK 7
print("Union:", set1.union(set2))

# TASK 8
print("Intersection:", set1.intersection(set2))

# TASK 9
print("Difference (set1 - set2):", set1.difference(set2))

# TASK 10
print("Tuple: Ordered, immutable, allows duplicates")
print("Set: Unordered, mutable, only unique elements")
