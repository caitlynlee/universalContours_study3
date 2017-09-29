import itertools as iter
import math

size(500, 500, P2D)
num_images = 20
num_vertices = 12

for prop in range(7,11):
    prop_curves = prop*0.1
    
    num_curves = math.floor(num_vertices * prop_curves)
    combinations = list(iter.combinations(range(num_vertices), num_curves))
    
    t=0
    while (t < num_images):
        #new image
        strokeWeight(2) 
        background(255)
        smooth(4)
        
        pick = int(random(int(math.factorial(num_vertices)/math.factorial(num_curves)/
                        math.factorial(num_vertices - num_curves))))
                        
        pos = combinations[pick]
        print pos
        
        s = createShape()
        s.beginShape()
        
        origin_x = random(50, 451)
        origin_y = random(50, 451) 
        s.vertex(origin_x, origin_y)
        
        prev_x = origin_x
        prev_y = origin_y
        
        curves_drawn = 0
        for i in range (num_vertices):
            
            #adding another vertex in, connecting with a curve
            if (curves_drawn < num_curves and  i == pos[curves_drawn]):
                b1_x = random(50, 451)
                b1_y = random(50, 451)
                
                b2_x = random(50, 451)
                b2_y = random(50, 451)
                
                if (i == num_vertices-1):
                    next_x = origin_x
                    next_y = origin_y 
                
                else:
                    next_x = random(50, 451)
                    next_y = random(50, 451)
                
                s.vertex(prev_x, prev_y)
                
                s.bezierVertex(b1_x, b1_y, b2_x, b2_y, next_x, next_y)
                prev_x = next_x 
                prev_y = next_y
                
                curves_drawn = curves_drawn + 1
                
            #adding another vertex in, connecting with a straight line
            elif (i < num_vertices-1): 
                a_x = random(50, 451)
                a_y = random(50, 451) 
                
                s.vertex(a_x, a_y)    
            
                prev_x = a_x
                prev_y = a_y
                
        s.endShape(CLOSE)    
        shape(s)
    
        filename = ("~path" 
                     + str(num_vertices) + "_" + str(int(num_curves)) + "_" + str(t))
        save(filename)
        
        t = t+1
 
