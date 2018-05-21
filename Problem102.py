def run() -> int:
    with open("input_data/problem102.txt", "r") as f:
        vrstice, counter = f.read().splitlines(), 0
        for i in vrstice:
            i = list(map(int, i.split(",")))

            # Split vertices data into each vertex (and the origin)
            a, b, c, origin = list(map(tuple, [i[:2], i[2:4], i[4:], (0, 0)]))

            # Prepare the formula for calculating area from three given vertices
            area = lambda x, y, z: abs((x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1])) / 2)

            # We take all three possible pairs vertices and each pair gives a triangle with the origin
            # If sum of all three triangles equals the one of the original triangle, the origin lies within the triangle
            trije_trikotniki = [area(origin, b, c), area(a, origin, c), area(a, b, origin)]
            counter += sum(trije_trikotniki) == area(a, b, c)
        return counter


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
