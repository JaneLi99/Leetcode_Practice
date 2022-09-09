def numberOfWeakCharacters(properties):
    properties.sort(key=lambda x: (-x[0], x[1]))
    mxattack = properties[0][0]
    mxdefense = properties[0][1]
    count = 0
    for i in range(1, len(properties)):
        if properties[i][0] < mxattack and properties[i][1] < mxdefense:
            count += 1
        else:
            mxattack = properties[i][0]
            mxdefense = properties[i][1]
    return count

if __name__ == '__main__':
    print(numberOfWeakCharacters(properties = [[5,5],[6,3],[3,6]]))
    print(numberOfWeakCharacters(properties = [[2,2],[3,3]]))
    print(numberOfWeakCharacters(properties = [[1,5],[10,4],[4,3]]))
    print(numberOfWeakCharacters(properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]))