def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

print(mysum([1,2,3,4,5]))
print(sumtree([1,[2, [3,4], 5], 6, [7, 8]]))
