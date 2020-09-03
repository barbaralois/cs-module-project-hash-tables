cache = {}


def expensive_seq(x, y, z):
    # add y+z if x is 0 or below
    if x <= 0:
        return y + z
    # if x is larger than 0, and this combo is not yet in the cache
    if (x, y, z) not in cache:
        # add the tuple into the cache so this only has to run once for this combo
        cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + \
            expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    return cache[(x, y, z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
