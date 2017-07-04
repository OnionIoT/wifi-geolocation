# oled expansion helper

from OmegaExpansion import oledExp

oledExp.driverInit()
oledExp.clear()

def clear():
    oledExp.clear()

def writeLines(lines, startingRow=0, startingColumn=0, printBlock=False):
    # set the cursor to the beginning of the row where you want to start printing
    oledExp.setCursor(startingRow, startingColumn)
    
    # write the lines row by row
    for i in range (0,len(lines)):
        # choose between printing at column 0 on newlines
        # or printing from the same column
        if i == 0 or printBlock:
            column = startingColumn
        else:
            column = 0
                
        oledExp.setCursor(startingRow + i, column)
        oledExp.write(lines[i])
        