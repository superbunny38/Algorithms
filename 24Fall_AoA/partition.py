def is_partition(points):
    sorted_x = [p[0] for p in points]
    sorted_y = [p[1] for p in points]
    
    if len(points)%2 == 0:
        mid_x = (sorted_x[int(len(sorted_x)//2)]+sorted_x[int(len(sorted_x)//2-1)])/2
        mid_y = (sorted_y[int(len(sorted_y)//2)]+sorted_y[int(len(sorted_y)//2-1)])/2
    else:
        mid_x = sorted_x[int(len(sorted_x)//2)]
        mid_y = sorted_y[int(len(sorted_y)//2)]
    
    n_1 = 0
    n_2 = 0
    n_3 = 0
    n_4 = 0
    
    for point in points:
        x,y = point[0],point[1]
        if x<mid_x and y<mid_y:
            n_1 +=1
        if n_1>len(sorted_x)//4:
            return False
        if x>mid_x and y<mid_y:
            n_2+=1
        if n_2>len(sorted_x)//4:
            return False
        if x<mid_x and y>mid_y:
            n_3 +=1
        if n_3>len(sorted_x)//4:
            return False
        if x>mid_x and y>mid_y:
            n_4+=1
        if n_4 > len(sorted_x)//4:
            return False
    return True
