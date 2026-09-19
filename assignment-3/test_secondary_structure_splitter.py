"""

"""
import os
import pytest

from secondary_structure_splitter import (get_cli_args, get_filehandle, get_fasta_lists, _verify_lists,
                            outfile_results, main)

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name 'test_get_filehandle_for_OSError'
# doesn't conform to snake_case naming style"
# pylint: diavle=C0103

FILE_TO_TEST = "test_file.txt"
FILE_TO_TEST_PARSING = "test_file.fasta"
FASTA_STR_TO_TEST = """\n
>TEST1 A/TEST/2006 2006// 4 (HA)
ATGAAAAATTTGACAAATTGTACATTTGGGGGGTTCACCACCCGGGTACGGACAATGACCAAATCTTCCT
GTATGCTCAAGCATCAGGAAGAATCACAGTCTCTACCAAAAGAAGCCAACAGACTGTAATCCCGAATATC
GGATCTAGACCCAGAGTAAGGAATATCCCCAGCAGAATAAGCATCTATTGGACAATAGTAAAACCGGGAG
ACATACTTTTGATTAACAGCACAGGGAATTTAATTGCTCCTAGGGGTTACTTCAAAATACGAAGTGGGAA
>TEST2 A/TEST/2006 2006// 4 (HA)
AAACAACAAAGAGAAAGAAGTCCTTGTACTATGGGGTGTCCATCACCCGCCTAACATAGGGGACCAAAGG
GCCCTCTATCATACGGAAAATGCTTATGTCTCTGTAGTGTCTTCACATTATAGCAGAAGATTCACCCCAG
>TEST3 A/TEST/TEST/2006 2006// 4 (HA)
CGGGGATACAATAATATTTGAGGCAAATGGGAATCTAATAGCGCCAAGGTTTGCTTTCGCACTGAGTAGA
GGCTTGGGATCAGGAATCATCACCTCAAATGCACCAATGGATGAATGTGATGCGAAATGTCAAACACCTC
AGGGAGCTATAAACAGCAGTCTTCCTTTCCAGAATGTACACCCAGTCACAATAGGAGAGTGTCCAAAGTA
TGTCAGGAGTGCAAAATTAAGGATGGTTACAGGACTAAGGAACATCCCATCCATTCAATCCAGAGGTTTG
>EU521894 A/Arequipa/FLU3845/2006 2006// 4 (HA)
ACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAGTGAAAACAATCACGAATGACC
AAATTGAAGTTACTAATGCTACTGAGCTGGTTCAGAGTTCCTCAACAGGTGAAATATGCGACAGTCCTCA
TCAGATCCTTGATGGAGAAAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGTGATGGCTTC
"""
FILE_TO_TEST_NT_STATS = "test_nt_fasta_stats.txt"


def test_existing_get_filehandle_for_reading():
    # does it open a file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    #test
    test = get_filehandle(FILE_TO_TEST, 'r')
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    # does it open a file for writing
    # create a test file
    _create_file_for_testing(FILE_TO_TEST_PARSING)
    # test
    test = get_filehandle(FILE_TO_TEST_PARSING, 'w')
    assert hasattr(test, "writelines") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST_PARSING)


def test_get_filehandle_for_ValueError():
    # does it raise ValueError
    # this should exit
    with pytest.raises(ValueError):
        # use rrr to represent any wrong value for mode
        get_filehandle(FILE_TO_TEST, 'rrr')


def test_get_filehandle_for_OSError():
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def _create_file_for_testing(file):
    # not actually run, it is just a helper function for the test script
    # create a test file
    open(file, 'w').close()


def _create_fasta_file_for_testing():
    # not actually run, it is just a helper function for the test script
    with open(FILE_TO_TEST_PARSING, 'w') as fh:
        fh.write(FASTA_STR_TO_TEST)


def test_get_fasta_lists():
    _create_fasta_file_for_testing()
    # does it make a header list and a seq_list
    test = get_filehandle(FILE_TO_TEST_PARSING, 'r')
    header_list, seq_list = get_fasta_lists(test)
    assert header_list != []
    assert seq_list != []


def test_verify_lists():
    _create_fasta_file_for_testing()
    # are the lists equal lengths
    test = get_filehandle(FILE_TO_TEST_PARSING, 'r')
    header_list, seq_list = get_fasta_lists(test)
    _verify_lists(header_list, seq_list)
    assert len(header_list) == len(seq_list)