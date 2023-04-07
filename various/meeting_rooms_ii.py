from collections import defaultdict


def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort()
    rooms = defaultdict(list)
    print(f"sorted intervals: {intervals}")

    # go through each interval
    for interval in intervals:
        # find out which room to add it in
        print(f"current interval: {interval}")
        added = False
        for room, r_intervals in rooms.items():
            last_meeting = r_intervals[-1]
            if last_meeting[1] <= interval[0]:
                rooms[room].append(interval)
                added = True
                break
        if not added:
            rooms[len(rooms)].append(interval)
    print(rooms)

    return len(rooms)


intervals = [[1293, 2986], [848, 3846], [4284, 5907],
             [4466, 4781], [518, 2918], [300, 5870]]
# sorted intervals: [[300, 5870], [518, 2918], [848, 3846], [1293, 2986], [4284, 5907], [4466, 4781]]
print(minMeetingRooms(intervals))
# Output: 4
# {
#     0: [[300, 5870]],
#     1: [[518, 2918], [4284, 5907]],
#     2: [[848, 3846], [4466, 4781]],
#     3: [[1293, 2986]]
# }
