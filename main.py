numbers = [100, 101, 3, 2]
numbers = list(map(str, numbers))
numbers.sort(key=lambda x: x*3, reverse=True)
print(numbers)