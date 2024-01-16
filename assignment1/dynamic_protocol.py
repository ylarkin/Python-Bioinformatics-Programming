'''
File   :  dynamic_protocol.py
cd
Instructor example: how to prepare a 3 ml solution of
10mM NaCl and 0.5 mM MgCl2, given stock solutions
of 1 M NaCl and 0.1 M MgCl2.

Change code to make it ask for user input values
'''

def main():
    """Q3 Adjusted code for user input"""

    # use ml volumes throughout the program
    final_vol = input("Please enter the final volume of the solution (mL): ")
    final_vol = float(final_vol)

    # NaCl user inputs
    # use mM concentrations throught the program
    nacl_stock = input("Please enter the NaCl stock (mM): ")
    nacl_stock = float(nacl_stock)
    nacl_final = input("Please enter the NaCl final (mM): ")
    nacl_final = float(nacl_final)

    # Calc concatenation of NaCl needed using fstring
    step1 = f"Add {str(final_vol * (nacl_final / nacl_stock))} ml NaCl\n"

    # MgCl2 user inputs
    mg_stock = input("Please enter the MgCl2 stock (mM): ")
    mg_stock = float(mg_stock)
    mg_final = input("Please enter the MgCl2 final (mM): ")
    mg_final = float(mg_final)

    # Calc concentration of MgCl2 needed using fstring
    step2 = f"Add {str(final_vol * (mg_final / mg_stock))} ml MgCl2\n"

    # Water addition
    step3 = f"Add water to a final volume of {str(final_vol)} ml and mix"

    # Protocol solutions: print out steps b/c they were formatted earlier
    print(step1 + step2 + step3)


if __name__ == '__main__':
    main()
