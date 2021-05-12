'''
Checking if two line segments intersect returns True if they intersect and False otherwise.
This helper function is sourced from https://www.kite.com/python/answers/how-to-check-if-two-line-segments-intersect-in-python
'''
def on_segment(p, q, r):

#check if r lies on (p,q)


    if r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]):
        return True
    else:
        return False

def orientation(p, q, r):
#return 0/1/-1 for colinear/clockwise/counterclockwise


    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0 : 
        return 0
        
    elif val > 0 : 
        return 1
    else :
        return-1

def intersects(seg1, seg2):
#check if seg1 and seg2 intersect

    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1, p2)
#find all orientations

    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

#check general case
    if o1 != o2 and o3 != o4:
        return True

#check special cases    
    if o1 == 0 and on_segment(p1, q1, p2): 
        return True

    if o2 == 0 and on_segment(p1, q1, q2): 
        return True
    
    if o3 == 0 and on_segment(p2, q2, p1): 
        return True
    
    if o4 == 0 and on_segment(p2, q2, q1): 
        return True

    return False

    
