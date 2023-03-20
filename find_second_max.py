n = int(input())
arr = list(map(int, input().split()))
first_max = max(arr)
flag = False
while flag == False:
    if first_max in arr:
        arr.remove(first_max)
    else:
        flag = True
second_max = max(arr)
print(second_max)