# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    x1 = left1
    y1 = top1
    x2 = left1 + width1
    y2 = top1 + height1
    n1 = left2
    m1 = top2
    n2 = left2 + width2
    m2 = top2 + height2
    if(((x1 <= n1 and n1 <= x2) or (x1 <= n2 and n2 <= x2) or (n1 <= x1 and x1 <= n2) or (n1 <= x2 and x2 <= n2)) and ((y1 <= m1 and m1 <= y2) or (y1 <= m2 and m2 <= y2) or (m1 <= y1 and y1 <= m2) or (m1 <= y2 and y2 <= m2))):
        return True
    return False


        