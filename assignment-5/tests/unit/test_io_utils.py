"""
Test suite for assignment5 io_utils module
"""
import os
import sys
import pytest
from assignment5.io_utils import get_filehandle, is_gene_file_valid
sys.path.insert(0, 'assignment5/assignment5')
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_filehandle_for_OSError
# " doesn't conform to snake_case naming style"
# pylint: disable=C0103
# io_utils Program only
# test file for writing or reading respective to test
FILE_TO_TEST = "test_file.txt"


def test_existing_get_filehandle_for_reading():
    # does it open a file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    # clean up
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    # does it open a file for writing
    # test
    test = get_filehandle(FILE_TO_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    # clean up
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_OSError():
    # does it raise OSError
    # this should exit
    # use file that is not in test suite
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_ValueError():
    # does it raise ValueError for incorrect mode
    # this should exit
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)

def _create_file_for_testing(file):
    # helper function in test suite to help test program function
    # create a test file
    open(file, "w").close()


def test_is_gene_file_valid():
    # test file for True
    _create_file_for_testing(FILE_TO_TEST)
    assert is_gene_file_valid(FILE_TO_TEST) is True
    os.remove(FILE_TO_TEST)


def test_is_gene_file_valid():
    # test file for False
    file = "file_does_not_exist.txt"
    assert is_gene_file_valid(file) is False
