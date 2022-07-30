"""
Amazon OA 2 - Get Minimum Cost
Amazon ships millions of packages regularly. There are a number of parcels that need to be shipped. Computer the minimum
possible sum of transportation costs incurred in the shipment of additional parcels in the following scenario.

- A fully loaded truck carries k parcels.
- It is most efficient for the truck to be fully loaded.
- There are a number of parcels already on the truck as listed in parcels[].
- There are parcels with a unique id that ranges from 1 through infinity.
- The parcels id is also the cost to ship that parcel.

Given the parcel IDs which are already added in the shipment, find the minimum possible cost of shipping the items added
to complete the load.

Example:
parcels = [2, 3, 6, 10, 11]
k = 9
output = 17 since the sum of [1, 4, 5, 7] is 17
"""

def getMinimumCost(parcels, k):
    if len(parcels) == k:
        return 0

    res = []
    parcels.sort()
    num = 1
    while len(res) < k - len(parcels):
        if num not in parcels:
            res.append(num)
        num = num + 1
    return sum(res)

if __name__ == '__main__':
    print(getMinimumCost(parcels = [2, 3, 6, 10, 11], k = 9))
    print(getMinimumCost(parcels = [1, 7], k = 2))