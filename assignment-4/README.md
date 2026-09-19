# Assignment 4:
Code 3 programs:

## Program:
    1. gene_names_from_chr21.py
        - optional argsparse terminal inputs for program: 1 file
        - default file settings to run
        - STDOUT only
        - asks user for input: gene symbol to querry the file
    2. find_common_cats.py
        - optional argsparse terminal inputs for program: 2 files
        - default file settings to run
        - give output file of category number,
          of gene symbols with that category assignment, and subcategory description
    3. intersection_of_gene_names.py
        - optional argsparse terminal inputs for program: 2 files
        - default file settings to run
        - STDOUT counts for intersection and unique gene symbols for each file
        - give output file of intersection gene symbols in alphabetical order


## Text Files (numbers correspond to program number):
    - input files provided for testing
        1. chr21_genes.txt
        2. chr21_genes.txt, chr21_genes_categories.txt
        3. chr21_genes.txt, HUGO_genes.txt
    - output files
        1. none
        2. OUTPUT/categories.txt
        3. OUTPUT/intersection_output.txt

## Getting Started

### Dependencies
- python3 : code written using python 3.10.11
- Windows 8 (or newer) OR macOS
- terminal
- module sys
- module os
- module argparse
- module pytest (for test scripts)
- module assignment4 in assignment4 directory for programs

### Installing:
- python.org : to download version of python language
- import sys
- import pytest
- import os
- import argparse

### Linting and Testing:
- pylint and flake 8 used with multiple parameters disabled
- run_lints.sh
- .coveragerc worked on linux but difficulties on windows

### Executing program:
- Run programs in terminal directly, not through IDE, under directory ...\assignment3\
  - Program 1 Template Format:
    ```
    C:\Users\....\assignment3> [language: python] [progam to run] [flag: '-i'] [input file name] 
    ```
  - Windows Command (example uses file name: data_file.txt)
    ```
    C:\Users\...\assignment3> python .\secondary_structure_splitter.py -i ss.txt
    ```
  - macOS Command (example uses program name: calc_daltons.py)
    ```
    C:\Users\...\BINF6200\assignment3> python3 .\secondary_structure_splitter.py -i ss.txt
    ```
  - Program 2 Template Format:
      ```
  C:\Users\....\assignment3> [language: python] [progam to run] [flag: '-i']
                             [input file name] [flag2: -o] [output file name]
      ```
  - Windows Command (example uses file name: data_file.txt)
    ```
    C:\Users\...\assignment3> python .\secondary_structure_splitter.py -i influenza.fasta -o influ_count.txt
    ```
  - macOS Command (example uses program name: calc_daltons.py)
    ```
    C:\Users\...\BINF6200\assignment3> python3 .\secondary_structure_splitter.py -i influenza.fasta -o influ_count.txt

## Authors:
Yvonne Larkin
(email) larkin.y@northeastern.edu

## Version History:
- Version 1.0
  - code ran through pylint and flake8 numerous times
  - borrowed a (non-classmate) friend's linux to run program through run_lints.sh
  - no previous versions of code formally implemented- though many hours of trial and error 

## License (N/A)

## Acknowledgments:
- Dominique Pizzie : [github README.md example.](https://gist.githubusercontent.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc/raw/d59043abbb123089ad6602aba571121b71d91d7f/README-Template.md)
- Chesley Leslin : Canvas Announcements, assignment hints, lecture, and example code lines
- Johanna Regan : previous assignment feedback and clarifications for formatting; 
                  office hour clarifications for testing section
