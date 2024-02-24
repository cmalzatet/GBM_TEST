def jumps():    
    n_cases = int(input())
    cases = []    
    for i in range(n_cases):
        cases.append(int(input()))
        
    for x in cases:
        k = 0
            
        while (k*(k+1)) < 2*x:
            k+=1
        
        if (k*(k+1))/2 == x+1:
            k+=1
            
        print(k)
    

if __name__ == "__main__":
    jumps()
