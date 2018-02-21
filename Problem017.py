numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
           18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
           70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}


def getWording(n):
    words = ""
    desetice = n % 100
    if n == 1000:
        return "onethousand"
    elif n in numbers and n is not 100:
        return numbers[n]
    else:
        if n < 100:
            return numbers[(desetice // 10) * 10] + numbers[desetice % 10]
        else:
            if n // 100 == n / 100:
                return numbers[n // 100] + numbers[100]
            else:
                if desetice in numbers:
                    return numbers[n // 100] + numbers[100] + "and" + numbers[desetice]
                return numbers[n // 100] + numbers[100] + "and" + numbers[(desetice // 10) * 10] + numbers[
                    desetice % 10]


print(sum([len(getWording(i)) for i in range(1, 1001)]))
