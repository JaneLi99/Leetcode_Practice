def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key = lambda list: list[1], reverse = True)
    total_units = 0
    for i in range(len(boxTypes)):
        if boxTypes[i][0] >= truckSize:
            total_units = total_units + boxTypes[i][1] * truckSize
            break
        total_units = total_units + boxTypes[i][0] * boxTypes[i][1]
        truckSize = truckSize - boxTypes[i][0]

    return total_units

if __name__ == '__main__':
    print(maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
    print(maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))