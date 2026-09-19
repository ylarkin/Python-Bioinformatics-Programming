"""
Using argparse for one file input
asks user for gene symbol and checks the file for gene
if gene is present it provides the gene description
will loop until told to quit
"""
import argparse
import sys
from assignment4.io_utils import get_filehandle


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Provide tab delimited gene file'
                                                 'gene symbols')

    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, default="chr21_genes.txt", help='Path to file to open',
                        required=False)

    return parser.parse_args()
def get_dict_symbol_descript(file_input):
    """
    create dictionary from fh_in
    :param file_input: file handle from argparse argument imported from assignment4
    open file and read
    :return: dictionary of dictionaries
    outer dictionary key is gene subcategory and value is nested dictionary
    nested dictionary key is gene symbol and value is gene description
    """
    dict_of_gene_descript = {}  # create empty dictionary
    gene_symb_list = []  # create empty list for symbols
    for line in file_input:
        line_entry = line.split("\t")
        gene_symb_list.append(line_entry[0])
        # key is gene symbol with original case maintained wanted to avoid casefold in dictionary
        # values are tuple of description and subcategory
        dict_of_gene_descript[line_entry[0]] = (line_entry[1], line_entry[2].rstrip("\n"))
    # wanted 2 separate functions but had difficulty with the file being opened already
    return dict_of_gene_descript, gene_symb_list


def get_list_casefold_symb(symb_list):
    """
    This is used to erase case sensitivity from the user input but maintain true case in dictionary
    :param symb_list: list of gene symbols
    :return: casefold (all true lowercase) gene symbols
    """
    get_index_list = []
    for i in symb_list:
        # make everything true lowercase for searching
        i = i.casefold()
        get_index_list.append(i)

    return get_index_list


def main():
    """
    Asks use for gene symbol input
    searches for input without case sensitivity
    checks if it exists in the provided file
    :return: if gene symbol is in file it returns the gene description
    """
    args = get_cli_args()
    infile = args.infile  # infile chr21_genes.txt
    fh_in = get_filehandle(infile, "r")

    dict_of_gene_descript, gene_symb_list = get_dict_symbol_descript(fh_in)
    get_index = get_list_casefold_symb(gene_symb_list)

    # infinite loop to have user input gene symbols until quit
    # more convoluted because I didn't want to use casefold in dictionary creation
    while True:
        gene_symbol = input("Enter gene name of interest. Type quit to exit: ")
        gene_lookup = gene_symbol.casefold()

        if gene_lookup == "quit":
            print("Thanks for querying the data.")
            sys.exit()
        try:
            # get index position to correspond in original list for true symbol case
            index_pos = get_index.index(gene_lookup)
            original_sym = gene_symb_list[index_pos]
        except ValueError:
            print(f"Not a valid gene name.\n")
        else:
            # search dictionary with original case
            value = dict_of_gene_descript[original_sym]
            # print true case of gene symbol not input
            print(f"{original_sym} found! Here is the description:\n{value[0]}\n")

        # clean up, close filehandles
        fh_in.close()


if __name__ == '__main__':
    main()
