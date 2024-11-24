def majority_element(A):
    def majority(low, high):
        if low == high:  
            return A[low]
        
        mid = (low + high) // 2
        left_majority = majority(low, mid)
        right_majority = majority(mid + 1, high)
        
        if left_majority == right_majority:
            return left_majority
        
        left_count = 0
        right_count = 0
        for i in range(low, high + 1):
            if A[i] == left_majority:
                left_count += 1
            if A[i] == right_majority:
                right_count += 1
        
        if left_count > (high - low + 1) // 2:
            return left_majority
        if right_count > (high - low + 1) // 2:
            return right_majority
        
        return None
    
    return majority(0, len(A) - 1)

def majority_element2(A):
    def reduce_pairs(A):
        reduced = []
        i = 0
        while i < len(A) - 1:
            if A[i] == A[i + 1]:
                reduced.append(A[i])#Αν είναι ίδια,κρατάμε το ένα
            #Αν είναι διαφορετικά,απορρίπτουμε και τα δύο
            i += 2
        #Αν το μήκος είναι περιττό
        if len(A) % 2 == 1:
            reduced.append(A[-1])
        return reduced

    #Αναδρομική μείωση
    def find_candidate(A):
        if len(A) == 1:
            return A[0]#Μόνο ένα στοιχείο
        if len(A) == 0:
            return None#Κενή λίστα
        reduced = reduce_pairs(A)
        return find_candidate(reduced)

    #Επαλήθευση
    candidate = find_candidate(A)
    if A.count(candidate) > len(A) // 2:
        return candidate
    else:
        return None



A = [2, 3, 9, 7, 2, 2, 5, 2]
print("Πλειοψηφούν στοιχείο:", majority_element(A))  

A = [2, 3, 9, 2, 2, 2, 5, 2]
print("Πλειοψηφούν στοιχείο:", majority_element2(A)) 
