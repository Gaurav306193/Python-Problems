# find the cube sum of in the range 
# N=2 and M=5
# means we have to solve the cube from 2 to 5

n = int(input())
m = int(input())

cube_sum = 0

i=n
while i<=m:
    cube_sum+= i*i*i
    i+=1
print(cube_sum)


