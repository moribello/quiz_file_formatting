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
    """opens the .csv files with student names and creates a dataframe"""
    student_names = pd.read_csv('studentlist01.csv')
    return student_names

def create_usernames(student_names):
    for i in student_names.index:
        usrname = student_names.loc[i,'firstname'][0].lower() + student_names.loc[i,'lastname'].lower()
        student_names.loc[i, 'username'] = usrname
    return student_names

def output_file(student_names, filename):
    """Outputs contents of current dataframe to filename_corrected file"""
    student_names.to_csv(filename +'_formatted.csv', index=False)

def main():
    filename = get_filename()
    student_names = input_files(filename)
    student_names_updated = create_usernames(student_names)
    output_file(student_names_updated, filename)

if __name__ == "__main__":
    main()
