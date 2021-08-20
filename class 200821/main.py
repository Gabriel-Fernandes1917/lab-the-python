L = [5, 8, 3, 7, 2]

print('Size the array',len(L))

print('Value mim the list: ',min(L))
print('Value max the list is : ', max(L))
print('add the all the elements the lis: ',sum(L))

L.append(21) ##add element
print(L)
L.remove(8) ## remove element
print("Remove 8 ",L)
del L[3]## remove one position
print("Removed the element on position 3 ",L)