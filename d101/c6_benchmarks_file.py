x = [i for i in range(10_000)] # 0, 1, 2, ..., 9_999

y = [xi ** 2 for xi in x] # 0, 1, 4, 9, 16, 25, ..., ...

f = open("result_file.txt", "w")

# --- VERSION 1 --
# for xi, yi in zip(x, y):
#     f.write("{:.4f} | {:4f} \n".format(xi, yi))

# --- VERSION 2 --
# lines = []

# for xi, yi in zip(x, y):
#      lines.append("{:.4f} | {:4f}".format(xi, yi))

lines = ["{:.4f} | {:4f}".format(xi, yi) for xi, yi in zip(x, y)]

f.writelines(lines)

f.close()



