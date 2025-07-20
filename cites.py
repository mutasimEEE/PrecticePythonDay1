# List of cities
cities = ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi', 'Khulna']

# Print the original list
print("Original list:")
print(cities) 
 # ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi', 'Khulna']

# Accessing individual elements by index
print("\nFirst city in the list:")
print(cities[0]) 
 # Dhaka

# Using title() method
print("\nSecond city title-cased:")
print(cities[1].title())  
# Chittagong
# salman
# Adding elements
cities.append('Barisal')
print("\nAfter appending a city:")
print(cities) 
 # ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi', 'Khulna', 'Barisal']

# Inserting elements
cities.insert(2, 'Rangpur')
print("\nAfter inserting a city at index 2:")
print(cities)  
# ['Dhaka', 'Chittagong', 'Rangpur', 'Sylhet', 'Rajshahi', 'Khulna', 'Barisal']

# Removing elements by index
del cities[3]
print("\nAfter deleting city at index 3:")
print(cities)  
# ['Dhaka', 'Chittagong', 'Rangpur', 'Rajshahi', 'Khulna', 'Barisal']

# Popping an element
popped_city = cities.pop()
print("\nPopped the last city:")
print(popped_city)  # Barisal
print("List after popping:")
print(cities)  
# ['Dhaka', 'Chittagong', 'Rangpur', 'Rajshahi', 'Khulna']

# Popping an element from a specific position
popped_city = cities.pop(1)
print("\nPopped the second city:")
print(popped_city)  # Chittagong
print("List after popping index 1:")
print(cities) 
 # ['Dhaka', 'Rangpur', 'Rajshahi', 'Khulna']

# Removing an item by value
cities.remove('Rangpur')
print("\nAfter removing 'Rangpur' by value:")
print(cities)  
# ['Dhaka', 'Rajshahi', 'Khulna']

# Sorting the list permanently
cities.sort()
print("\nPermanently sorted list:")
print(cities)  
# ['Dhaka', 'Khulna', 'Rajshahi']

# Sorting the list in reverse order
cities.sort(reverse=True)
print("\nPermanently reverse sorted list:")
print(cities)  
# ['Rajshahi', 'Khulna', 'Dhaka']

# Temporarily sorting a list
print("\nTemporarily sorted list:")
print(sorted(cities)) 
 # ['Dhaka', 'Khulna', 'Rajshahi']

# Reversing the list
cities.reverse()
print("\nList after reversing:")
print(cities) 
 # ['Dhaka', 'Khulna', 'Rajshahi']

# Finding the length of the list
print("\nNumber of cities in the list:")
print(len(cities)) 
 # 3
