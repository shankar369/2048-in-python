
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for row in a:
    print(row)

print('\n')

a=[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

for row in a:
    print(row)

print('\n')
a=[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

for row in a:
    print(row)


