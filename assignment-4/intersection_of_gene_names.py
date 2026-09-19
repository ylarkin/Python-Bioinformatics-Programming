"""
input 2 files via commandline argparse flags
files contain gene symbols first tab delimited from the rest of the information
create sets of both files for comparison and a final alphabetic intersection output file
"""
import argparse
from assignment4.io_utils import get_filehandle


def get_cli_args2():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Provide two gene list (ignore header line),'
                                                 ' find intersection.'
                                                 ' File order is not important.')

    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, default="chr21_genes.txt",
                        help='Gene symbol tab delimited from remaining line entry',
                        required=False)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, default="HUGO_genes.txt",
                        help='Gene symbol tab delimited from remaining line entry',
                        required=False)

    return parser.parse_args()
def get_set_of_gene(file_gene_sym):
    """
    Function used on both files provided
    :param file_gene_sym: the input file provided by argparse command line
    :return: a set of gene symbols from the file
    """
    set_gene_symb = set() # create empty set
    for line in file_gene_sym:
        symb_line = line.split("\t")
        # add index 0 of each line in file to set
        set_gene_symb.add(symb_line[0])
    return set_gene_symb


def main():
    '''

    :return:
    '''
    args = get_cli_args2()

    i1_name = args.infile1.lstrip('./ ')
    i2_name = args.infile2.lstrip('./ ')
    outfile = "OUTPUT/intersection_output.txt" # hardcoded
    # filehandles
    fh_in1 = get_filehandle(args.infile1, "r")
    fh_in2 = get_filehandle(args.infile2, mode='r')
    fh_out = get_filehandle(outfile, mode='w')
    # create sets of genes for each file
    infile1_set = get_set_of_gene(fh_in1) # chr21
    infile2_set = get_set_of_gene(fh_in2) # HUGO
    # compare sets
    intersect_both_sets = infile1_set.intersection(infile2_set) # interesection chr21 and HUGO
    unique_infile1 = infile1_set.difference(infile2_set) # unique chr21
    unique_infile2 = infile2_set.difference(infile1_set) # unique HUGO
    # sort set of interest alphabetically to write to file
    alph_order = sorted(intersect_both_sets)
    for i in alph_order:
        fh_out.write(i + "\n")
    # clean up, close files
    fh_in1.close()
    fh_in2.close()
    fh_out.close()
    # print statements
    print(f"Number of unique gene names in {i1_name}: {len(unique_infile1)}")
    print(f"Number of unique gene names in {i2_name}: {len(unique_infile2)}")
    print(f"Number of common gene symbols found: {len(intersect_both_sets)}")
    print(f"Output stored in OUTPUT/intersection_output.txt")

if __name__ == '__main__':
    main()
