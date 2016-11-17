import time
import helpers

start = time.clock()
matrixFile = open('resources/matrix.txt', 'r')
matrix = []
routeSum = 1000000
numSum = 0
combinations = 0
for line in matrixFile.readlines():
    matrix.append(map(int, line.split(',')))
route = []


def calc_route(route):
    global numSum, routeSum, combinations
    numSum = 0
    for i in route:
        numSum += matrix[i['i']][i['j']]
        # print numSum
    combinations += 1
    if combinations % 10000 == 0:
        print(combinations)
    routeSum = min(numSum, routeSum)


def build_routes(i, j, route, sq_side):
    global numSum, combinations, routeSum
    # route.append(tmpSquare)
    square_value = matrix[i][j]
    numSum += square_value
    if i == sq_side - 1 and j == sq_side - 1:
        routeSum = min(numSum, routeSum)
        combinations += 1
        print(combinations, numSum)
        if routeSum == numSum:
            print('FOUND', routeSum)
    if i + 1 < sq_side and numSum + matrix[i + 1][j] < routeSum:
        build_routes(i + 1, j, route, sq_side)
        # route.pop()
    if j + 1 < sq_side and numSum + matrix[i][j + 1] < routeSum:
        build_routes(i, j + 1, route, sq_side)
        # route.pop()
    numSum -= square_value


# route = []
# route.append(matrix[0][0])
# i=0;j=0
# while i < 80:
#     while j < 80:
#         route.append(matrix[i][j])
#         j+=1
#     else:
#         j=79
#     i+=1
#     if i==80 and j == 80:
#         routeSum = max(sum(route),routeSum)
build_routes(0, 0, route, 80)

print('+' * 20)
print(routeSum)
# print sum(route)

print('-' * 20)
print(time.clock() - start)
