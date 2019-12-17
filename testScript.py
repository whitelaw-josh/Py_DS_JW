arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(type(arr))
print(arr[0][1])