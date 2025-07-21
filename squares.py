squares =[]
for value in range(1,20):
    square=value**2
    squares.append(square)
print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))
print(sum(squares) / len(squares))  # Shortcut to find average