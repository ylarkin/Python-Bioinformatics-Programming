# Assignment 5:
Code 1 programs and 2 modules:

## Program:
    1. get_gene_level_information.py
        - optional argsparse terminal inputs for program: gene and host
        - default file settings to run
        - STDERR for hosts that aren't found
## Modules
    1. config.py
        - contains 2 global variables
        - a function per global variable to return
        - function to return a dictionary of host names
        - ErrorType configs
    2. io_utils.py
        - get filehandle function
        - boolean test for if a file is valid


## Text Files:
    - not included in zipfile
    - large import of assignment5_data containing 6 subdirectories by host
    - each subdirectory contains text files of a gene
    - these files were used to test the program

## Getting Started

### Dependencies
- python3 : code written using python 3.10.11
- Windows 8 (or newer) OR macOS
- terminal
- module argparse
- module os
- module pytest (for test scripts)
- module re
- module sys
- module assignment5 in assignment5 directory for programs
- files assignment5_data in assignment5 outer most directory

### Installing:
- python.org : to download version of python language
- import argparse
- import os
- import pytest
- import re
- import sys

### Linting and Testing:
- pylint and flake 8 used with multiple parameters disabled
- run_lints.sh
- .coveragerc worked on linux but difficulties on windows

### Executing program:
- Run programs in terminal directly, not through IDE, under directory ...\assignment3\
  - Program 1 Template Format:
    ```
    C:\Users\....\assignment5> [language: python(3)] [progam to run] [flag: '--gene'] [gene name] [flag: --host] [host name]

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
