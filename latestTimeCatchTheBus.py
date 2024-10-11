class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        end = len(passengers)
        j = 0  # next passengers in line for buses
        count = 0
        for bus in buses:
            count =  0
            while j < end and passengers[j] <= bus and count < capacity:
                j += 1
                count += 1
        if count < capacity and (j == 0 or (j > 0 and passengers[j - 1] < buses[-1])):
            return buses[-1]
        j -= 1
        res = passengers[j] - 1
        while j > 0 and res == passengers[j-1]:
            res -= 1
            j -= 1
        return res
