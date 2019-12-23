from heapq import heappush,heappop

def shortest_path(M,start,goal):
    
    path = []
    frontier = []
    explored = set()
    nodes = []
    
    start_cordinates = M.intersections[goal]
    goal_cordinates = M.intersections[goal]
    
    h = ((start_cordinates[0] - goal_cordinates[0])**2 + (start_cordinates[1] - goal_cordinates[1])**2)**(1/2)
    g = 0
    
    starting_point = [h,g,start,start]
    
    finished = False
    fail = False
    
    heappush(frontier,starting_point)
    
    
    while not finished and not fail:
        
        if len(frontier) == 0:
            fail = True
            break 
        else:
            
            next_state = heappop(frontier)
            
            nodes.append(next_state)
            
            g = next_state[1]
            state = next_state[2]
            parent_state_cordinates = M.intersections[state]
            
            explored.add(state)
            
            neighboures = M.roads[state]
            
            
            for cell in neighboures:
                
                if cell == goal:
                    
                    g2 = g + ((state_cordinates[0] - parent_state_cordinates[0])**2 + (state_cordinates[1]-parent_state_cordinates[1])**2)**(1/2)
                    nodes.append([g2,g2,goal,state])
                    explored.add(goal)
                    finished = True
                    break
                    
                else:
                    
                    
                    if cell not in explored :
                        
                        state_cordinates = M.intersections[cell]
                        g2 = g + ((state_cordinates[0] - parent_state_cordinates[0])**2 + (state_cordinates[1] - parent_state_cordinates[1])**2)**(1/2)
                        
                        h = ((state_cordinates[0] - goal_cordinates[0])**2 + (state_cordinates[1] - goal_cordinates[1])**2)**(1/2)
                        f = g2 + h
                 
                        heappush(frontier,[f,g2,cell,state])
            
            
            
            
    if fail == True:
        print('Goal cant be found')
    else:    
        point = goal
        path.append(point)
    
        while point != start:
            for cell in nodes:
            
                if point == cell[2]:
                    point = cell[3]
                    path.append(point)
                    break 
        
        path.reverse()    
    
    return path

