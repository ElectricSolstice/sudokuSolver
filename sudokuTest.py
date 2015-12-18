import sudokuSolver
from sudokuSolver import *

incompleteSudoku= [['1','2','3','4','5','6','7','8','9'],
                   ['4','5','6','7','8','9','1','2','3'],
                   ['7','8','9','1','2','3','4','5','6'],
                   ['','','','','','','','',''],
                   ['','','','','','','','',''],
                   ['','','','','','','','',''],
                   ['','','','','','','','',''],
                   ['','','','','','','','',''],
                   ['','','','','','','','','']]

incorrectSudoku = [['2','1','3','4','5','6','7','2','9'],
                   ['4','5','6','7','8','9','1','8','3'],
                   ['7','8','9','1','2','3','4','5','6'],
                   ['2','3','4','5','6','7','8','9','1'],
                   ['3','4','5','6','7','8','9','1','2'],
                   ['5','6','7','8','9','1','2','3','4'],
                   ['6','7','8','9','1','2','3','4','5'],
                   ['8','9','1','2','3','4','5','6','7'],
                   ['','','','3','4','5','6','7','8']]

correctSudoku = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                 ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
                 ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
                 ['2', '1', '4', '3', '6', '5', '8', '9', '7'],
                 ['3', '6', '5', '8', '9', '7', '2', '1', '4'],
                 ['8', '9', '7', '2', '1', '4', '3', '6', '5'],
                 ['5', '3', '1', '6', '4', '2', '9', '7', '8'],
                 ['6', '4', '2', '9', '7', '8', '5', '3', '1'],
                 ['9', '7', '8', '5', '3', '1', '6', '4', '2']]

print("On correct sudoku")
if not checkAll(correctSudoku,3,3):
    if not checkColumns(correctSudoku):
        print("Error in logic of checkColumns")
    if not checkSquares(correctSudoku,3,3):
        print("Error in logic of checkSquares")
    if not checkRows(correctSudoku):
        print("Error in logic of checkRows")

print("On incomplete sudoku")
if not checkAll(incompleteSudoku,3,3):
    if not checkColumns(incompleteSudoku):
        print("Error in logic of checkColumns")
    if not checkSquares(incompleteSudoku,3,3):
        print("Error in logic of checkSquares")
    if not checkRows(incompleteSudoku):
        print("Error in logic of checkRows")

print("On incorrect sudoku")
if checkColumns(incorrectSudoku):
    print("Error in logic of checkColumns")
if checkSquares(incorrectSudoku,3,3):
    print("Error in logic of checkSquares")
if checkRows(incorrectSudoku):
    print("Error in logic of checkRows")

solution = bruteSolve(incompleteSudoku,['1','2','3','4','5','6','7','8','9'],3,3)
if not checkAll(solution,3,3):
    print("Error in bruteSolve with incomplete sudoku")

none = bruteSolve(incorrectSudoku,['1','2','3','4','5','6','7','8','9'],3,3)
if not none is None:
    print("Error in bruteSolve with incorrect sudoku")

alreadySolved = bruteSolve(correctSudoku,['1','2','3','4','5','6','7','8','9'],3,3)
if not checkAll(alreadySolved,3,3):
    print("Error in bruteSolve with correct sudoku")

#for row in solution:
#    print(row)
