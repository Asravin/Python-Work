def find_farthest_orbit(orbit: list):
    max = orbit[0]
    for i in orbit:
        if i[0] != i[1]:
            if i[0] * i[1] > max[0] * max[1]:
                max = i
    return max

orbit = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbit))
