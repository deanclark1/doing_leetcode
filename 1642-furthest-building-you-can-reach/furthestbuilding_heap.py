from heapq import *
def furthestBuilding(heights, bricks, ladders):
    """
    :type heights: List[int]
    :type bricks: int
    :type ladders: int
    :rtype: int
    """
    biggest_jumps = []
    ladders_used = 0
    pos = 0
    while pos < len(heights) - 1:
        jump = heights[pos+1]-heights[pos]
        if jump > 0:
            if ladders_used < ladders:
                heappush(biggest_jumps, jump)
                ladders_used += 1
            else:
                if ladders == 0 or jump < biggest_jumps[0]:
                    if bricks < jump:
                        return pos
                    else:
                        bricks = bricks - jump
                else:
                    old_jump = heappop(biggest_jumps) 
                    if bricks >= old_jump: 
                        bricks = bricks - old_jump 
                        heappush(biggest_jumps, jump)
                    else:
                        return pos
        pos = pos + 1
    return pos

#heights, bricks, ladders = [4,12,2,7,3,18,20,3,19], 10, 2
#heights, bricks, ladders = [14,3,19,3], 17, 0
#heights, bricks, ladders = [4,2,7,6,9,14,12], 5, 1
#print(furthestBuilding(heights, bricks, ladders))