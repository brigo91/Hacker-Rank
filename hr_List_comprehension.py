#print([[x + y, x - y] for x in [1,2,3] for y in [3,1,4] if x != y])

x=3
y=4
z=5

n=2
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i+ j + k) != n])
