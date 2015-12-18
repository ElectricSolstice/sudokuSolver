#Functions that handle the logic of solving a sudoku

def sudokuEqual(one,two):
    if one != "" and len(one.split(" ")) == 1:
        if one == two:
            return True
    return False

def checkRows(sudoku):
    for row in sudoku:
        for i in range(len(row)):
            for j in range(i+1,len(row)):
                if sudokuEqual(row[i],row[j]):
                    return False
    return True

def checkColumns(sudoku):
    #The number of sudoku boxes in a row equals
    #the number of columns
    for column in range (len(sudoku[0])):
        for height in range(len(sudoku)):
            for i in range(height+1,len(sudoku)):
                if sudokuEqual(sudoku[height][column],sudoku[i][column]):
                    return False
    return True

def checkSquares(sudoku,squareLength,squareHeight):
    for square in range(len(sudoku[0])):
        for i in range(len(sudoku[0])):
            for j in range(i+1,len(sudoku[0])):
                #adds the square offset, checking the squares and boxes 
                #from left to right rather than top to bottom
                if sudokuEqual(sudoku[int(i/squareLength)+int(square/squareHeight)*squareHeight]\
                         [i%squareLength+square%squareHeight*squareLength],          \
                   sudoku[int(j/squareLength)+int(square/squareHeight)*squareHeight]\
                         [j%squareLength+square%squareHeight*squareLength]):
                    return False
    return True


def checkAll(sudoku,squareLength,squareHeight):
    if checkRows(sudoku):
        if checkColumns(sudoku):
            if checkSquares(sudoku,squareLength,squareHeight):
                return True
    return False

def bruteSolve(sudoku,symbols,squareLength,squareHeight):
    sudokuCopy = sudoku
    solution = [] 
    backtrack = []
    for row in range(len(sudoku)):
        for box in range(len(sudoku[row])):
            #skip over squares that don't need to be solved
            if len(sudoku[row][box].split()) == 1:
                continue
            #solve by plugging in symbols and checking
            else:
                symbol = iter(symbols)
                currentRow = row
                currentBox = box
                #while true, try a symbol
                while True:
                    try:
                        value = next(symbol)
                        solution.append([currentRow,currentBox,value,symbol])
                        sudokuCopy[currentRow][currentBox] = value
                        if checkAll(sudokuCopy,squareLength,squareHeight) and not backtrack:
                            break
                        elif checkAll(sudokuCopy,squareLength,squareHeight):
                            symbol = backtrack[-1][3]
                            currentRow = backtrack[-1][0]
                            currentBox = backtrack[-1][1]
                            backtrack.pop()
                        else:
                            solution.pop()
                            sudokuCopy[currentRow][currentBox] = ""
                    #when out of symbols to try for current
                    #box, try next symbol for previous box
                    except StopIteration:
                        if not solution:
                            return None
                        symbol = solution[-1][3]
                        pastRow = solution[-1][0]
                        pastBox = solution[-1][1]
                        solution[-1][3] = iter(symbols)
                        solution[-1][0] = currentRow
                        solution[-1][1] = currentBox
                        currentRow = pastRow
                        currentBox = pastBox
                        backtrack.append(solution.pop())
                        sudokuCopy[currentRow][currentBox] = ""
    return sudokuCopy
