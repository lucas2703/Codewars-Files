def valid_solution(board):  
    print(board)
    # check rows
    for i in range(len(board)):
        if sorted(board[i]) != list(range(1, 10)):
            return False
        # check cols
        check_col = [item[i] for item in board]
        if sorted(check_col) != list(range(1,10)):
            return False
        
    # check 3x3
    for a in range(0, 9, 3):
        _square = []
        for i in range(a, a + 3):
            for j in range(a, a + 3):
                _square.append(board[i][j])
                #print(_square)
        #print(sorted(_square[i]))
        if sorted(_square) != list(range(1, 10)):
            return False
    
    return True