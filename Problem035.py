def getRotations(n):
    return [int(str(n)[i:] + str(n)[:i]) for i in range(len(str(n)))]


biggest_possible = 10 ** 6
sito = [True for i in range(1, biggest_possible)]
nums = []
position = 2
while not position == len(sito):
    if sito[position] == True:
        for j in range(position, len(sito), position):
            sito[j] = False
        nums.append(position)
    position += 1

triangle = []
for i in range(len(nums)):
    if (("0" not in str(nums[i])) and ("2" not in str(nums[i])) and ("4" not in str(nums[i])) and (
            "5" not in str(nums[i])) and ("6" not in str(nums[i])) and ("8" not in str(nums[i]))) or nums[i] < 10:
        rotacije = getRotations(nums[i])
        juhu = True
        for w in rotacije:
            if w not in nums:
                juhu = False
        if juhu:
            triangle += rotacije

print(len(list(set(triangle))))
