# tup = (1,2,3,4,'hello world')
# print(type(tup))

# lst = [1,2,3,4,5]
# tup = tuple(lst)
# print(tup)


# st = set([3,4,5,6,7,3])
st = {1,2,3,4,5,3,2,1}
for i in st:
    print(i)
st = {2,3,4,1}
# print(st)

bt = {4,5,6}
# print(st.union(bt))
# print(st.intersection(bt))
print(st.difference(bt))
bt.discard(5)
print(bt)

# print(st)
