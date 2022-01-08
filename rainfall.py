def rainaverage(l):
    raindata = {}
    outputlist = []
    for c, r in l:
        if c in raindata.keys():
            raindata[c].append(r)
        else:
            raindata[c] = [r]
    print(raindata)

    for c in raindata:
        average = sum(raindata[c]) / len(raindata[c])
        outputlist.append((c, average))
        outputlist.sort()

    return (outputlist)


print(rainaverage([(1, 2), (1, 3), (2, 3), (1, 1), (3, 8)]))
print(rainaverage([('Bombay', 848), ('Madras', 103), ('Bombay', 923), ('Bangalore', 201), ('Madras', 128)]))
