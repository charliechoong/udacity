def shortest_path(M, start, goal):
    
    def compute_straight_line_distance(pos1, pos2):
        # Helper function to compute straight line distance between 2 coordinates
        x1, y1 = M.intersections[pos1]
        x2, y2 = M.intersections[pos2]
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def get_h_val(pos):
        # Helper function to compute h(s) from pos to goal
        return compute_straight_line_distance(pos, goal)
    
    print("shortest path called")
    
    neighbors = M.roads
    # at any time, intersections are stored in one of 3 sets: explored, frontier, unexplored
    unexplored, frontier, explored = set(), set(), set()
    
    # initialise start in frontier and all other intersections in unexplored
    g_val = get_h_val(start)
    for intersection in M.intersections:
        if intersection == start:
            frontier.add((g_val, intersection))
        else:
            unexplored.add(intersection)
            
    
    # Track the path in format of (prev_node, shortest actual distance from start) eg. d['C']: ('A', 0.67)
    path_track = {start: (None, 0)} 
    
    # while frontier is not empty
    while len(frontier) > 0:
        # remove the intersection with lowest g(s)=f(s)+h(s) value
        g_val, curr = frontier.pop()
        # process node, perform goal test, then put into explored
        if curr == goal:
            print('goal reached')
            explored.add(curr)
            break
        else:
            explored.add(curr)
        # expand curr and add unexplored neighbors to frontier with f(s)
        # update path dict
        for neighbor in neighbors[curr]:
            # Update shorter distance to an explored intersection
            f_s = path_track[curr][1] + compute_straight_line_distance(curr, neighbor)
            g_s = f_s + get_h_val(neighbor)
            if (neighbor in explored or neighbor in [n[0] for n in frontier]) and g_s < path_track[neighbor][1]:
                path_track[neighbor] = (curr, f_s)
            elif neighbor in unexplored:
                unexplored.remove(neighbor)
                frontier.add((f_s, neighbor))
                path_track[neighbor] = (curr, f_s)
            
    # retrace the path
    path, total_dist = [goal], 0
    curr = goal
    while curr != start:
        prev_pos, dist = path_track[curr]
        path.insert(0, prev_pos)
        total_dist += dist
        curr = prev_pos
    print(f'path = {path} completed in {total_dist} distance')
    return path