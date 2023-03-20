array = []
n = int(input("Enter number of students: "))
arr =[]
for i in range(0, n):
    x = [input(), int(input())]
    arr.append(x[1])
    array.append(x)
swapped = False
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            swapped = True
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if not swapped:
        break
for i in range(0, n):
    if arr[i]/arr[0] != 1:
        temp = arr[i]
        break
out = []
for i in range(0, n):
    for j in range(0,1):
        if temp == array[i][1]:
            out.append(array[i][0])
out.sort()
for i in range(0, len(out)):
    print(out[i])



