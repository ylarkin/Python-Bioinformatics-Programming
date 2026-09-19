"""
Receives 2 input files via command line, file order is important
first file is (3 objects tab delimited) gene symbol, description and subcategory
second file is (2 objects tab delimited) subcategory and cat description
This will create a nested dictionary to count the number of genes in each subcat
"""
import argparse
from assignment4.io_utils import get_filehandle


def get_cli_args2():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Provide tab delimited gene file.'
                                                 ' File order is important.')

    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, default="chr21_genes.txt",
                        help='Gene symbol, descr, subcat', required=False)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, default="chr21_genes_categories.txt",
                        help='Subcategory and description', required=False)

    return parser.parse_args()
def get_dict_cat_gene(infile):
    """
    create dictionary from fh_in
    :param infile: file handle from argsparse argument imported from assignment4
    open file and read
    :return: dictionary of key gene symbol and value gene description
    """
    dict_cat_dict_gene_descr = {}  # create empty dictionary
    infile.readline()  # skip header
    for line in infile:
        try:
            gene_symbol, gene_description, gene_subcategory = line.strip().split("\t")
        except ValueError:
            break
        # key is gene symbol, value is a tuple of the description and category
        if gene_subcategory not in dict_cat_dict_gene_descr.keys():
            dict_cat_dict_gene_descr[gene_subcategory] = {}
            dict_cat_dict_gene_descr[gene_subcategory][gene_symbol] = [gene_description]
        else:
            dict_cat_dict_gene_descr[gene_subcategory][gene_symbol] = [gene_description]

    return dict_cat_dict_gene_descr # D of D


def get_dict_list_subcat(infile2):
    """
    create dictionary from fh_in2
    :param infile: file handle from argsparse argument imported from assignment4
    open file and read
    :return: dictionary of key gene symbol and value gene description
    """
    dict_subcat_descr = {}

    for line in infile2:
        subcategory, subcat_description = line.split("\t")
        # key is gene subcategory, value is subcategory description
        dict_subcat_descr[subcategory] = subcat_description.rstrip("\n")
    return dict_subcat_descr


def gen_value_key_order(dict_of_dict):
    """
    generator function, so not stored and exhausted
    :param dict_of_dict: This is the nested dictionary of key subcategories and dict
    nest dictionary is gene symbol and description
    need the number of nested keys to determine how many of each subcategory exist
    previous function already ignored blank category gene
    :return: subcategory number and corresponding count of genes that have that cat
    """
    for subcat, dict_values in dict_of_dict.items():
        nested_keys = dict_values.keys()
        count = len(nested_keys)
        yield subcat, count


def main():
    """
    needs 2 input files from argparse command line
    :return: output file generated
    of category, count of genes in that category and the category description
    """
    args = get_cli_args2()

    infile1 = args.infile1 # chr21_genes.txt
    infile2 = args.infile2 # chr21_genes_categories.txt
    outfile = "OUTPUT/categories.txt" # hardcoded

    # filehandles
    fh_in1 = get_filehandle(infile1, "r")
    fh_in2 = get_filehandle(infile2, mode="r")
    fh_out = get_filehandle(outfile, mode="w")

    # dictionary of files
    dict_cat_dict_gene = get_dict_cat_gene(fh_in1)
    dict_cat_descr = get_dict_list_subcat(fh_in2)

    # write to hardcoded output file
    fh_out.write(f'Category\tOccurrence\tDescription\n')
    for subcat, counter in gen_value_key_order(dict_cat_dict_gene):
        # convert floats to string and format to variable for one argument
        string_output = str(subcat) + "\t" + str(counter) + "\t" + dict_cat_descr[subcat] + "\n"
        fh_out.write(string_output)

    # clean up, close files
    fh_in1.close()
    fh_in2.close()
    fh_out.close()

if __name__ == '__main__':
    main()
