def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res=arg
    return res

# def min2(firsr, *rest):
#     for arg in rest:
#         if arg < rest:
#             first = arg
#     return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1(3,4,5,1))
# print(min2("bb","aa"))
print(min3([2,2], [1,1], [3,3]))
