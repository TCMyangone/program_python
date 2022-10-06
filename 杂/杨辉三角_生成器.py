def yf_gen(line):
    b = []
    for i in range(1, line + 1):
        if i <= 2:
            b.append(1)
            yield b
        else:
            r = [b[e] + b[e + 1] for e in range(0, len(b) - 1)]
            b = [1] + r + [1]
            yield b

yf_gen_1 = yf_gen(100)
for t in yf_gen_1:
    print(t)



