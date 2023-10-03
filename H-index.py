def h_index(citations):
    n = len(citations)
    citations.sort(reverse=True)

    h = 0
    for i in range(n):
        if citations[i] >= i + 1:
            h = i + 1

    return h

citations = [1,3,1]
print(h_index(citations))
