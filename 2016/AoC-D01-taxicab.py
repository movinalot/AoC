vectors_str = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"
#vectors_str = "R8,R4,R4,R8"
vectors = vectors_str.split(',')

direction_facing = ['N']
x = 0
y = 0

points = [(0,0)]

for vector in vectors:

    print "Current Facing direction: " + direction_facing[0]
    
    #print vector.strip()[0]
    #print vector.strip()[1:]

    traveled = vector.strip()[1:]
    steps = int(traveled)

    # Going right
    if vector.strip()[0] == 'R' and direction_facing[0] == 'N':
        direction_facing[0] = 'E'
        print "Turned Right Facing East and went " + traveled + " steps."
        #x = x + steps
        for step in range(1,steps + 1):
            x = x + 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)
        
    elif vector.strip()[0] == 'R' and direction_facing[0] == 'E':
        direction_facing[0] = 'S'
        print "Turned Right Facing South and went " + traveled + " steps."
        #y = y - steps
        for step in range(1,steps + 1):
            y = y - 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)
        
    elif vector.strip()[0] == 'R' and direction_facing[0] == 'S':
        direction_facing[0] = 'W'
        print "Turned Right Facing West and went " + traveled + " steps."
        #x = x - steps
        for step in range(1,steps + 1):
            x = x - 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)
            
    elif vector.strip()[0] == 'R' and direction_facing[0] == 'W':
        direction_facing[0] = 'N'
        print "Turned Right Facing North and went " + traveled + " steps."
        #y = y + steps
        for step in range(1,steps + 1):
            y = y + 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)

    # Going left
    if vector.strip()[0] == 'L' and direction_facing[0] == 'N':
        direction_facing[0] = 'W'
        print "Turned Left Facing West and went " + traveled + " steps."
        #x = x - steps
        for step in range(1,steps + 1):
            x = x - 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)
        
    elif vector.strip()[0] == 'L' and direction_facing[0] == 'W':
        direction_facing[0] = 'S'
        print "Turned Left Facing South and went " + traveled + " steps."
        #y = y - steps
        for step in range(1,steps + 1):
            y = y - 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)
        
    elif vector.strip()[0] == 'L' and direction_facing[0] == 'S':
        direction_facing[0] = 'E'
        print "Turned Left Facing East and went " + traveled + " steps."
        #x = x + steps
        for step in range(1,steps + 1):
            x = x + 1
            point = (x, y)
            
            if point in points:
                print "I've been here before",point
                break
                
            points.append(point)
        
    elif vector.strip()[0] == 'L' and direction_facing[0] == 'E':
        direction_facing[0] = 'N'
        print "Turned Left Facing North and went " + traveled + " steps."
        #y = y + steps
        for step in range(1,steps + 1):
            y = y + 1
            point = (x, y)
            
            if point in points:
                print "I've been here before", point
                break
                
            points.append(point)

    print x, y

    #point = (x, y)

    #if point in points:
    #    print "I've been here before"
    #    print point
        #break

    #points.append(point)

print points
