def findRestaurant(list1, list2):
    res = []
    min_sum = float('inf')
    for i in range(len(list1)):
        if list1[i] in list2:
            idx_2 = list2.index(list1[i])
            if idx_2 + i < min_sum:
                min_sum = idx_2 + i
                res = [list1[i]]
            elif idx_2 + i == min_sum:
                res.append(list1[i])
    return res

if __name__ == '__main__':
    print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
                         list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
    print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
                         list2 = ["KFC","Shogun","Burger King"]))
    print(findRestaurant(list1 = ["happy","sad","good"],
                         list2 = ["sad","happy","good"]))