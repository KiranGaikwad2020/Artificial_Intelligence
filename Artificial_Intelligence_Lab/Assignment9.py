def minimax(node, depth, player):
    if depth == 0:
        return value(node)
    
    if player == 'MAX':
        alpha = ('-inf')
        for child in children(node):
            val = minimax(B, depth=3, 'MIN')
            alpha = max(alpha, val)
        return alpha
    else:  
        alpha = ('inf')
        for child in get_children(node):
            val = minimax(A, depth =2, 'MAX')
            alpha = min(alpha, val)
        return alpha
