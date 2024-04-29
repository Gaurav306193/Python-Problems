# input are ["apple",1.0,5],["orange",10.0,5],["apple",10.0,5]

# outputs are find rates : [5+50+50]
# 1.0*1=5 , 10.0*5= 50, 10.0*5= 5033
# string is given only for confusions

arr = []
n = int(input())
rates = 0

for _ in range(n):
    x = input()
    y = float(input())
    z = int(input())
    rates += y * z
    arr.append((x, [(y, z)]))

print(rates / n)
print(arr)
