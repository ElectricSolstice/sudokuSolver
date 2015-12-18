#GUI part of the sudoku solver
import sudokuSolver
import tkinter
from tkinter import messagebox

sudokuWindow = tkinter.Tk()
sudokuWindow.withdraw()
window = tkinter.Toplevel()
window.protocol("WM_DELETE_WINDOW",sudokuWindow.destroy)

class SudokuBox(tkinter.Entry):
    def __init__(self, rootWindow, syms):
        self.value = tkinter.StringVar()
        tkinter.Entry.__init__(self,rootWindow,width=5,textvariable=self.value)

    def set(self, newValue):
        self.value.set(newValue)

standard = tkinter.IntVar()
options = tkinter.Checkbutton(window, text="Is it a standard sudoku? (1-9)", variable=standard)
options.pack()

text = tkinter.Label(window,text = "If not, which symbols are used in this sudoku?\nSeperate the symbols using space")
text.pack()

symbols = tkinter.StringVar()
symbolEntry = tkinter.Entry(window, textvariable=symbols)
symbolEntry.pack()

text = tkinter.Label(window,text = "Also, if not a standard sudoku, what is the size of the squares?")
text.pack()

sizeFrame = tkinter.Frame(window)
sizeFrame.pack()

sizeX = tkinter.StringVar()
sizeEntry = tkinter.Entry(sizeFrame, textvariable=sizeX)
sizeEntry.pack(side=tkinter.LEFT)

text = tkinter.Label(sizeFrame, text = " by ")
text.pack(side=tkinter.LEFT)

sizeY = tkinter.StringVar()
sizeEntry= tkinter.Entry(sizeFrame, textvariable=sizeY)
sizeEntry.pack(side=tkinter.LEFT)

sudoku = []
def sudokuData():
    global sudoku
    data = []
    for row in range(len(sudoku)):
        data.append([])
        for box in sudoku[row]:
            data[row].append(box.get())
    return data

syms = None
squareLength = None
squareHeight = None

def startSudokuWindow():
    global standard
    global syms
    global sudoku
    global squareLength
    global squareHeight
    if standard.get() == 1:
        squareLength = 3
        squareHeight = 3
        syms = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    else:
        try: 
            squareLength = int(sizeX.get()) 
            squareHeight = int(sizeY.get())
        except ValueError:
            messagebox.showerror("Error","Square size is incorrect")
            return
        syms = symbols.get().split()
        if squareLength * squareHeight != len(syms):
            messagebox.showerror("Error","Square size is incorrect")
            return
    #Add every sudoku box row by row
    for height in range(len(syms)):
        sudoku.append([])
        frame = tkinter.Frame(sudokuWindow)
        frame.pack()
        for length in range(len(syms)):
            sudoku[height].append(SudokuBox(frame,syms))
            sudoku[height][length].pack(side=tkinter.LEFT)
    window.withdraw()
    sudokuWindow.deiconify()

def guiSolve():
    global sudoku
    global squareLength
    global squareHeight
    solution = sudokuSolver.bruteSolve(sudokuData(),syms,squareLength,squareHeight)
    if solution:
        for row in range(len(solution)):
            for box in range(len(solution[row])):
                sudoku[row][box].set(solution[row][box])
    else:
        messagebox.showinfo("No solution","A solution could not be found")

solveButton = tkinter.Button(sudokuWindow,text="solve",command=guiSolve)
solveButton.pack(side=tkinter.BOTTOM)

acceptSymbols = tkinter.Button(window,text="next", command=startSudokuWindow)
acceptSymbols.pack()

window.mainloop()
