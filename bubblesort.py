def bubble_sort(given_list):
    
    for _ in range(len(given_list)):
        for i in range(len(given_list) - 1):    
            
            if given_list[i] > given_list[i + 1]:
                # Make swap between i and i + 1
                temp = given_list[i]
                given_list[i] = given_list[i + 1]
                given_list[i + 1] = temp
    
    # return sorted list
    return given_list

print(bubble_sort([]))
