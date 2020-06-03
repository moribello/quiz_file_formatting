import pandas as pd
import numpy as np
import sys

def get_filename():
    while True:
        try:
            filein = sys.argv[1]
            filename = filein[:-4]
            return filename
            break
        except:
            print(filename)
            print("That doesn't appear to be a valid file. Please try again.")
            break

def input_files(filename):
    """opens the quiz file and creates an array"""
    file_input = open("testQuiz02",'r')
    array = np.array(file_input.readlines())
    rows = int(input("How many questions are in this quiz? \n"))
    newarray = np.resize(array, (rows,6))
    return rows, newarray

def format_rows(rows, newarray):
    """Adds answer letters to index columnms 1-4; it skips index 0 and 5 by appending nothing to those particular columns"""
    for row in range(rows):
        line = 0
        letters = ["", "A. ", "B. ", "C. ", "D. ", ""]
        for letter in letters:
            dummystring = letter + newarray[row, line]
            newarray[row, line] = dummystring
            line +=1
        print(newarray[row])
        return newarray

def output_file(newarray, filename):
    """Outputs contents of current dataframe to filename_corrected file"""
    np.savetxt(filename + "_formatted.txt", newarray, delimiter=" ", fmt="%s")

def main():
    filename = get_filename()
    rows, newarray = input_files(filename)
    newarray = format_rows(rows, newarray)
    output_file(newarray, filename)

if __name__ == "__main__":
    main()
