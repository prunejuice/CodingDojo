words = "It's thanksgiving day. It's my birthday,too!"

print words.find("day")

words2 = words.replace("day", "month", 1)

print words2

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[len(x)-1]
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
y = []
for num in range(len(x)/2):
    y.append(x[num])

print y
x[0] = y
print x
