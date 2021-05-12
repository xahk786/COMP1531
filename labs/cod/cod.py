from helper import on_segment
from helper import orientation
from helper import intersects

def simulate(commando_points, turret_points, base_points):    
    
    commando_list = commando_points
    barrier_len = len(base_points)
    attack_list = []
    barrier_list = []
    
    for c in commando_points:
        for t in turret_points:
            if t[0] - c[0] == 0:
                line = {'t_point' : (t[0],t[1]),
                       'c_point' : (c[0],c[1]),
                       }
                attack_list.append(line)
                continue
           
            line = {'t_point' : (t[0],t[1]),
                    'c_point' : (c[0],c[1]),
                    }
            
            attack_list.append(line)
    i = 0
    b_l = base_points 
    
    temp = []
    temp = [b_l[0], b_l[len(b_l) - 1]]
    
    if (temp[1][0] - temp[0][0]) == 0:
        base_line_special = {'b_point_1' : (temp[0][0],temp[0][1]),
                            'b_point_2' : (temp[1][0],temp[1][1]),
                            }
    
    else:
        base_line_special = {'b_point_1' : (temp[0][0],temp[0][1]),
                            'b_point_2' : (temp[1][0],temp[1][1]),
                            }    
    
            
    while True:

        if b_l[i+1][0] - b_l[i][0] == 0:
            base_line = {'b_point_1' : (b_l[i][0],b_l[i][1]),
                         'b_point_2' : (b_l[i+1][0],b_l[i+1][1]),
                        }
            barrier_list.append(base_line)
            del b_l[:1]
            if len(b_l) == 1:
                barrier_list.append(base_line_special)
                break
            continue

        base_line = {'b_point_1' : (b_l[i][0],b_l[i][1]),
                    'b_point_2' : (b_l[i+1][0],b_l[i+1][1]),
                    }
               
        barrier_list.append(base_line)
        del b_l[:1]
        if len(b_l) == 1:
            barrier_list.append(base_line_special)
            break   
    
    #At this point we have aquired a list of line segments, those which are attack lines (in attack_list) and barrier lines (barrier)list)
    #E.g:  data = {'attack_list' : attack_list, 'barrier_list' : barrier_list }
    #Method:
    #Create an if two segments intersect function that returns either true or false 
    #Check whether or not that: for each attack line : All barrier lines do not intercept with that attack line
    #If all barrier lines (edges of the polygon) do not intersect the attack line, then the commando is killed and we can remove the commando from the commando list

    check = 0 #increments by 1 each time an attack misses a barrier (does not intersect), check resets to 0 for every attack_line iteration, if check == num_barriers, commando is killed

    for a in attack_list:
        check = 0
        for b in barrier_list:
            
            turret = a["t_point"]
            commando = a["c_point"]
            
            b_p1 = b["b_point_1"]
            b_p2 = b["b_point_2"]
            
            segment_1 = (turret, commando)
            segment_2 = (b_p1, b_p2)
            
            if intersects(segment_1, segment_2) == False:
                check = check+1
            
            if check == barrier_len:
                check = 0
                if a["c_point"] in commando_list:
                    commando_list.remove(a["c_point"])
        

    return commando_list