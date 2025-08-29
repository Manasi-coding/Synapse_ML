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
for x in range (radius, n-radius):
    for y in range (radius, n-radius):
        
        #the bomb can detonate only on land
        if grid[x][y] == 1:
            count_land = 0
            for i in range (x-radius, x+radius+1):
                for j in range (y-radius, y+radius+1):
                    if grid[i][j] == 1:
                        count_land += 1
            
            if count_land > maxLand:
                maxLand = count_land
                bestX = x
                bestY = y

if bestX == -1:
    print('BOMB DID NOT DETONATE!')

else:
    Y = n-bestY
    print(f'Best place to drop the bomb: {bestX}, {Y}')
    print('Destroyed cells: ')
    for i in range (bestX-radius, bestX+radius+1):
        for j in range (bestY-radius, bestY+radius+1):
            print(f'({i}, {n-j})', end=' ')