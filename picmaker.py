
fname = "OMEGALUL.ppm"

f = open(fname,"w+")
f.write("P3 1000 1000 255\n")

for x in range(1000):
    for y in range(1000):
        ds = (x - 500) ** 2 + (y - 500) ** 2
        if ds <= 250 ** 2:
            f.write("75 0 0 ")
        elif ds <= 275 ** 2:
            f.write("253 228 200 ")
        else:
            for i in range(1000):
                if ds < (275 + i) ** 2:
                    f.write((str(i / 4) + " ") * 3)
                    break

f.close()
