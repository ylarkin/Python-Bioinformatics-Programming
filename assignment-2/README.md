# Assignment 2:
Code a program, using only modules sys and math, to open a text file with tab-deliminated values and compile a column for statistical analysis. Open file in terminal using the sys.argv[], where sys.argv[1] is the file and sys.artgv[2] is the column number you want to anylize. write a README.md file, and zip all together for submission.
Follow rubric criteria and make sure code passes pylint test.

## Program:
    1. stats_in_python.py
        - Opens text file (defined below) and calculate stats on valid float entries
        - Return specific print values depending on the <ErrorType> encountered
        - calculates: 
            1. Count number of elements in compiled column
            2. Count number of valid float entries in compiled column
            3. Calculate average for valid floats
            4. Calculate maximum for compiled column of valid float entries
            5. Calculate minimum for compiled column of valid float entries
            6. Calculate variance for compiled column of valid float entries
            7. Calculate standard deviation for compiled column of valid float entries
            8. Calculate median value for compiled column of valid float entries

## Text Files:
    - text files with lines of tab-deliminated values that the program then converts into column lists
    - practice text file examples not included in zip folder:
        1. data_file.txt
        2. data_file2.txt
        3. data_file3.txt

## Getting Started

### Dependencies
- python3 : code written using python 3.10.11
- Windows 8 (or newer) OR macOS
- terminal
- module sys
- module math

### Installing:
- python.org : to download version of python language
- import sys
- import math

### Executing program:
- Run programs in terminal directly, not through IDE, under directory ...\assignment2\
  - Template Format:
    ```
    C:\Users\....\assignment2> [language: python] [progam to run] [sys.argv[1]: file name] [sys.argv[2]: column number] 
    ```
  - Windows Command (example uses file name: data_file.txt)
    ```
    C:\Users\...\programming6200> cd ./assignment2
    C:\Users\...\assignment2> python .\stats_in_python.py data_file.txt 3
    ```
  - macOS Command (example uses program name: calc_daltons.py)
    ```
    C:\Users\...\programming6200> cd ./assignment2
    C:\Users\...\BINF6200\assignment1> python3 .\stats_in_python.py data_file.txt 3
    ```

## Authors:

Yvonne Larkin
(email) larkin.y@northeastern.edu

## Version History:
- Version 1.0
  - code ran through pylint numerous times until formatting was rated 10.0/10
  - no previous versions of code implemented formally though many hours of trial and error 

## License (N/A)

## Acknowledgments:
- Dominique Pizzie : [github README.md example.](https://gist.githubusercontent.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc/raw/d59043abbb123089ad6602aba571121b71d91d7f/README-Template.md)
- Chesley Leslin : Canvas Announcements, assignment hints and example code lines
- Muzhdah Waqar : office hours clarification on pylint and general formatting for assignment1
