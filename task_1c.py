n=int(input('Enter the size of the map (n): '))
m=int(input('Enter blast region (m): '))

print('Enter the entire map row by row: ')
print('0 for water, and 1 for land ')
grid = [list(map (int, input().split())) for _ in range(n)]

radius = m//2
maxLand = 0     # max land destroyed
# co-ordinates of the best bomb centre
bestX = -1
bestY = -1

# to check for the bomb centres
for y in range (radius, n-radius):
    for x in range (radius, n-radius):
        i=0