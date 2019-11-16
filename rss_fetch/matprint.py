def mat_put(a):
    n = len(a)
    l = n * 2 - 1
    listl = [[0] * l for i in range(l)]
    for i in range(0, l):
        for j in range(0, l):
            for k in range(0,n):
                if i == k or i == l - k - 1 or j == k or j == l - k - 1:
                    listl[i][j] = a[k]
                    break
    for i in range(0,l):
        print(listl[i])



mat_put([1, 2, 3])
