This is the README for the quiz formatting tool.

Quiz file formatting tool for Moodle
====================================

Pre-requisites:
---------------
- Python 3
- NumbPy library
- Pandas library

Description:
------------
This script combine two text files into a single text file that can be uploaded to Moodle using the Aiken import format. The two files must have specific names and formats.

File names:
-----------
The file containing your questions and selections should be called "\<filename\>.txt" and be located in the same directory as the "convert_quiz.py" file.

The file containing the quiz answers should be called "\<filename\>\_answers.txt" and should be located in the same directory as the "convert_quiz.py" and "<filename>.txt" files.

Running the script
------------------
The script accepts the filename as an argument so you can use line completion (because writing a script to format a data file is the ultimate in appropriate laziness, and having to type a full filename in is too much work). To run the script simply type:

```
python convert_quiz.py <filename>.txt
```

The script will strip the <filename> value and apply it to the <filename>\_answers.txt file, so make sure both names are the same.

File format - questions file:
-----------------------------
The file with the questions and selections should begin with the question on one line and each of the selections on a separate line immediately under it. Each selection should begin with a unique letter in order (i.e., "A", "B", "C", etc.) There must be an empty line between the last selection and the next question. Note that the script currently does some trimming at the beginning of the question line to get rid of question numbers (at the beginning of the question) and page numbers (at the end of the question); if you don't have either of these just omit the indexing variables.

**Example:**
```
<This is the first question>
A. <This is the first selection>
B. <This is the second selection>
C. <This is the third selection>
D. <This is the fourth selection>

<This is the second question>
A.<etc. etc.>
```

File format - answer file
-------------------------
The file with the answers in it should have two columns - a question number and a letter value. A row header is also needed to maintain proper indexing; the values don't really matter to the script. The question number and letter value need to be separated by a comma - you can use the find/replace function in your text editor to do this quickly and easily (change "." to ",")

**Example:**
```
<column1>, <column2>
1, A
2, B
3, C
4, D
```
