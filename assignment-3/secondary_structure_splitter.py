"""
Program to receive a combined file
with protein sequence and secondary structures
and create two separate files
with respective information

"""

import argparse
import sys


def get_cli_args():
    """
    void: get_sli_args()
    takes: no arguments
    @returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='write to fh_out from fh_in')
    # add infile and help arguments to call in terminal
    parser.add_argument('-i', '--infile', dest='file_path', type=str,
                        help='Path to file to open',
                        required=True)
    # return the argument called
    return parser.parse_args()


def get_filehandle(file_name, mode):
    """
    uses argsparse to give a file and mode to be run in the program
    :param file_name: argsparse file name given in the terminal line
    :param mode: argsparse mod give in the terminal line
    :return: file_handle, object to call on in subsequent function
    """
    try:
        file_handle = open(file_name, mode)
    except ValueError:
        raise ValueError("Exit:Value error: second argument mode is either 'r' or 'w'")
    except OSError:
        raise OSError("Exit:File not found")
    return file_handle


def get_fasta_lists(file_handle):
    """
    splits fasta file into 2 lists,
    one for the headers and one for the sequence
    contains both aa and sec structure data
    :param file_handle: parameter provided from get_filehandle()
    :return: 2 lists: header list and sequence list
    """
    # create variables with empty objects to append to and reassign values
    header_list = []
    seq_list = []
    header = ""
    seq = ""
    # protect code for try to open
    for line in file_handle:
        if line.startswith('>'):
            if header != "" and seq != "":
                header_list.append(header)
                # append before the reset
                # but after the last addition to seq string
                seq_list.append(seq)
            header = line.strip('\n')
            seq = ""
        else:
            seq = seq + line.strip('\n')
    # final seq header and value appended
    header_list.append(header)
    seq_list.append(seq)
    _verify_lists(header_list, seq_list)
    return header_list, seq_list


def _verify_lists(list1, list2):
    """
    :param list1: list of headers
    :param list2: list of sequences
    :return: no value return unless lists are not equal, print error
    """
    if len(list1) != len(list2):
        raise sys.exit("The two lists are not of equal element size")
    return True


def outfile_results(header_list, seq_list, fh_out1, fh_out2):
    """
    Takes the lists and loops through,
    write relevant data to the respective file
    :param header_list: list of all headers from text file
    :param seq_list: list of aa and ss sequences from text file
    :param fh_out1: the hard coded pdb_protein.fasta file
    :param fh_out2: the hard coded pdb_ss.fasta file
    :return: the 2 files written to with respective data from the 2 lists
    """
    for header in header_list:
        if "sequence" in header:
            index = header_list.index(header)
            fh_out1.write(f"{header}\n")
            fh_out1.write(f"{seq_list[index]}\n")

    for header in header_list:
        if "secstr" in header:
            index = header_list.index(header)
            fh_out2.write(f"{header}\n")
            fh_out2.write(f"{seq_list[index]}\n")
    return fh_out1, fh_out2


def main():
    """
    call on other functions in program
    to split one provided file into 2 written:
    one contains only aa sequence related data
    and the other has only secondary structure related data
    :return: 2 written files: one for aa and one for sstr
    """
    args = get_cli_args()
    input_file = args.file_path
    # hardcode files path to write
    outfile1 = "pdb_protein.fasta"
    outfile2 = "pdb_ss.fasta"
    # get filehandle for the 3 files
    fh_in = get_filehandle(input_file, 'r')
    fh_out1 = get_filehandle(outfile1, 'w')
    fh_out2 = get_filehandle(outfile2, 'w')
    # get 2 lists and unpack into variables
    header_list, seq_list = get_fasta_lists(fh_in)
    # get 2 files and unpack into variables
    num_aa, num_ss = outfile_results(header_list, seq_list, fh_out1, fh_out2)
    # writing this to STDERR
    sys.stderr.write("Found {} protein sequences\n".format(num_aa))
    sys.stderr.write("Found {} ss sequences\n".format(num_ss))
    # close all files
    fh_in.close()
    fh_out1.close()
    fh_out2.close()


if __name__ == '__main__':
    main()
