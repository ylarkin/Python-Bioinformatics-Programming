"""
File: calc_number_amino_acids.py

Interactive calculation of protein's average molecular weight
Ask the user for gene name and nucleic acid sequence length
From input, determines if an average molecular weight can be calculated
If yes, code calculations average protein weight in kilodaltons
"""

import sys
def main():
    """Q2 Calculate the average molecular weight for a given user input sequence"""

    # ask user for gene name and sequence length
    user_gene = input("\nPlease enter a name for the DNA sequence: ")
    print("Your sequence name is: ", user_gene)
    user_gene_na_num = input("Please enter the length of the sequence: ")
    user_gene_na_num = float(user_gene_na_num)


    # only give a molec. wt calc. if sequence is divisible by 3
    if user_gene_na_num % 3 == 0:
        print("The length of the DNA sequence is: ", user_gene_na_num)
        # calc the number of amino acids based on number of nucleic acids; 1 aa is a codon of 3 na
        user_gene_aa_num = user_gene_na_num / 3
        print("The length of the decoded protein is: ", user_gene_aa_num)
        # calc the average kD weight; avg aa = 110 D or 0.110 kD
        user_gene_avg_wt = user_gene_aa_num * 0.110
        print("The average weight of the protein sequence is: ", user_gene_avg_wt)
    else:
        print("\n\nError: the DNA sequence is not a multiple of 3", file=sys.stderr)
        # exit program with sys.exit(); give a non-zero exit value b/c 0=successful termination
        sys.exit(1)


if __name__ == '__main__':
    main()
