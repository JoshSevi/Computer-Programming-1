data = [5, 3, 7]

print("task 1")
print(data[2])
print(data[-1])
print(len(data))
print(data[0:2])
print(0 in data)
print(data + [2, 10, 5])
print(tuple(data))

print("\ntask 2")
data[0] = -data[0]
print(data)

data.append(10)
print(data)

data.insert(2, 22)
print(data)

data.pop(1)
print(data)

data.sort()
print(data)
