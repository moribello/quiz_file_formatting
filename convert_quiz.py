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
    """opens the quiz and answer files and creates dataframes for each"""
    file_input = open(filename + '.txt','r')
    answers = pd.read_csv(filename + '_answers.txt')
    array = np.array(file_input.readlines())
    numQuestions = int(input("How many questions in this quiz?"))
    newarray = np.resize(array, (numQuestions,6))
    quiz = pd.DataFrame(newarray, columns=['question', 'ans1', 'ans2', 'ans3', 'ans4', 'correct'])
    return quiz, answers

def format_rows(quiz, answers):
    """Removes question number and page reference from question, then writes
    correct answer to "correct" column in DataFrame"""
    for i in quiz.index:
        if quiz.loc[i,'question'][1] == ".":
            quiz.loc[i,'question'] = (str(quiz.loc[i,'question'])[2:-6])+"\n"
        else:
            quiz.loc[i,'question'] = str(quiz.loc[i,'question'])[3:-6] + "\n"
        quiz.loc[i,'correct'] = "ANSWER: " + answers.loc[i][1].strip() + '\n'
    return quiz

def output_file(df, filename):
    """Outputs contents of current dataframe to filename_corrected file"""
    text_array = df.to_numpy()
    np.savetxt(filename + "_corrected.txt", text_array, delimiter=" ", fmt="%s")

def main():
    filename = get_filename()
    quiz, answers = input_files(filename)
    quiz_updated = format_rows(quiz, answers)
    output_file(quiz_updated, filename)

if __name__ == "__main__":
    main()
