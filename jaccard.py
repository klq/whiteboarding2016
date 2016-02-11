def j(l1, l2):
    intersect =  set(l1) & set(l2)
    union = set(l1) | set(l2)
    return float(len(intersect))/float(len(union))

def j_longversion_as_we_were_working_it_out(*args):
    # Testing condition 1-3
    if len(args) != 2:
        raise TypeError('Number of arguments is invalid.')

    set0 = set(args[0])
    set1 = set(args[1])
    intersect = set0 & set1
    union = set0 | set1

    # Testing condition 4-6
    if set0 == set1:
        return float(1.0)
    
    # Testing condition 7
    if intersect == set():
        return 0

    # All the rest
    return float(len(intersect))/float(len(union))