"""
Rule states on the three files and can only use modules sys, collections, and math
use inputs for file and write functions for one task to feed into another
"""
import math
import sys

def get_variance(column_list, average, valid_num_count):
    """
    Calculates variance for column list provided.
    @param column_list: list of floats
    @param average: float average of the column_list provided
    @param valid_num_count: length of column_list as a float
    @return: calculated float variance
    """
    top = 0.0
    for i in column_list:
        # the total sum of all elements in list for numerator of variance equation
        top += (i - average) ** 2
        # length of valid float entries in list
        bottom = (valid_num_count - 1)
        # checking if list only has one valid number entry and is dividing by zero
        if bottom == 0:
            variance = 0
        else:
            variance = top / (valid_num_count - 1)
    return variance


def get_median(column_list):
    """
    Calculates median of column list provided.
    @param column_list: list of floats
    @return: calculated median value of list as a float
    """
    # sort list
    copy_list = column_list.copy()
    copy_list.sort()
    # is the column list even?
    is_even = len(copy_list) % 2 == 0
    # if even number of elements in list
    if is_even:
        middle = (len(copy_list) - 1) / 2
        floor_middle = math.floor(middle)
        ceil_middle = math.ceil(middle)
        median = (copy_list[floor_middle] + copy_list[ceil_middle]) / 2
    # if odd number of elements in list
    else:
        middle = int((len(copy_list) - 1) / 2)
        median = copy_list[middle]
    return median


def main():
    """
    Open a provided text file with values that are tab deliminated.
    Then compile a list of floats for the column of interest.
    Print out descriptive statistics for the column of interest and any errors encountered.
    """
    column_x = []
    total_count = 0.0

    with open(sys.argv[1], 'r') as data:
        for line in data:

            # count for all lines in file, which is total number of elements
            total_count += 1

            # extract the value for a given column number (index position)
            try:
                number = line.split("\t")[int(sys.argv[2])]
            except IndexError:
                prompt2 = "Exiting: There is no valid 'list index' in column "
                print(f"\n{prompt2}{sys.argv[2]} in line {total_count} in file: {sys.argv[1]}\n")
                sys.exit()

            # convert all extracted values to floats
            try:
                number = float(number)
            except ValueError:
                prompt = ": could not convert string to float: "
                print(f"\nSkipping line number {total_count}{prompt}'{number}'")
                continue

            # compile floats into a list
            if not math.isnan(number):
                # remove print function, nan will just skip without
                column_x.append(number)

        # check for empty list
        if column_x == []:
            prompt3 = "There were no valid number(s)"
            print(f"\nError: {prompt3} in column {sys.argv[2]} in file: {sys.argv[1]}\n")
            sys.exit()

    # Descriptive statistic calculations
    valid_num_count = float(len(column_x))
    average = sum(column_x) / valid_num_count
    maximum_value = max(column_x)
    minimum_value = min(column_x)
    variance = get_variance(column_x, average, valid_num_count)
    standard_deviation = math.sqrt(variance)
    median = get_median(column_x)

    print(f"\n\tColumn: {sys.argv[2]}")
    print(f"\n\n\t\t{'Count':10}={total_count:>10.3f})")
    print(f"\t\t{'ValidNum':10}={valid_num_count:>10.3f}")
    print(f"\t\t{'Average':10}={average:>10.3f}")
    print(f"\t\t{'Maximum':10}={maximum_value:>10.3f}")
    print(f"\t\t{'Minimum':10}={minimum_value:>10.3f}")
    print(f"\t\t{'Variance':10}={variance:>10.3f}")
    print(f"\t\t{'Std Dev':10}={standard_deviation:>10.3f}")
    print(f"\t\t{'Median':10}={median:>10.3f}\n")


if __name__ == '__main__':
    main()
