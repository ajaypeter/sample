l1 = [1,2,3,4]
l2 = [2,3,4,5]
l3 = []
for item in zip(l1,l2) :
    l3.append(item[0] + item[1])
print(l3)
