def grand_prix():
    input_list = []
    user_input = ""
    while user_input.strip(' ') != "0 0":
        user_input = input()
        input_list.append(user_input.strip(' '))
        
    user_input = input_list[:-1]
    
    while len(user_input) > 1:
        race_number = [int(i) for i in user_input[0].split(' ')][0]
        sco_sys_number = [int(i) for i in user_input[1+race_number].split(' ')][0]
        
        test = [[int(i) for i in line.split()] for line in user_input[0:2 + race_number + sco_sys_number]]
        
        G = test[0][0]
        P = test[0][1]
        S = test[1+G][0]        
        
        for SS in test[2+G:]:
            total_score = [0] * P             
            num_prem = SS.pop(0)
            SS.extend([0]*(P-num_prem))
            
            for result in test[1:G+1]:                
                total_score = [total_score[i] + SS[result[i]-1] for i in range(P)]
                
            print(" ".join([str(i+1) for i,value in enumerate(total_score) if value == max(total_score)]))
            
            
        del user_input[0:2 + race_number + sco_sys_number]
    

if __name__ == "__main__":
    grand_prix()
