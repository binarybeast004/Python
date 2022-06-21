import queue as Qx
 
        
graph={
        'V1':{'V2':9,'V3':4,},
    
        'V2':{'V1':9, 'V3':2 ,'V4':7 , 'V5': 3},
    
        'V3':{'V1':4, 'V2':2 ,'V4':1 , 'V5': 6},
    
        'V4':{'V2':7, 'V3':1 ,'V5':4 , 'V6': 8},
    
        'V5':{'V2':3, 'V3':6 ,'V4':4 , 'V6': 2},
    
        'V6':{'V4':8 , 'V5': 2},
        }
def Uniform_Cost_Search(startNode, endNode):
    if startNode not in graph:
        print('Start node is not found in graph !')
        return
    if endNode not in graph:
        print('End node is not found in graph !')
        return
    
    queue = Qx.PriorityQueue()
    queue.put((0, [startNode]))
    
    print("\nStarting Node : ",startNode)
    print("Ending Node   : ",endNode)
 
    while not queue.empty():
        node = queue.get()
        #print(node)
        current = node[1][len(node[1]) - 1]
         
        
        if endNode in node[1]:
            print("Uniform Cost Search Path: " + str(node[1]) )
            print("Total Cost =",str(node[0]))
            break
        
        pathCost = node[0]
        for child in graph[current]:
            temp = node[1][:]
            temp.append(child)
            queue.put((pathCost + graph[current][child], temp))
        
     

 
Uniform_Cost_Search('V1', 'V6')



 
