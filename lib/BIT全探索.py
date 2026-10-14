for bit in range(1 << N):
        
       
        selected_elements = []
        
        for i in range(N):
            if (bit >> i) & 1:
                
                selected_elements.append(i)