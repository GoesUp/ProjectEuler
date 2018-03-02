count = 1
while True:
    moznosti = [set(str(count * i)) for i in range(1, 7)]
    prva = moznosti[0]
    if all([True if prva == j else False for j in moznosti[1:]]):
        break
    count += 1

print(count)
