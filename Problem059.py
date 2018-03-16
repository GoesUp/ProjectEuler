def do_the_xor(x, y, z):
    key = [x, y, z]
    while len(key) < len(cifre):
        key += key
    combine = zip(cifre, key)
    temp_spaces = 0
    return [a ^ b for a, b in combine]


with open("input_data/problem059.txt", "r") as f:
    cifre = list(map(int, f.readlines()[0].split(",")))
    best_xyz, spaces = (0, 0, 0), 0
    for x in range(ord("a"), ord("z") + 1):
        for y in range(ord("a"), ord("z") + 1):
            for z in range(ord("a"), ord("z") + 1):
                text = do_the_xor(x, y, z)
                if text.count(32) > spaces:
                    best_xyz, spaces = (x, y, z), text.count(32)

    print("Result:", sum(do_the_xor(best_xyz[0], best_xyz[1], best_xyz[2])), end="\n\n")
    if input("Type anything and press enter if you want to see the key and the decrypted text: "):
        print("Key:", "".join([chr(best_xyz[0]), chr(best_xyz[1]), chr(best_xyz[2])]))
        print("Text:", "".join(chr(i) for i in do_the_xor(best_xyz[0], best_xyz[1], best_xyz[2])))
