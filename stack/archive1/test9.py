mylist = [
    ["I like fruits", "I like meat"],
    ["I like meat", "I like fruits"],
    ["This is only test", "This is being tested"],
    ["This is being tested", "This is only test"],
    ["I like flowers", "I like fruits"],
]

newlist = [mylist[0][0]]
for i, row in enumerate(mylist):
    for j, col in enumerate(row):
        print(row[i], col[j], any(x[1] == col[j] for x in newlist))

print(newlist)
