"""
Extract Gene level information:
print which tissues is a given host contain the specified gene
if gene is not found this is told to user and exit
if host is not found directory of valid host names are given
"""
import argparse
import os
import re
import sys
from assignment5 import config
from assignment5 import io_utils


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments: host and gene
    """
    parser = argparse.ArgumentParser(description='Provide the host name and gene name for lookup')

    parser.add_argument('--host', dest='host',
                        type=str, default="Human",
                        help='Name of Host', required=False)
    parser.add_argument('-g', '--gene', dest='gene',
                        type=str, default="TGM1",
                        help='Name of Gene', required=False)
    args = parser.parse_args()
    return args


def update_host_name(host_name):
    """
    convert the input to a usable form for lookup in the
    dictionary returned by config.get_keywords_for_hosts()
    :param host_name: user input host name by args flag
    :return: the scientific file name value that corresponds
            to that common or scientific key input
    """
    dict_sci_names = config.get_keywords_for_hosts()
    user_input = host_name.casefold()
    # Split the input into words, strip spaces, and join with underscores
    formatted_input = '_'.join(word.strip() for word in user_input.split())
    host = formatted_input.replace('_', ' ')
    try:
        host_name_keyvalue = dict_sci_names[host]
    except KeyError:
        _print_directories_for_hosts()
        sys.exit(1)

    return host_name_keyvalue


def _print_directories_for_hosts():
    """
    Receives no arguments, helper function to tell user all
    acceptable host inputs
    :return: list of common and scientific names for host
    """
    dict_keyword = config.get_keywords_for_hosts()
    set_keywords = set(dict_keyword.values())
    sorted_values = sorted(set_keywords)
    sorted_keys = sorted([key.capitalize() for key in dict_keyword])
    print(f'\n\nEither the Host Name you are searching for is not in the database'
          f'\n\nor If you are trying to use the scientific name please put the '
          f'name in double quotes:\n\n"Scientific name"\n\nHere is a (non-case '
          f'sensitive) list of available Hosts by scientific name\n\n',
          file=sys.stderr)
    for index, value in enumerate(sorted_values, start=1):
        print(f"  {index}. {value}", file=sys.stderr)
    print(f'\n\nHere is a (non-case sensitive) list of available Hosts '
          f'by common name\n', file=sys.stderr)
    for index, key in enumerate(sorted_keys, start=1):
        print(f"{index: 3}. {key}", file=sys.stderr)


def get_data_for_gene_file(gene_fh):
    """
    :param gene_fh: filehandle to read gene information
    and extract tissue list
    :return: alphabetically sorted tissue list
    """
    for line in gene_fh:
        # Find the line containing the tissue expression information
        match = re.search(r'^EXPRESS\s+(.*)', line)
        if match:
            tissue_string = match.group(1)
            tissue_express_list = tissue_string.split('|')
            # strip any extra space around list items
            tissue_list = [i.strip() for i in tissue_express_list]

    sorted_tissue_list = sorted(tissue_list)
    return sorted_tissue_list


def print_host_to_gene_name_output(host_name, gene_name, sorted_tissue_list):
    """
    formatted print output
    :param host_name: updated host name from user original flag input
    :param gene_name: gene flag input
    :param sorted_tissue_list: returned list from get_data_for_gene_file()
    :return: printed alphabetic list of tissue for gene in host
    """
    host = host_name.replace('_', ' ')
    print(f'In {host}, There are {len(sorted_tissue_list)} '
          f'tissues that {gene_name} is expressed in:\n')
    # Print the enumerated items from the tissue_express_list
    for index, item in enumerate(sorted_tissue_list, start=1):
        print(f"{index: 3}. {item.capitalize()}")


def main():
    """
    Lookup user input gene and host to give a list of all
    tissues that gene is found in for host
    If the file does not exist, it will tell user, exit,
    and providing directory list of hosts
    """
    args = get_cli_args()
    # variables for lookup
    temp_host = args.host
    gene = args.gene
    host = update_host_name(temp_host)
    # create file path
    file = os.path.join(config.get_directory_for_unigene(),
                        host, gene + "." + config.get_extension_for_unigene())
    if io_utils.is_gene_file_valid(file):
        print(f"\nFound Gene {gene} for {host}")
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {temp_host}. "
              f"exiting now...", file=sys.stderr)
        sys.exit(1)
    fh_gene_file = io_utils.get_filehandle(file, 'r')
    sorted_tissue_list = get_data_for_gene_file(fh_gene_file)
    print_host_to_gene_name_output(host, gene, sorted_tissue_list)
    fh_gene_file.close()


if __name__ == '__main__':
    main()
