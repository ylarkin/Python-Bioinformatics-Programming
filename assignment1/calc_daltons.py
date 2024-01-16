"""
File: calc_daltons.py

Defined protein kinase C beta sequence
hardcoded from external site
calculate average molecular weight
"""

def main():
    """Q1 calc average molecular weight of the protein in kilodaltons."""

    # protein hardcoded from https://www.ncbi.nlm.nih.gov/protein/P68403.3?report=fasta
    pkc = """MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC
    CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH
    KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ
    KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ
    EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK
    GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM
    EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE
    NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY
    PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF
    DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV"""

    # length of the sequence includes the line breaks and indents so need to remove them
    pkc = pkc.replace('\r', '').replace('\n', '').replace('    ', '')
    aa_num = len(pkc)
    print('The length of "Protein kinase C beta type" is : ', aa_num)

    # average aa molecular weight is 110 Daltons; convert daltons to kilodaltons
    avg_kd = 110 * 0.001
    avg_wt_pkc = aa_num * avg_kd
    print('The average weight of this protein sequence in kilodaltons is: ', avg_wt_pkc)


if __name__ == '__main__':
    main()
