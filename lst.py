lst = [(None, None), (1, 2), (None, 3), (4, 5), (None, None)]
filterd=[]
for tup in lst:
    if any(elem is not None for elem in tup):
        filterd.append(tup)
print(filterd)
print('*'*50)
