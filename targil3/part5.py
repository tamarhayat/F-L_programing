
def sortedzip(lists):
    if not lists or not lists[0]:
        return []
    
    # Sort each list in lists
    sorted_lists = list(map(sorted, lists))
    
    # Create a tuple for the first elements of each sorted list
    first_elements = tuple(sorted_lists[i][0] for i in range(len(sorted_lists)))
    
    # Recursively call sortedzip for the remaining elements
    return [first_elements] + sortedzip([lst[1:] for lst in sorted_lists])


def sortedzip_t(lists):
    def sortedzip_tail(sorted_lists, result):
        if all(len(lst) == 0 for lst in sorted_lists):
            return result

        #check the first element in each list
        heads = [lst[0] for lst in sorted_lists if lst]  
        if len(heads) == 0:
            return result
        
        #get the tails of the lists
        tails = [lst[1:] for lst in sorted_lists]  
        return sortedzip_tail(tails, result + [tuple(heads)])

    # sorted the lists in the outer function
    sorted_lists = list(map(sorted, lists))
    return sortedzip_tail(sorted_lists, [])


#print(sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]))
#print(sortedzip_t([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]))
