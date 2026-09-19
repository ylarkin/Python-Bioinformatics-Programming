"""
takes terminal argument for infile and outfile
will take the infile and process it
for descriptive counts to print to outfile
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
    parser.add_argument('-i', '--infile', dest='open_file', type=str,
                        help='Path to file to open', required=True)
    parser.add_argument('-o', '--outfile', dest='write_file', type=str,
                        help="Path to file to write", required=True)
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


def get_fasta_lists(file_input):
    """
    splits fasta file into 2 lists,
    one for headers and one for sequences
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
    for line in file_input:
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


def output_results_to_files(header_list, seq_list, write_file):
    """
    Takes data from the argsparse file input and
    split into two lists by get_fasta_list()
    Takes count of all instances of a na in a sequence, length of seq and %GC
    writes the descriptive results to argsparse out file given
    :param header_list: output result from get_fasta_list()
    :param seq_list: output result from get_fasta_list()
    :param write_file: argsparse file given in terminal
    :return:
    """
    counter = 0
    write_file.write(f"Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n")
    for header in header_list:
        counter += 1
        index = header_list.index(header)
        seq = seq_list[index]
        accession_string = _get_ncbi_accession(header)
        nt_a = _get_num_nucleotides('A', seq)
        nt_c = _get_num_nucleotides('C', seq)
        nt_t = _get_num_nucleotides('T', seq)
        nt_g = _get_num_nucleotides('G', seq)
        nt_n = _get_num_nucleotides('N', seq)
        perc_gc = "{:.1f}".format(((nt_g + nt_c)/(len(seq)))*100)
        write_file.write(f"{counter}\t{accession_string}\t{nt_a}\t{nt_g}\t{nt_c}\t{nt_t}\t{nt_n}\t{len(seq)}\t{perc_gc}\n")


def _get_num_nucleotides(na_value, sequence):
    """
    loops through the sequence to count instances of a given na value
    :param na_value: nucleotide of interest
    :param sequence: sequence of interest
    :return: number of times na is found in that sequence
    """
    count = 0
    list_na = ['A', 'T', 'C', 'G', 'N']
    if na_value not in list_na:
        raise sys.exit("Did not code this condition")
    for nucleotide in sequence:
        if nucleotide == na_value:
            count += 1
    return count


def _get_ncbi_accession(header):
    """
    split header into a list
    isolate the zero index
    strip away unwanted information
    :param header: header from header_list
    :return: accession number for that FASTA header
    """
    header_string = header.split()
    accession = header_string[0].lstrip('>')
    return accession


def print_sequence_stats():
    """
    Main function calling on all other functions to produce the final outfile
    based on the provided infile being processed
    :return: outfile with descriptive results for infile
    """
    args = get_cli_args()

    fh_in = get_filehandle(args.open_file, 'r')
    fh_out = get_filehandle(args.write_file, 'w')
    # get 2 lists of data and unpack into variables
    header_list, seq_list = get_fasta_lists(fh_in)
    # get file with descriptive counts of sequence data
    output_results_to_files(header_list, seq_list, fh_out)
    fh_in.close()
    fh_out.close()


if __name__ == '__main__':
    print_sequence_stats()
