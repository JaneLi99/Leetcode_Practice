class MyCalendar:
    def __init__(self):
        self.cal = [(0, 0), (10 ** 9, 10 ** 9)]

    def book(self, start: int, end: int) -> bool:
        # Binary Search
        l, r = 0, len(self.cal)
        while l < r:
            mid = (l + r) // 2
            if end == self.cal[mid][0]:
                l = mid
                break
            elif end > self.cal[mid][0]:
                l = mid + 1
            else:
                r = mid

        # l index
        if start < self.cal[l - 1][1]:
            return False

        self.cal.insert(l, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10, 20)
# return True

param_2 = obj.book(15, 25)
# return False, It can not be booked because time 15 is already booked by another event.

param_3 = obj.book(20, 30)
# return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

print(param_1, param_2, param_3)