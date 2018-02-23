nums = []
for i in range(1, 1000000):
 if str(i) == str(i)[::-1] and bin(i)[2:] == (bin(i)[2:])[::-1]:
  nums+= [i]
print(sum(nums))