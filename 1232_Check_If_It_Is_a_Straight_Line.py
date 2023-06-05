def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True

    y_value = coordinates[1][1] - coordinates[0][1]
    x_value = coordinates[1][0] - coordinates[0][0]
    for i in range(2, len(coordinates)):
        if (coordinates[i][0] - coordinates[1][0]) * y_value != (coordinates[i][1] - coordinates[1][1]) * x_value:
            return False
    return True


if __name__ == '__main__':
    print(checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
    print(checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
    print(checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]]))
    print(checkStraightLine(coordinates = [[2,4],[2,5],[2,8]]))
    print(checkStraightLine(coordinates = [[1,1],[2,2],[2,0]]))
    print(checkStraightLine(coordinates = [[0,0],[0,5],[5,5],[5,0]]))