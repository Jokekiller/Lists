# define functions

def GetGridSize():
    validGrid = False
    while validGrid == False:
        thisGridSize = int(input("Enter a grid size(Max 20 ): "))
        if thisGridSize <= 20:
            validGrid == True
        else:
            validGrid == False
    return thisGridSize

def GetGridRow(aRowLength):
    # draws a single row using |_ for each square
    thisRow = '|_' * (aRowLength)
    # add closing | to row
    thisRow = thisRow + '|'
    return thisRow

def DisplayGrid(thisGridSize, aRow):
    # display top of grid using _ as top of each square
    print(' _' * thisGridSize)
    # display rows of |_| for each row
    for rowCount in range(thisGridSize):
        print(aRow)

# main program
thisGridSize = GetGridSize()
rowToDraw = GetGridRow(thisGridSize)
DisplayGrid(thisGridSize, rowToDraw)
