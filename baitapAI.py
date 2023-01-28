#Thuật toán Breadth-first search
def BFS(data, begin, end):
    fringer = []
    close = []
    fringer.append(begin)
    
    while True:
        
        if len(fringer) == 0:
            print("Không tồn tại")
            return
          
        tam = fringer.pop(0)
        close.append(tam)
        
        if end in close:
            print ("Đã tìm thấy:")
            for i in close:
                print(i, end = "    ")
            print()
            return
        
        else:
            try:
                for i in data[tam]:
                    fringer.append(i)
            except:
                continue
         
#Thuật toán Uniform-cost search
def ucs_weight(from_node, to_node, weights=None):
    return weights.get((from_node, to_node), 10e100) if weights else 1

def UCS(data, begin, end, weights=None):
    fringer = []
    close = []
    fringer.append((0, begin))
    m = 0
    while True:
        if len(fringer) == 0:
            print("Không tìm thấy")
            return
        
        fringer.sort(reverse=True)
        ucs_w = fringer[0][0]
        tam = fringer[0][1]
        fringer.pop(0)
        close.append(tam)

        if end in close:
            print("Đã tìm thấy")
            for i in close:
                print(i, end= "    ")
            print()
            return
        else:
            try:
                for i in range(len(data[tam])):
                    fringer.insert(0, (ucs_w + ucs_weight(tam, data[tam][len(data[tam]) - 1 - i], weights), data[tam][len(data[tam]) - 1 - i]))
                m = m + 1
            except:
                # close.clear()
                # close.append(begin)
                continue

#Thuật toán Depth-first search
def DFS(data, begin, end):
    fringer = []
    close = []
    fringer.append(begin)
    
    while True:
        if len(fringer) == 0:
            print("Không tồn tại")
            return  
        
        tam = fringer.pop(0)
        close.append(tam)
        
        if end in close:
            print ("Đã tìm thấy:")
            for i in close:
                print(i, end = "    ")
            print()
            return
        
        else:
            try:
                for i in range(len(data[tam])):
                    fringer.insert(0, data[tam][len(data[tam]) - 1 - i])
            except:
                continue

#Thuật toán Depth-limited search
def DLS(data, begin, end, limit = 5):
    depth = 0
    fringer = []
    close = []
    fringer.append(begin)
    
    while True:
        count = 0
        if len(fringer) == 0:
            print("Không tồn tại")
            return False
       
        tam = fringer.pop(0)
        close.append(tam)
        
        if end in close:
            print ("Đã tìm thấy:")
            for i in close:
                print(i, end = "    ")
            print()
            return True
        
        else:
            try:
                if depth < limit:
                    for i in range(len(data[tam])):
                        fringer.insert(0, data[tam][len(data[tam]) - 1 - i])
                        count = count + 1
                    depth = depth + 1
            except:
                depth = depth - 1
            
        if depth == limit and len(fringer) != 0 and (end not in fringer):
            for i in range(count):
                close.append(fringer[0])
                fringer.pop(0)
            depth = depth - 1
            
        if (depth == limit) and (end in fringer) or (end in close):
            close.append(end)
            print ("Đã tìm thấy:")
            for i in close:
                print(i, end = "    ")
            print()
            return True

        if depth == limit and len(fringer) == 0:
            print("Không tồn tại")
            return
    
#Thuật toán Iterative deepening search
def IDS(data, begin, end):
    M = 1
    while True:
        print("Tầng " + str(M))
        if DLS(data, begin, end, M):
            return
        M = M + 1

def main():
    treedata = {
        'A': ['B' , 'C', 'D'],
        'B': ['E', 'F'],
        'D': ['G'],
        'E': ['H', 'I'],
        'G': ['J', 'K', 'L', 'M']
    }
    BFS(treedata, 'A', 'I')
    UCS(treedata, 'A', 'I')
    DFS(treedata, 'A', 'M')
    DLS(treedata, 'A', 'G', 2)
    IDS(treedata, 'A', 'F')
    
main()