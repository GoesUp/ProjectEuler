coord = {(0, 0): 1}
direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
curr_coord, curr_direct = (0, 0), 0
count = 2
while len(coord) < 1001 * 1001:
    curr_coord = (curr_coord[0] + direct[curr_direct][0], curr_coord[1] + direct[curr_direct][1])
    coord[curr_coord] = count
    count += 1
    if (curr_coord[0] + direct[(curr_direct + 1) % 4][0], curr_coord[1] + direct[(curr_direct + 1) % 4][1]) in coord:
        pass
    else:
        curr_direct = (curr_direct + 1) % 4

print(sum([coord[(i, -i)] + coord[(i, i)] for i in range(-500, 501)]) - 1)
