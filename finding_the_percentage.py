n = 3
dict = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    dict[name] = scores
query = input("Enter the query name: ")
for key in dict:
    if query == key:
        for value in dict[key]:
            sum = sum + int(value)
avg = sum/3
print("%.2f" % avg)




